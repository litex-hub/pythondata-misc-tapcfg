import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/enjoy-digital/tapcfg"
git_hash = "bd557ff00d8fe2473fcf346e36c96d004e94b8ca"
git_describe = "v0.0-375-gbd557ff"
version_str = "0.0.post375"
version_tuple = (0, 0)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post375")
except ImportError:
    pass