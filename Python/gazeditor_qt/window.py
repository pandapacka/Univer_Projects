__author__ = 'gazik'

import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        """

        :rtype : object
        """
        QtGui.QMainWindow.__init__(self)
        self.resize(700, 500)
        self.setWindowTitle('menubar')

main = MainWindow()