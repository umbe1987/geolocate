# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_addressFile_clicked(self):
        """
        Public slot invoked when the user clicks the File Button .
        """
        
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './addresses')
        
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.addressBox.setText(data) 
