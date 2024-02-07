from ._version import version_info, __version__  # noqa: F401 imported but unused


def get_include(user=False):
    return '/usr/include/pybind11'
