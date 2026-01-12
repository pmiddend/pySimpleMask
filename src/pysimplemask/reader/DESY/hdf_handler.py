import numpy as np

# required for bloc compression
import hdf5plugin
import h5py
import logging
from .xpcs_dataset import XpcsDataset
from ..utils import sum_frames_parallel

logger = logging.getLogger(__name__)

def _find_data(f):
    # Old Eiger 4M outputs data_00000n
    return "/entry/data/data" if "/entry/data/data" in f else "/entry/data/data_000001"

class HdfDataset(XpcsDataset):
    """
    Parameters
    ----------
    filename: string
    """

    def __init__(
        self,
        *args,
        preload_size=8,
        dtype=np.uint8,
        **kwargs,
    ):
        super().__init__(*args, dtype=dtype, **kwargs)
        self.dataset_type = "HDF5 Dataset"
        self.is_sparse = False
        with h5py.File(self.fname, "r") as f:
            self.dataset_name = _find_data(f)
            data = f[self.dataset_name]
            self.shape = data.shape

            # update data type;
            if data.dtype == np.uint8:
                self.dtype = np.int16
            elif data.dtype == np.uint16:
                # lambda2m's uint16 is actually 12bit. it's safe to to int16
                if self.shape[1] * self.shape[2] == 1813 * 1558:
                    self.dtype = np.int16
                # likely eiger detectors
                else:
                    self.dtype = np.int32
            elif data.dtype == np.uint32:
                self.dtype = np.int32
                logger.warning(
                    "cast uint32 to int32. it may cause "
                    + "overflow when the maximal value >= 2^31"
                )
            else:
                self.dtype = data.dtype

        if "avg_frame" in kwargs and kwargs["avg_frame"] > 1:
            self.dtype = np.float32
        self.fhdl = None
        self.data = None
        self.data_cache = None

        self.update_batch_info(self.shape[0])
        self.update_det_size(self.shape[1:])

        if self.mask_crop is not None:
            self.mask_crop = self.mask_crop.cpu().numpy()

        self.current_group = None
        self.preload_size = preload_size

    def __reset__(self):
        if self.fhdl is not None:
            self.fhdl.close()
            self.data = None
            self.fhdl = None

    def __getbatch__(self, idx):
        """
        return numpy array, which will be converted to tensor with dataloader
        """
        if self.fhdl is None:
            self.fhdl = h5py.File(self.fname, "r", rdcc_nbytes=1024 * 1024 * 256)
            self.data = self.fhdl[self.dataset_name]

        beg, end, size = self.get_raw_index(idx)
        idx_list = np.arange(beg, end, self.stride)

        if self.mask_crop is not None:
            # x = self.data[beg:end, self.sl_v, self.sl_h].reshape(end - beg, -1)
            x = self.data[idx_list].reshape(size, -1)
            x = x[:, self.mask_crop].astype(self.dtype)
            # if idx == 0:
            #     print(np.max(x), x.dtype)
        else:
            x = self.data[idx_list].reshape(-1, self.pixel_num)

        if x.dtype != self.dtype:
            x = x.astype(self.dtype)
        return x

    def get_scattering(self, num_frames=-1, begin_idx=0, num_processes=None):
        return sum_frames_parallel(
            self.fname,
            dataset_name=self.dataset_name,
            start_frame=begin_idx,
            num_frames=num_frames,
            chunk_size=32,
            num_processes=num_processes,
        )
