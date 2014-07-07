#!/usr/bin/env python3

import os
import shutil
import configuration

testPath = os.path.join(configuration.cryengineDirectory, "objects", "_warehouse", "_test")

if os.path.exists(configuration.cryengineDirectory):
    if os.path.exists(testPath):
        shutil.rmtree(testPath)
        input("\nCleared test directory from Cryengine game directory!\n")
    else:
        input("\nGame directory already cleared.\n")

else:
    input("\nCryengine directory is wrong!  Change it in 'config.txt'.\n")
