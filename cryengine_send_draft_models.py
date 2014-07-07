#!/usr/bin/env python3

import os
import shutil
import configuration

if os.path.exists(configuration.cryengineDirectory):
    for (dirpath, dirnames, filenames) in os.walk("models"):
        if "mark_for_cryengine_draft.txt" in filenames:
            sendTestModel(os.sep.join(dirpath.split(os.sep)[1:]))

else:
    input("\nCryengine directory is wrong!  Change it in 'configuration.py'.\n")

def sendTestModel(modelPath):
    testPath = os.path.join(configuration.cryengineDirectory, "objects", "_warehouse", "_test")

    if not os.path.exists(testPath):
        os.makedirs(testPath)

    if os.path.exists(os.path.join(testPath, modelPath)):
        shutil.rmtree(os.path.join(testPath, modelPath))

    shutil.copytree(os.path.join("models", modelPath), os.path.join(testPath, modelPath))

    input("\nCopied draft model to Cryengine!\n")
