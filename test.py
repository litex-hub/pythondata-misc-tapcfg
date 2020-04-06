#!/usr/bin/env python3
import os

from litex.data.misc import tapcfg

print("Found tapcfg @ version", tapcfg.version_str, "(with data", tapcfg.data_version_str, ")")
print()
print("Data is in", tapcfg.data_location)
assert os.path.exists(tapcfg.data_location)
print("Data is version", tapcfg.data_version_str, tapcfg.data_git_hash)
print("-"*75)
print(tapcfg.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(tapcfg.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), tapcfg.data_location)
        print(" -", path)
