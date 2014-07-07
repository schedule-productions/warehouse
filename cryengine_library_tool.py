#!/usr/bin/env python3

import os
import shutil

import configuration

def main():
    global gameDirectory
    
    paths = []

    for (dirpath, dirnames, filenames) in os.walk("models"):
        if "mark_for_cryengine.txt" in filenames:
            paths.append(dirpath)

    gameDirectory = configuration.cryengineDirectory

    if os.path.exists(gameDirectory):
        for modelpath in paths:
            copyModel(modelpath)
        input("\nCopied all marked models to the Cryengine game directory!\n")
        
    else:
        input("\nCryengine game directory is incorrect!  Change it in 'configuration.py'.\n")

def checkFiletype(modelpath, extension):
    name = os.path.split(modelpath)[-1]
    return os.path.exists(os.path.join(modelpath, name + "." + extension))

def copyFile(modelpath, extension):
    name = os.path.split(modelpath)[-1]
    shortmodelpath = os.sep.join(modelpath.split(os.sep)[1:])

    copyto = os.path.join(gameDirectory, "objects", "_warehouse", shortmodelpath)
    if not os.path.exists(copyto):
        os.makedirs(copyto)
        
    shutil.copy(os.path.join(modelpath, name + "." + extension), copyto)
    
    print ("Copied '{}' to '{}'".format(
        os.path.join(shortmodelpath, name + "." + extension),
        copyto,
        ))

def copyTexture(modelpath, filename):
    name = os.path.split(modelpath)[-1]
    shortmodelpath = os.sep.join(modelpath.split(os.sep)[1:])

    copyto = os.path.join(gameDirectory, "objects", "_warehouse", shortmodelpath)
    if not os.path.exists(copyto):
        os.makedirs(copyto)

    shutil.copy(os.path.join(modelpath, filename), copyto)
    
    print ("Copied '{}' to '{}'".format(
        os.path.join(shortmodelpath, filename),
        copyto,
        ))

def copyModel(modelpath):
    name = os.path.split(modelpath)[-1]
    filetypes = ["cgf", "mtl"]
    for filetype in filetypes:
        if checkFiletype(modelpath, filetype):
            copyFile(modelpath, filetype)
            
    files = os.listdir(modelpath)
    for file in files:
        if file.endswith(".dds") and file.startswith("texture_"):
            copyTexture(modelpath, file)

    os.remove(os.path.join(modelpath, "mark_for_cryengine.txt"))

if __name__ == "__main__":
    main()
