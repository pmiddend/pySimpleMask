import logging
import os
import h5py
import re

from ..base_reader import FileReader
from .hdf_handler import HdfDataset
from pathlib import Path

logger = logging.getLogger(__file__)


def _read_batchinfo(p: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    with p.open("r") as f:
        for line in f:
            key, value = line.split(": ")
            result[key] = value
    return result


class DESYP10Reader(FileReader):
    def __init__(self, fname) -> None:
        super().__init__(fname)
        self.handler = HdfDataset(fname, batch_size=100)

    def get_scattering(self, **kwargs):
        return self.handler.get_scattering(**kwargs)

    def _get_metadata(self):
        fname_path = Path(self.fname)
        batchinfo_path = (
            fname_path
            .with_name(
                re.sub(r"_data_[0-9]+", "", fname_path.name).replace("_master", "")
            )
            .with_suffix(".batchinfo")
        )
        batchinfo_assocs = _read_batchinfo(batchinfo_path)
        # x0, y0 are beam center
        # rr is sample distance
        keys_in_batchinfo = [
            "energy",
            "ccdx",
            "ccdz",
            "ccdx0",
            "ccdz0",
            "x0",
            "y0",
            "rr",
        ]
        keys_in_h5 = {
            "x_pixel_size": "/entry/instrument/detector/x_pixel_size",
            "y_pixel_size": "/entry/instrument/detector/y_pixel_size"
        }

        # The following is basically a verbatim copy of the APS
        # treatment of metadata, adapted for the two sources P10 uses:
        # batchinfo files and the HDF5 file.
        meta = {}
        with h5py.File(self.fname, "r") as f:
            for key, val in keys_in_h5.items():
                meta[key] = f[val][()]
            meta["data_name"] = os.path.basename(self.fname)

        for k in keys_in_batchinfo:
            meta[k] = float(batchinfo_assocs[k])
        meta["det_dist"] = meta["rr"]
        meta["ccdy"] = meta["ccdz"]
        meta["ccdy0"] = meta["ccdz0"]
        meta.pop("ccdz")
        meta.pop("ccdz0")

        ccdx, ccdx0 = meta["ccdx"], meta["ccdx0"]
        ccdy, ccdy0 = meta["ccdy"], meta["ccdy0"]

        meta["bcx"] = meta["x0"] + (ccdx - ccdx0) / meta["x_pixel_size"]
        meta["bcy"] = meta["y0"] + (ccdy - ccdy0) / meta["y_pixel_size"]
        meta.pop("bcx0", None)
        meta.pop("bcy0", None)
        meta["pix_dim"] = meta["x_pixel_size"]
        meta.pop("x_pixel_size", None)
        meta.pop("y_pixel_size", None)
        return meta
