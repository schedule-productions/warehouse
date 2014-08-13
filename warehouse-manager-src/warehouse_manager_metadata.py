import wpf

import clr
clr.AddReference("System.Drawing")

from System.Windows import Window
from System import Uri, UriKind
from System.Windows.Media.Imaging import BitmapImage

from System.Windows import *

from os import path
from os import remove
from traceback import format_exc

class WindowMetadata(Window):
    def __init__(self, pathName):
        wpf.LoadComponent(self, "warehouse_manager_metadata.xaml")

        pathName = pathName.ToString()
        
        self.Title = "Edit Metadata - " + pathName
        self.textPathName.Text = pathName

        self.sPathName = pathName
        self.sModelPath = path.join("..", "models", pathName)
        self.sAttributes = {}
        self.sName = self.sPathName.split(path.sep)[-1]

        self.showPreview()
        self.validateCryEngine()

    def showPreview(self):
        filename = None
        for extension in ["jpg", "png"]:
            filename = path.join(self.sModelPath, "preview." + extension)
            if path.exists(filename):
                break

        if filename:
            image = BitmapImage()
            image.BeginInit()
            imageUri = filename
            image.UriSource =  Uri(imageUri, UriKind.RelativeOrAbsolute)
            image.EndInit()
            self.imagePreview.Source = image
        else:
            pass

    def buttonTagAppend_Click(self, sender, e):
        if self.entryNewTag.Text.ToString():
            self.addTag(self.entryNewTag.Text.ToString())
        self.entryNewTag.Text = ""
    def buttonTagRemove_Click(self, sender, e):
        indexOfSelection = self.listTags.SelectedIndex
        self.removeTag()
        if len(self.listTags.Items):
            self.listTags.SelectedIndex = indexOfSelection
        else:
            self.buttonTagRemove.IsEnabled = False

    def entryNewTag_GotFocus(self, sender, e):
        self.buttonTagAppend.IsDefault = True
        self.buttonConfirm.IsDefault = False
    def entryNewTag_TextChanged(self, sender, e):
        if self.entryNewTag.Text:
            self.buttonTagAppend.IsEnabled = True
        else:
            self.buttonTagAppend.IsEnabled = False

    def entryModelName_TextChanged(self, sender, e):
        if self.entryModelName.Text:
            self.buttonConfirm.IsEnabled = True
        else:
            self.buttonConfirm.IsEnabled = False
        self.buttonConfirm.IsDefault = True
        self.buttonTagAppend.IsDefault = False

    def listTags_SelectionChanged(self, sender, e):
        self.buttonTagRemove.IsEnabled = True

    def buttonConfirm_Click(self, sender, e):
        file = None
        try:
            file = open(path.join(self.sModelPath, "meta.txt"), "w")

            modelName = self.entryModelName.Text

            def parsePathBlocks():
                string = ""
                for block in self.sPathName.split(path.sep):
                    string += "%" + block
                return string
            def parseTags():
                string = ""
                for tag in self.listTags.Items:
                    string += "%" + tag
                return string
            def parseAttributes():
                string = ""
                for key in self.sAttributes.keys():
                    value = self.sAttributes[key]
                    string += "%" + key + "#" + str(value)
                return string

            data = [
                "%name%" + modelName + "\n",
                "%dataname%" + self.sName + "\n",
                "%path" + parsePathBlocks() + "\n",
                "%tags" + parseTags() + "\n",
                "%attributes" + parseAttributes() + "\n",
                ]

            file.writelines(data)
            file.close()

            MessageBox.Show("Metadata saving successful!",
                       "Save Successful", MessageBoxButton.OK,
                       MessageBoxImage.Information)

            self.Close()

        except:
            if file != None:
                file.close()
            MessageBox.Show("Metadata saving failed!\n{}".format(format_exc()),
                       "Fatal Error", MessageBoxButton.OK,
                       MessageBoxImage.Error)
            if path.exists(path.join(self.sModelPath, "meta.txt")):
                remove(path.join(self.sModelPath, "meta.txt"))

    def validateCryEngine(self):
        name = self.sName
        cryengineBlenderFile = path.join(self.sModelPath, name+"_cryengine.blend")
        cryengineCompatible = path.exists(cryengineBlenderFile)
        self.sAttributes["cryengine"] = str(cryengineCompatible)
        if cryengineCompatible:
            self.textCryEngine.Text = "This model is CryEngine compatible."

    def addTag(self, newTag):
        if newTag not in self.listTags.Items:
            self.listTags.Items.Add(newTag)
    def removeTag(self):
        self.listTags.Items.Remove(self.listTags.SelectedItem)