import wpf

from System.Windows import Application, Window

import os
from os import path
from traceback import format_exc

from System.Windows import *

app = Application()

import warehouse_manager_metadata

class WindowMain(Window):
    def __init__(self):
        wpf.LoadComponent(self, "warehouse_manager_src.xaml")

        self.refreshMetadata()

    def refreshMetadata(self):
        self.listMetadata.Items.Clear()
        for (dirpath, dirnames, filenames) in os.walk("../models"):
            hasSubfolders = False
            for dirname in dirnames:
                if dirname[0] != "_":
                    hasSubfolders = True
            if "meta.txt" not in filenames and not hasSubfolders and \
                "__bin__.txt" not in filenames:
                noMetadataPath = os.sep.join(dirpath.split(os.sep)[1:])
                self.listMetadata.Items.Add(noMetadataPath)
    
    def MetadataChecklist_SelectionChanged(self, sender, e):
        self.buttonMetadataCreate.IsEnabled = True
    
    def buttonMetadataCreate_Click(self, sender, e):
        self.popupWindowMetadata()

    def popupWindowMetadata(self):
        pathName = self.listMetadata.SelectedItem.ToString()
        newDialog = warehouse_manager_metadata.WindowMetadata(pathName)
        newDialog.ShowDialog()
        self.refreshMetadata()
    
    def buttonMetadataRefresh_Click(self, sender, e):
        self.refreshMetadata()



if __name__ == '__main__':
    try:
        app.Run(WindowMain())
    except:
        MessageBox.Show(format_exc(),
                        "Fatal Error",
                        MessageBoxButton.OK,
                        MessageBoxImage.Error)

"""
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
"""