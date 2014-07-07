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

    if os.path.exists(os.path.join(testPath, modelPath)):
        retrieveDirectory = os.path.join("models", modelPath, "_retrieved")
        if os.path.exists(retrieveDirectory):
            shutil.rmtree(retrieveDirectory)
        shutil.copytree(os.path.join(testPath, modelPath), retrieveDirectory)
        input("\nRetrieved finished draft model from Cryengine game directory!\n")
    else:
        input("\nNo test model at that location!\n")

else:
    input("\nCryengine directory is wrong!  Change it in 'configuration.py'.\n")
