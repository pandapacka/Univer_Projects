__author__ = 'gazik'

from window import *
from canva import *
from PyQt4 import QtGui, QtCore

class Menu():
    def file_save(self):
        self.filename = QtGui.QFileDialog.getSaveFileName(main, "save file","img","Images (*.png *.bmp *.jpg)")
        self.scene.gzPainter = QtGui.QPainter(self.scene.gzPixmap)
        self.scene.render(self.scene.gzPainter)
        self.scene.gzPixmap.save(self.filename)
        self.scene.gzPainter.end()
        print('file_new')

    def __init__(self, scene):
        main.statusBar()
        menubar = main.menuBar()
        self.scene = scene

        """***FILE***"""
        self.menu_file_exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', main)
        self.menu_file_exit.setShortcut('Ctrl+Q')
        self.menu_file_exit.setStatusTip('Покончить с этим!')

        self.menu_file_save = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Save', main)
        self.menu_file_save.setShortcut('Ctrl+S')
        self.menu_file_save.setStatusTip('Cохраниться!!')


        main.connect(self.menu_file_exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        main.connect(self.menu_file_save, QtCore.SIGNAL('triggered()'), self.file_save)

        self.menu_file = menubar.addMenu('&File')
        self.menu_file.addAction(self.menu_file_exit)
        self.menu_file.addAction(self.menu_file_save)

        """***ABOUT***"""
        self.menu_about_author = QtGui.QAction(QtGui.QIcon('icons/menu_author.gif'), 'Author', main)
        self.menu_about_author.setStatusTip('Кто за всем этим стоит?')

        menu_about = menubar.addMenu('&About')
        menu_about.addAction(self.menu_about_author)