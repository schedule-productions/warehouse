import wpf

from System.Windows import Application, Window

import os
from os import path

app = Application()

class WindowMain(Window):
    def __init__(self):
        wpf.LoadComponent(self, "warehouse_manager_src.xaml")

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
        newDialog = WindowMetadata(pathName)
        newDialog.ShowDialog()

class WindowMetadata(Window):
    def __init__(self, pathName):
        wpf.LoadComponent(self, "metadata.xaml")

        pathName = pathName.ToString()
        
        self.Title = "Edit Metadata - " + pathName
        self.textPathName.Text = pathName

        self.sPathName = pathName

        file = open("test.txt", "w")
        file.write(self.sPathName)
        file.close()

if __name__ == '__main__':
    app.Run(WindowMain())

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