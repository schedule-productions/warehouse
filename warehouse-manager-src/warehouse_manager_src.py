import wpf

from System.Windows import Application, Window

import os
from os import path
from traceback import format_exc

from System.Windows import *
from System.Windows.Controls import *

app = Application()

import warehouse_manager_metadata

class WindowMain(Window):
    def __init__(self):
        wpf.LoadComponent(self, "warehouse_manager_src.xaml")

        #if path.exists("models"):
        #    self.sModelPath = path.join("models", pathName)
        #else:
        #    self.sModelPath = path.join("..", "models", pathName)

        self.refreshMetadata()
        #self.processRefresh()

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
        self.buttonMetadataCreate.IsEnabled = False

    def popupWindowMetadata(self):
        pathName = self.listMetadata.SelectedItem.ToString()
        newDialog = warehouse_manager_metadata.WindowMetadata(pathName)
        newDialog.ShowDialog()
        self.refreshMetadata()
    
    def buttonMetadataRefresh_Click(self, sender, e):
        self.refreshMetadata()
        #self.processRefresh()

    def _CEPTreeTemplate(self):
        #private DataTemplate GetHeaderTemplate()
        # {
        #    //create the data template
        #    DataTemplate dataTemplate = new DataTemplate();

        #    //create stack pane;
        #    FrameworkElementFactory stackPanel = new FrameworkElementFactory(typeof(StackPanel));
        #    stackPanel.Name = "parentStackpanel";
        #    stackPanel.SetValue(StackPanel.OrientationProperty, Orientation.Horizontal);

        #    // Create check box
        #    FrameworkElementFactory checkBox = new FrameworkElementFactory(typeof(CheckBox));
        #    checkBox.Name = "chk";
        #    checkBox.SetValue(CheckBox.NameProperty, "chk");
        #    checkBox.SetValue(CheckBox.TagProperty , new Binding());
        #    checkBox.SetValue(CheckBox.MarginProperty, new Thickness(2));
        #    stackPanel.AppendChild(checkBox);

        #    // Create Image 
        #    FrameworkElementFactory image = new FrameworkElementFactory(typeof(Image));
        #    image.SetValue(Image.MarginProperty, new Thickness(2));
        #    image.SetBinding(Image.SourceProperty, new Binding() 
        #  { Converter = new CustomImagePathConverter() });
        #    stackPanel.AppendChild(image);

        #    // create text
        #    FrameworkElementFactory label = new FrameworkElementFactory(typeof(TextBlock));
        #    label.SetBinding(TextBlock.TextProperty, new Binding());
        #    label.SetValue(TextBlock.ToolTipProperty, new Binding());          
        #    stackPanel.AppendChild(label);

          
        #    //set the visual tree of the data template
        #    dataTemplate.VisualTree = stackPanel;

        #    return dataTemplate;
        # } 
        pass

if __name__ == '__main__':
    try:
        app.Run(WindowMain())
    except:
        MessageBox.Show(format_exc(),
                        "Fatal Error",
                        MessageBoxButton.OK,
                        MessageBoxImage.Error)
