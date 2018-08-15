__author__ = 'gazik'

from window import *

class Tool():


    """КАРАНДАШ"""

    """КИСТЬ"""



    def brush_style1_clicked(self):
        self.brush_style = QtCore.Qt.SolidPattern
        print(self.brush_style)

    def brush_style2_clicked(self):
        self.brush_style = QtCore.Qt.Dense2Pattern
        print(self.brush_style)

    def brush_style3_clicked(self):
        self.brush_style = QtCore.Qt.Dense3Pattern
        print(self.brush_style)

    """ЛАСТИК"""


    """ФИГУРА"""

    def figure_style1_clicked(self):
        self.figure_style = self.RECT
        print(self.figure_style)

    def figure_style2_clicked(self):
        self.figure_style =self.ELLIPSE
        print(self.figure_style)

    """ЗАЛИВКА"""


    """ЗВЕЗДА"""
    def clone_settings_click(self):
        self.clone_moving = True


    def __init__(self):
        self.PENCIL = 0
        self.BRUSH = 1
        self.ELASTIC = 2
        self.FIGURE = 3
        self.FILL = 4
        self.STAR = 5
        self.CLONE = 60

        self.width_workspace = 200
        self.height_workspace = 200

        self.set = self.PENCIL
        main.toolbar = main.addToolBar('toolbasik')
        main.toolbar2 = main.addToolBar('toolbaser')
        #main.toolbar2.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        main.addToolBar(0x4, main.toolbar)
        main.addToolBar(0x1, main.toolbar2)

        self.common_color_view_height = 20

        """***Настройка карандаша***"""
        # self.pencil_settings = QtGui.QGroupBox('Карандаш')
        #
        self.pencil_color = QtGui.QColor(QtCore.Qt.green)
        self.pencil_pen = QtGui.QPen()

        # self.pencil_settings.pencil_color_diag = QtGui.QColorDialog()
        # self.pencil_settings.pencil_color_btn = QtGui.QPushButton('color', main)
        # self.pencil_settings.pencil_color_btn.clicked.connect(self.pencil_color_click)
        #
        # self.pencil_settings.pencil_layout = QtGui.QVBoxLayout()
        # self.pencil_settings.pencil_layout.addWidget(self.pencil_settings.pencil_color_btn)
        # self.pencil_settings.setLayout(self.pencil_settings.pencil_layout)



        """***Настройка кисти***"""

        self.brush_style = QtCore.Qt.BrushStyle(QtCore.Qt.SolidPattern)
        self.brush_color = QtGui.QColor(QtCore.Qt.green)

        self.brush_brush = QtGui.QBrush()
        self.brush_pen = QtGui.QPen()
        self.brush_pen_move = QtGui.QPen()



        #self.brush_rect = QtCore.QRectF()

        """***Настройка ластика***"""
        self.elastic_brush = QtGui.QBrush()
        self.elastic_brush.setColor(QtCore.Qt.white)
        self.elastic_brush.setStyle(QtCore.Qt.SolidPattern)
        self.elastic_pen = QtGui.QPen()
        self.elastic_pen.setColor(QtCore.Qt.white)
        self.elastic_rect = QtCore.QRectF()
        self.elastic_pen_move = QtGui.QPen()
        self.elastic_pen_move.setColor(QtCore.Qt.black)



        """***Настройка фигуры***"""
        self.figure_flag = 0
        self.RECT = 0
        self.ELLIPSE = 1
        self.figure_style = self.RECT
        self.figure_color = QtGui.QColor(QtCore.Qt.green)
        self.figure_pen = QtGui.QPen()
        self.figure_pen.setColor(self.figure_color)
        """~~~Настройка Заливки~~~"""
        self.fill_color = QtGui.QColor(QtCore.Qt.green)

        """***Настройка "звезды"***"""



        """ЗВЕЗДА"""

        self.star_pen = QtGui.QPen()
        self.star_color = QtGui.QColor(QtCore.Qt.green)
        self.star_pen.setColor(self.star_color)


        """***Настройка Выделения***"""
        self.clone_flag = 0
        self.clone_pen = QtGui.QPen()
        self.clone_pen.setColor(QtCore.Qt.black)
        self.clone_proc= True
        self.clone_moving = False
        """~~~Кнопки инструментов (по умолчанию верхний бар)~~~"""

        self.btn_icon_size = 25
        self.btn_new = QtGui.QPushButton(QtGui.QIcon('icons/new.gif'),'', main)
        self.btn_new.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_pencil = QtGui.QPushButton(QtGui.QIcon('icons/pencil.gif'),'', main)
        self.btn_pencil.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_brush = QtGui.QPushButton(QtGui.QIcon('icons/brush.gif'),'', main)
        self.btn_brush.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_elastic = QtGui.QPushButton(QtGui.QIcon('icons/elastic.gif'),'', main)
        self.btn_elastic.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_figure = QtGui.QPushButton(QtGui.QIcon('icons/figure.gif'),'', main)
        self.btn_figure.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_fill = QtGui.QPushButton(QtGui.QIcon('icons/fill.gif'),'', main)
        self.btn_fill.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_star= QtGui.QPushButton(QtGui.QIcon('icons/star.gif'),'', main)
        self.btn_star.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        self.btn_clone= QtGui.QPushButton(QtGui.QIcon('icons/clone.gif'),'', main)
        self.btn_clone.setFixedSize(self.btn_icon_size,self.btn_icon_size)

        main.toolbar.addWidget(self.btn_new)
        main.toolbar.addWidget(self.btn_pencil)
        main.toolbar.addWidget(self.btn_brush)
        main.toolbar.addWidget(self.btn_elastic)
        main.toolbar.addWidget(self.btn_figure)
        main.toolbar.addWidget(self.btn_fill)
        main.toolbar.addWidget(self.btn_star)
        main.toolbar.addWidget(self.btn_clone)

        # main.toolbar2.addWidget(self.pencil_settings)
        # main.toolbar2.addWidget(self.figure_settings)
        # main.toolbar2.addWidget(self.brush_settings)
        # main.toolbar2.addWidget(self.star_settings)