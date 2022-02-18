"""
Source type-dependencies.

Helioviewer JPEG2000 files have stretched images compared to the FITS data.

"""
from astropy.visualization import LinearStretch

__author__ = "Jack Ireland"
__email__ = "jack.ireland@nasa.gov"

__all__ = ['from_helioviewer_project', 'source_stretch']


def from_helioviewer_project(meta):
    """
    Test determining if the MapMeta object contains Helioviewer Project sourced
    data.

    Parameters
    ----------
    meta : `~sunpy.map.MapMeta`

    Returns
    -------
    If the data of the map comes from the Helioviewer Project, then True is
    returned.  If not, False is returned.

    """
    return 'helioviewer' in meta.keys()


def source_stretch(meta, fits_stretch):
    """
    Assign the correct source-dependent image stretching function.

    Parameters
    ----------
    meta : `~sunpy.map.MapMeta`
    fits_stretch : `~astropy.visualization.BaseStretch`
        Image stretching function used when the source image data comes from a
        FITS file.

    Returns
    -------
    An image stretching function appropriate to the image data source.
    """
    return LinearStretch() if from_helioviewer_project(meta) else fits_stretch
