#!/usr/bin/env python3
import os

from litex.data.misc import tapcfg

print("Found tapcfg @ version", tapcfg.version_str, "("+tapcfg.git_hash+")")
print("Data is in", tapcfg.data_location)
assert os.path.exists(tapcfg.data_location)
print("It contains:\n -", end=" ")
print("\n - ".join(os.listdir(tapcfg.data_location)))