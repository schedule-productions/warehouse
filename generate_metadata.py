#!/usr/bin/env python3

from os import path

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

#File format
#------------
#%name%Octocat
#%dataname%octocat
#%path%misc%octocat
#%tags%misc%random%clutter%trophy%figure%toy
#%attributes%cryengine#True

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
