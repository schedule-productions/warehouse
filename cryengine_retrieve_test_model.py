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
        print("\nRetrieved finished draft model from Cryengine game directory!")
        materialFilename = os.path.join(retrieveDirectory, os.path.basename(modelPath) + ".mtl")
        if os.path.exists(materialFilename):
            materialFile = open(materialFilename, "r")
            materialData = materialFile.read()
            materialFile.close()

            materialData = materialData.replace("_warehouse/_test/", "_warehouse/")
            materialFile = open(materialFilename, "w")
            materialFile.write(materialData)
            materialFile.close()

            input(" -> Fixed material texture links.\n")
        else:
            input(" -> Could not retrieve material file to fix.\n")
        
    else:
        input("\nNo test model at that location!\n")

else:
    input("\nCryengine directory is wrong!  Change it in 'configuration.py'.\n")
