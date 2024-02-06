# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:59:30 2024

@author: arjun
"""
import sys # System-specific parameters and functions

from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget,QMainWindow,
                             QFileDialog, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox)
import pyqtgraph as pg
import json
import imageio.v2 as io
class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.l = QGridLayout(self)
        self.imv = pg.ImageView()
        self.l.addWidget(self.imv)
        
class DropDown(QComboBox):
    def __init__(self,items):
        super().__init__()
        self.items = items
        self.addItems(self.items)
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.set_default()
        w = QWidget(self)
        self.setCentralWidget(w)
        
        self.main_layout = QVBoxLayout()
        w.setLayout(self.main_layout)
        self.dropdown_box = QVBoxLayout()
        self.language_dd = DropDown(self.available_languages)
        self.language_dd.currentIndexChanged.connect(self.update_language_dd)
        
        self.language_dd.setCurrentIndex(self.index_language)
        self.main_layout.addWidget(self.language_dd)
        self.main_layout.addWidget(self.open_button)
        self.image_viewer = Interface()
        self.main_layout.addWidget(self.image_viewer)
    
    def update_language_dd(self,index):
        self.index_language = index
        self.language = self.available_languages[self.index_language]
        self.setWindowTitle(self.options["available languages"][self.language]["window title"])
        self.open_button.setText(self.open_button["available languages"][self.language]["button"])
        self.set_dropdowns()
    def set_default(self):
        self.status = self.statusBar()
        self.im = None
        with open("settings.json","r") as jsonfile:
            self.options = json.load(jsonfile)
        width  = self.options["defaults"]["width"]
        height = self.options["defaults"]["height"]
        self.resize(width, height)
        
        self.available_languages = list(self.options["available languages"].keys())
        self.language  = self.options["defaults"]["language"]
        self.index_language = self.available_languages.index(self.language)
        self.setWindowTitle(self.options["available languages"][self.language]["window title"])
        
        self.open_button = QPushButton()
        self.open_button.setGeometry(300, 300, 300, 300)
        self.open_button.setText(self.options["available languages"][self.language]["button"])
        
        self.open_button.clicked.connect(self.open)
    def open(self):
        fn,_ = QFileDialog.getOpenFileName(filter="*.jpg *.png")
    #     test_label = QLabel("Test Label")
    #     self.main_layout.addWidget(test_label)
        
    #     self.second_layout = QVBoxLayout()
    #     self.create_buttons(self.second_layout, 5)
    #     self.main_layout.addLayout(self.second_layout)
    # def create_buttons(self,layout,index):
    #     for i in range(index,index+5):
    #         button = QPushButton(f"{i}")
    #         self.second_layout.addWidget(button)
        if fn:
            self.status.showMessage(fn)
            self.im = io.imread(fn)
            self.image_viewer.imv.setImage(self.im)
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)
            message_box.setText("No images selected")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()
        
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()