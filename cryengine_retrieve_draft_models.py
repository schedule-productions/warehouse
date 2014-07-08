#!/usr/bin/env python3

import os
import shutil
import configuration

def retrieveTestModel(modelPath):
    
    testPath = os.path.join(configuration.cryengineDirectory, "objects", "_warehouse", "_test")

    if os.path.exists(os.path.join(testPath, modelPath)):
        retrieveDirectory = os.path.join("models", modelPath, "_retrieved")
        if os.path.exists(retrieveDirectory):
            shutil.rmtree(retrieveDirectory)
        shutil.copytree(os.path.join(testPath, modelPath), retrieveDirectory)
        os.remove(os.path.join(retrieveDirectory, "mark-ce-draft.txt"))
        print("\nRetrieved finished draft model '%s' from Cryengine game directory!" % \
              (modelPath))
        os.remove(os.path.join("models", modelPath, "mark-ce-draft.txt"))
        
        materialFilename = os.path.join(retrieveDirectory, os.path.basename(modelPath) + ".mtl")
        if os.path.exists(materialFilename):
            materialFile = open(materialFilename, "r")
            materialData = materialFile.read()
            materialFile.close()

            materialData = materialData.replace("_warehouse/_test/", "_warehouse/")
            materialFile = open(materialFilename, "w")
            materialFile.write(materialData)
            materialFile.close()

            print(" -> Fixed material texture links.\n")
        else:
            print(" -> Could not retrieve material file to fix.\n")
        
    else:
        input("\nNo test model at that location!\n")



once = False
if os.path.exists(configuration.cryengineDirectory):
    for (dirpath, dirnames, filenames) in os.walk("models"):
        if "mark-ce-draft.txt" in filenames:
            once = True
            retrieveTestModel(os.sep.join(dirpath.split(os.sep)[1:]))

    if not once:
        input("\nNo marks found.  Copy the mark " + \
              "'utilities/mark-ce-draft.txt' to any " + \
              "model folder you wish to retrieve after testing.\n")
    else:
        input("\nAll marked models retrieved!\n")

else:
    input("\nCryengine directory is wrong!  Change it in 'config.txt'.\n")

