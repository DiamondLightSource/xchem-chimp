import logging
import warnings

import imageio
import skimage
import torch
import torchvision

import xchem_chimp

with warnings.catch_warnings():
    # Disregard warnings like: DeprecationWarning: Please use `gaussian_filter` from the `scipy.ndimage` namespace, the `scipy.ndimage.filters` namespace is deprecated.
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import albumentations


logger = logging.getLogger(__name__)


# ----------------------------------------------------------
def version():
    """
    Current version.
    """

    return xchem_chimp.__version__


# ----------------------------------------------------------
def meta(given_meta=None):
    """
    Returns version information as a dict.
    Adds version information to given meta, if any.
    """
    s = {}
    s["xchem_chimp"] = version()
    s["imageio"] = imageio.__version__
    s["skimage"] = skimage.__version__
    s["torch"] = torch.__version__
    s["torchvision"] = torchvision.__version__
    s["albumentations"] = albumentations.__version__

    if given_meta is not None:
        given_meta.update(s)
    else:
        given_meta = s
    return given_meta
