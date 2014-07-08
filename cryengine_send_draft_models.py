#!/usr/bin/env python3

import os
import shutil
import configuration

def sendTestModel(modelPath):
    testPath = os.path.join(configuration.cryengineDirectory, "objects", "_warehouse", "_test")

    if not os.path.exists(testPath):
        os.makedirs(testPath)

    if os.path.exists(os.path.join(testPath, modelPath)):
        shutil.rmtree(os.path.join(testPath, modelPath))

    shutil.copytree(os.path.join("models", modelPath), os.path.join(testPath, modelPath))

    input("\nCopied draft model '%s' to Cryengine!\n" % modelPath)

once = False
if os.path.exists(configuration.cryengineDirectory):
    for (dirpath, dirnames, filenames) in os.walk("models"):
        if "mark-ce-draft.txt" in filenames:
            once = True
            sendTestModel(os.sep.join(dirpath.split(os.sep)[1:]))

    if not once:
        input("\nNo marks found.  Copy the mark " + \
              "'utilities/mark-ce-draft.txt' to any " + \
              "model folder you wish to test.\n")

else:
    input("\nCryengine directory is wrong!  Change it in 'config.txt'.\n")


