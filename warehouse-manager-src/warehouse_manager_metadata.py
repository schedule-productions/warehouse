import wpf

import clr
clr.AddReference("System.Drawing")

from System.Windows import Window
from System import Uri, UriKind
from System.Windows.Media.Imaging import BitmapImage

from System.Drawing import Image

from os import path

class WindowMetadata(Window):
    def __init__(self, pathName):
        wpf.LoadComponent(self, "warehouse_manager_metadata.xaml")

        pathName = pathName.ToString()
        
        self.Title = "Edit Metadata - " + pathName
        self.textPathName.Text = pathName

        self.sPathName = pathName

        self.showPreview()

    def showPreview(self):
        filename = None
        for extension in ["jpg", "png"]:
            filename = path.join("..", "models", "{}", "preview.{}").format(self.sPathName, extension)
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



    def addTag(self, newTag):
        self.listTags.Items.Add(newTag)
    def removeTag(self):
        self.listTags.Items.Remove(self.listTags.SelectedItem.ToString())