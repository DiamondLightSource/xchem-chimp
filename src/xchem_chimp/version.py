import logging

import xchem_chimp

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

    s.update(dls_utilpack.version.meta())

    if given_meta is not None:
        given_meta.update(s)
    else:
        given_meta = s
    return given_meta
