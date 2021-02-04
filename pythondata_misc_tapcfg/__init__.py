import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/enjoy-digital/tapcfg"

# Module version
version_str = "0.0.post463"
version_tuple = (0, 0, 463)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post463")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post375"
data_version_tuple = (0, 0, 375)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post375")
except ImportError:
    pass
data_git_hash = "bd557ff00d8fe2473fcf346e36c96d004e94b8ca"
data_git_describe = "v0.0-375-gbd557ff"
data_git_msg = """\
commit bd557ff00d8fe2473fcf346e36c96d004e94b8ca
Merge: 4ce399d 1a2accc
Author: enjoy-digital <florent@enjoy-digital.fr>
Date:   Wed May 1 12:11:43 2019 +0200

    Merge pull request #1 from gsomlo/gls-strncpy-werror
    
    fix strncpy string truncation warning/error

"""

# Tool version info
tool_version_str = "0.0.post88"
tool_version_tuple = (0, 0, 88)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post88")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_tapcfg."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_tapcfg".format(f))
    return fn
