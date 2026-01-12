import logging


logger = logging.getLogger(__name__)


def get_handler(beamline, fname, **kwargs):
    Reader = None
    if beamline == "APS_8IDI":
        from .reader.APS_8IDI.aps_8idi_reader import APS8IDIReader as Reader 
    elif beamline == "APS_9IDD":
        from .reader.APS_9IDD.aps_9idd_reader import APS9IDDReader as Reader
    elif beamline == "DESY_P10":
        from .reader.DESY.file_handler import DESYP10Reader as Reader
    
    if Reader is None:
        logger.error("Unsupported beamline")
        return None
    else:
        return Reader(fname, **kwargs)


if __name__ == "__main__":
    pass
