#!/usr/bin/env python3

from os import path
import os

noMetadataPaths = []
for (dirpath, dirnames, filenames) in os.walk("models"):
    hasSubfolders = False
    for dirname in dirnames:
        if dirname[0] != "_":
            hasSubfolders = True
    if "meta.txt" not in filenames and not hasSubfolders:
        noMetadataPaths.append(os.sep.join(dirpath.split(os.sep)[1:]))

if noMetadataPaths:
    print("\nThe following models have no metadata:")
    for ipath in noMetadataPaths:
        print(ipath)
else:
    print("\nAll models in valid directories have metadata!")

print("---------------------------------------------\n")

name = None
while True:
    print("Model directory path (ex. misc/octocat)")
    dirpath = input(" :: ")

    if "/" in dirpath:
        pathBlocks = dirpath.split("/")
    elif "\\" in dirpath:
        pathBlocks = dirpath.split("\\")
    elif "." in dirpath:
        pathBlocks = dirpath.split(".")
    else:
        pathBlocks = ""

    for block in pathBlocks:
        if not block:
            pathBlocks.remove(block)
    if pathBlocks[0] == "models":
        pathBlocks = pathBlocks[1:]

    name = pathBlocks[-1]

    testpath = "models/" + "/".join(pathBlocks) + "/"+name+".blend"
    if path.exists(testpath):
        break
    else:
        input("\nThere is no valid model at that location.\n")



modelName = input("Model proper name (ex. Octocat)\n :: ")

tags = []

print("Enter search tags by hitting return between tags.  Leave blank to finish.")

newTag = True
while newTag:
    newTag = input(" :: ")
    if newTag and "%" not in newTag:
        tags.append(newTag.lower())

modelPath = "models/" + "/".join(pathBlocks)

cryengine = path.exists(path.join(modelPath, name+"_cryengine.blend"))

attributes = {"cryengine" : str(cryengine)}

def saveMetadata():
    file = open(path.join(modelPath, "meta.txt"), "w")
    
    def parsePathBlocks():
        string = ""
        for block in pathBlocks:
            string += "%" + block
        return string
    def parseTags():
        string = ""
        for tag in tags:
            string += "%" + tag
        return string
    def parseAttributes():
        string = ""
        for key in attributes.keys():
            value = attributes[key]
            string += "%" + key + "#" + str(value)
        return string
    
    data = [
        "%name%" + modelName + "\n",
        "%dataname%" + name + "\n",
        "%path" + parsePathBlocks() + "\n",
        "%tags" + parseTags() + "\n",
        "%attributes" + parseAttributes() + "\n",
        ]

    file.writelines(data)

    input("\nSave successful!\n")
    
    file.close()

if not path.exists(path.join(modelPath, "meta.txt")):
    saveMetadata()
else:
    while True:
        answer = input("Okay to overwrite metadata? (ex. y/n) :: ")
        if answer == 'y':
            saveMetadata()
            break
        elif answer == 'n':
            break
        else:
            input("\nNot a valid answer.\n")
