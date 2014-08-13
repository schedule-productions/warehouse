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
