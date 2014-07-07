#!/usr/bin/env python3

import os
import shutil
import configuration

if os.path.exists(configuration.cryengineDirectory):
    while True:
        modelPath = input("Model path (ex. misc/octocat)\n :: ")
        if os.path.exists(os.path.join("models", modelPath)):
            break
        else:
            input("\nThere is no valid model at that location.\n")

    testPath = os.path.join(configuration.cryengineDirectory, "objects", "_warehouse", "_test")

    if not os.path.exists(testPath):
        os.makedirs(testPath)

    if os.path.exists(os.path.join(testPath, modelPath)):
        shutil.rmtree(os.path.join(testPath, modelPath))

    shutil.copytree(os.path.join("models", modelPath), os.path.join(testPath, modelPath))

    input("\nCopied draft model to Cryengine!\n")

else:
    input("\nCryengine directory is wrong!  Change it in 'configuration.py'.\n")
