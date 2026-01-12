import numpy as np
import logging
import os
import glob
import h5py


logger = logging.getLogger(__name__)


class XpcsDataset(object):
    def __init__(
        self,
        fname,
        begin_frame=1,
        end_frame=-1,
        stride_frame=1,
        avg_frame=1,
        batch_size=128,
        det_size=(512, 1024),
        device="cuda:0",
        use_loader=False,
        dtype=np.uint8,
        mask_crop=None,
    ):

        self.fname = fname
        self.raw_size = os.path.getsize(fname) / (1024**2)
        self.det_size = det_size
        self.pixel_num = self.det_size[0] * self.det_size[1]
        self.is_sparse = True

        self.mask_crop = mask_crop

        self.device = device

        self.batch_size = batch_size
        self.batch_num = 0
        self.frame_num = 0
        self.frame_num_raw = 0
        self.begin_frame = begin_frame
        self.end_frame = end_frame
        self.avg_frame = avg_frame
        self.stride = stride_frame

        self.use_loader = use_loader
        self.dtype = dtype
        self.dataset_type = None
        self.dtype_raw = None

    def get_data(self, roi_list):
        data_list = [[] for _ in range(len(roi_list))]

        for n in range(self.batch_num):
            x = self.__getbatch__(n).reshape(-1, *self.det_size)
            for m, roi in enumerate(roi_list):
                data_list[m].append(x[:, roi[0], roi[1]])

        for m in range(len(roi_list)):
            data_list[m] = np.vstack(data_list[m])

        return data_list

    def get_scattering(self, num_frames=-1, begin_idx=0):
        size = self.det_size[0] * self.det_size[1]
        saxs = np.zeros(shape=size, dtype=np.float32)
        curr_idx = 0

        if num_frames <= 0:
            num_frames = self.frame_num_raw - begin_idx
        end_idx = num_frames + begin_idx
        end_idx = min(end_idx, self.frame_num_raw)
        # print(begin_idx, end_idx, num_frames)

        total = 0
        sub_l = np.zeros_like(saxs)
        sub_r = np.zeros_like(saxs)
        for n in range(self.batch_num):
            # from curr_idx to curr_idx + self.batch_num
            x = self.__getbatch__(n)
            saxs += np.sum(x, axis=0)
            total += x.shape[0]

            if curr_idx + self.batch_size >= end_idx:
                sub_r += np.sum(x[end_idx - curr_idx :], axis=0)
                total -= x[end_idx - curr_idx :].shape[0]
                break

            if begin_idx > curr_idx:
                sub_l += np.sum(x[0 : begin_idx - curr_idx], axis=0)
                total -= x[0 : begin_idx - curr_idx].shape[0]

            curr_idx += self.batch_size
        saxs = (saxs - sub_l - sub_r) / num_frames
        saxs = saxs.reshape(self.det_size)
        # print(total, num_frames)
        return saxs

    def update_batch_info(self, frame_num):
        self.frame_num_raw = frame_num
        if self.end_frame <= 0:
            self.end_frame = frame_num

        tot = self.end_frame - (self.begin_frame - 1)
        eff_len = self.avg_frame * self.stride
        tot = tot // eff_len * eff_len
        end_frame = self.begin_frame - 1 + tot
        if self.end_frame != end_frame:
            logger.info("end_frame is rounded to the nearest number")
            self.end_frame = end_frame

        self.frame_num = tot // eff_len
        self.batch_num = (self.frame_num + self.batch_size - 1) // self.batch_size

    def update_mask_crop(self, new_mask):
        # some times the qmap's orientation is different from the dataset;
        # after rorating qmap, explicitly apply the new mask; if the original
        # mask is None (ie. not croping), then abort
        if self.mask_crop is None:
            return
        else:
            self.mask_crop = new_mask

    def update_det_size(self, det_size):
        self.det_size = det_size
        self.pixel_num = self.det_size[0] * self.det_size[1]

    def get_raw_index(self, idx):
        # get the raw index list
        eff_len = self.stride * self.avg_frame * self.batch_size
        beg = self.begin_frame - 1 + eff_len * idx
        end = min(self.end_frame, beg + eff_len)
        size = (end - beg) // self.stride
        return beg, end, size

    def get_sparsity(self):
        x = self.__getitem__(0)[0]
        y = (x > 0).sum() / self.pixel_num
        self.dtype_raw = x.dtype
        self.__reset__()
        return y

    def get_description(self):
        result = {}
        for key in [
            "fname",
            "frame_num_raw",
            "is_sparse",
            "frame_num",
            "det_size",
            "device",
            "batch_size",
            "batch_num",
            "dataset_type",
        ]:
            result[key] = self.__dict__[key]
        result["frame_info"] = (
            "(begin, end, stride, avg) = ("
            f"{self.begin_frame}, {self.end_frame}, "
            f"{self.stride}, {self.avg_frame})"
        )
        return result

    def describe(self):
        for key, val in self.get_description().items():
            logger.info(f"{key}: {val}")

        if self.mask_crop is not None:
            valid_size = self.mask_crop.shape[0]
        else:
            valid_size = self.pixel_num
        logger.info(f"dtype is: {self.dtype}")
        logger.info(f"valid_size: {valid_size}")
        logger.info("sparsity: %.4f" % self.get_sparsity())
        logger.info("raw dataset file size: {:,} MB".format(round(self.raw_size, 2)))

    def __len__(self):
        return self.batch_num

    def __reset__(self):
        return

    def __getbatch__(self, idx):
        raise NotImplementedError

    def __getitem__(self, idx):
        x = self.__getbatch__(idx)
        if self.avg_frame > 1:
            x = x.reshape(-1, self.avg_frame, x.shape[-1])
            x = np.mean(x.astype(np.float32), axis=1)
        return x

    def to_rigaku_bin(self, fname):
        """
        convert to rigaku binary format
        """
        offset = 0
        fid = open(fname, "a")
        for n in range(self.batch_num):
            x = self.__getitem__(n)
            idx = np.nonzero(x)
            count = x[idx]
            frame = idx[0] + offset
            index = idx[1].astype(np.int64)
            offset += x.shape[0]

            y = np.zeros_like(count, dtype=np.int64)
            y += frame.astype(np.int64) << 40
            y += index << 16
            y = y + count
            y.tofile(fid, sep="")

        fid.close()

    def sparse_to_dense(self, index, frame, count, size):
        if isinstance(index, np.ndarray):
            # using numpy array; will be sent to device by dataloader
            x = np.zeros((size, self.pixel_num), dtype=self.dtype)
            x[frame, index] = count
        else:
            x = np.zeros((size, self.pixel_num), dtype=self.dtype)
            x[frame, index] = count

        return x
