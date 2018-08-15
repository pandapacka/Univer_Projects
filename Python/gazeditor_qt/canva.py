__author__ = 'gazik'

from window import *
from queue import *
import sys
class Scene(QtGui.QGraphicsScene):

    """НАЧАЛЬНЫЕ НАСТРОЙКИ ДЛЯ ИНСТРУМЕНТОВ"""

    """~~~КАРАНДАШ~~~"""
    def pencil_color_click(self):
        self.tool.pencil_color = QtGui.QColorDialog.getColor()
        self.pencil_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.pencil_color, QtCore.Qt.SolidPattern))

    def install_pencil(self):
        self.tool.set = self.tool.PENCIL
        self.graphicalview.setMouseTracking(False)

        main.toolbar2.clear()

        self.pencil_settings = QtGui.QGroupBox('Карандаш')
        self.pencil_settings.pencil_color_diag = QtGui.QColorDialog()
        self.pencil_settings.pencil_color_btn = QtGui.QPushButton('color', main)
        self.pencil_settings.pencil_color_btn.clicked.connect(self.pencil_color_click)

        self.pencil_graphicalview = QtGui.QGraphicsView()
        self.pencil_graphicalview.setMaximumHeight(self.tool.common_color_view_height)
        self.pencil_graphicalview.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.pencil_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.pencil_color, QtCore.Qt.SolidPattern))
        self.pencil_graphicalscene = QtGui.QGraphicsScene()
        self.pencil_graphicalscene.setSceneRect(0,0,0,0)
        self.pencil_graphicalview.setScene(self.pencil_graphicalscene)

        self.pencil_settings.pencil_layout = QtGui.QVBoxLayout()
        self.pencil_settings.pencil_layout.addWidget(self.pencil_graphicalview)
        self.pencil_settings.pencil_layout.addWidget(self.pencil_settings.pencil_color_btn)
        self.pencil_settings.setLayout(self.pencil_settings.pencil_layout)

        main.toolbar2.addWidget(self.pencil_settings)


    """~~~КИСТЬ~~~"""
    #Изменение ширины кисти
    def brush_width(self, x):
        self.brush_settings.width = x
        self.brush_settings.slider_label.setText(str(x))

    #Изменение цвета кисти
    def brush_color_click(self):
        self.tool.brush_color = QtGui.QColorDialog.getColor()
        self.brush_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.brush_color, QtCore.Qt.SolidPattern))


    def install_brush(self):
        self.tool.set = self.tool.BRUSH
        self.graphicalview.setMouseTracking(True)
        self.brush_flag = False
        self.saveimage = self.gzPixmap.toImage()

        main.toolbar2.clear()

        self.brush_graphicalview = QtGui.QGraphicsView()
        self.brush_graphicalview.setMaximumHeight(self.tool.common_color_view_height)
        self.brush_graphicalview.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.brush_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.brush_color, QtCore.Qt.SolidPattern))
        self.brush_graphicalscene = QtGui.QGraphicsScene()
        self.brush_graphicalscene.setSceneRect(0,0,0,0)
        self.brush_graphicalview.setScene(self.brush_graphicalscene)

        self.brush_settings = QtGui.QGroupBox('Кисти')
        self.brush_settings.style1 = QtGui.QRadioButton("кисть 1")
        self.brush_settings.style2 = QtGui.QRadioButton("кисть 2")
        self.brush_settings.style3 = QtGui.QRadioButton("кисть 3")

        self.brush_settings.style1.clicked.connect(self.tool.brush_style1_clicked)
        self.brush_settings.style2.clicked.connect(self.tool.brush_style2_clicked)
        self.brush_settings.style3.clicked.connect(self.tool.brush_style3_clicked)

        self.brush_settings.style1.setChecked(True)  # кисть по умолчанию


        self.brush_settings.brush_color_diag = QtGui.QColorDialog()
        self.brush_settings.brush_color_btn = QtGui.QPushButton('color', main)
        self.brush_settings.brush_color_btn.clicked.connect(self.brush_color_click)

        self.brush_settings.width = 5
        self.brush_settings.slider = QtGui.QSlider(1)
        self.brush_settings.slider.setValue(5)

        self.brush_settings.slider_label = QtGui.QLabel('5')

        self.brush_settings.connect(self.brush_settings.slider,
                                    QtCore.SIGNAL('valueChanged(int)'),
                                    self.brush_width)

        self.brush_settings.brush_layout = QtGui.QVBoxLayout()

        self.brush_settings.brush_layout.addWidget(self.brush_settings.style1)
        self.brush_settings.brush_layout.addWidget(self.brush_settings.style2)
        self.brush_settings.brush_layout.addWidget(self.brush_settings.style3)
        self.brush_settings.brush_layout.addWidget(self.brush_graphicalview)
        self.brush_settings.brush_layout.addWidget(self.brush_settings.brush_color_btn)
        self.brush_settings.brush_layout.addWidget(self.brush_settings.slider)
        self.brush_settings.brush_layout.addWidget(self.brush_settings.slider_label)

        self.brush_settings.setLayout(self.brush_settings.brush_layout)

        main.toolbar2.addWidget(self.brush_settings)


    def install_elastic(self):
        self.tool.set = self.tool.ELASTIC
        self.graphicalview.setMouseTracking(True)
        self.elastic_flag = False
        self.saveimage = self.gzPixmap.toImage()

        main.toolbar2.clear()
        self.elastic_settings = QtGui.QGroupBox('Ластик')
        main.toolbar2.addWidget(self.elastic_settings)

    def figure_color_click(self):
        self.tool.figure_color = QtGui.QColorDialog.getColor()
        self.figure_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.figure_color, QtCore.Qt.SolidPattern))

    def install_figure(self):
        self.tool.set = self.tool.FIGURE
        self.graphicalview.setMouseTracking(False)

        main.toolbar2.clear()

        self.figure_settings = QtGui.QGroupBox('Фигуры')

        self.figure_settings.style1 = QtGui.QRadioButton("Прямяуг.")
        self.figure_settings.style2 = QtGui.QRadioButton("Овал")

        self.figure_settings.style1.clicked.connect(self.tool.figure_style1_clicked)
        self.figure_settings.style2.clicked.connect(self.tool.figure_style2_clicked)

        self.figure_settings.style1.setChecked(True)  # кисть по умолчанию


        self.figure_settings.figure_color_diag = QtGui.QColorDialog()
        self.figure_settings.figure_color_btn = QtGui.QPushButton('color', main)
        self.figure_settings.figure_color_btn.clicked.connect(self.figure_color_click)

        self.figure_graphicalview = QtGui.QGraphicsView()
        self.figure_graphicalview.setMaximumHeight(self.tool.common_color_view_height)
        self.figure_graphicalview.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.figure_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.figure_color, QtCore.Qt.SolidPattern))
        self.figure_graphicalscene = QtGui.QGraphicsScene()
        self.figure_graphicalscene.setSceneRect(0,0,0,0)
        self.figure_graphicalview.setScene(self.figure_graphicalscene)

        self.figure_settings.figure_layout = QtGui.QVBoxLayout()
        self.figure_settings.figure_layout.addWidget(self.figure_graphicalview)
        self.figure_settings.figure_layout.addWidget(self.figure_settings.figure_color_btn)
        self.figure_settings.figure_layout.addWidget(self.figure_settings.style1)
        self.figure_settings.figure_layout.addWidget(self.figure_settings.style2)
        self.figure_settings.setLayout(self.figure_settings.figure_layout)

        main.toolbar2.addWidget(self.figure_settings)

    def fill_color_click(self):
        self.tool.fill_color = QtGui.QColorDialog.getColor()
        self.fill_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.fill_color, QtCore.Qt.SolidPattern))

    def install_fill(self):
        self.tool.set = self.tool.FILL
        self.graphicalview.setMouseTracking(False)

        main.toolbar2.clear()

        self.fill_settings = QtGui.QGroupBox('Заливка')
        self.fill_settings.fill_color_diag = QtGui.QColorDialog()
        self.fill_settings.fill_color_btn = QtGui.QPushButton('color', main)
        self.fill_settings.fill_color_btn.clicked.connect(self.fill_color_click)

        self.fill_graphicalview = QtGui.QGraphicsView()
        self.fill_graphicalview.setMaximumHeight(self.tool.common_color_view_height)
        self.fill_graphicalview.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.fill_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.fill_color, QtCore.Qt.SolidPattern))
        self.fill_graphicalscene = QtGui.QGraphicsScene()
        self.fill_graphicalscene.setSceneRect(0,0,0,0)
        self.fill_graphicalview.setScene(self.fill_graphicalscene)

        self.fill_settings.fill_layout = QtGui.QVBoxLayout()
        self.fill_settings.fill_layout.addWidget(self.fill_graphicalview)
        self.fill_settings.fill_layout.addWidget(self.fill_settings.fill_color_btn)
        self.fill_settings.setLayout(self.fill_settings.fill_layout)

        main.toolbar2.addWidget(self.fill_settings)

    def star_color_click(self):
        self.tool.star_color = QtGui.QColorDialog.getColor()
        self.star_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.star_color, QtCore.Qt.SolidPattern))

    def install_star(self):
        self.tool.set = self.tool.STAR
        self.graphicalview.setMouseTracking(False)

        main.toolbar2.clear()

        self.star_settings = QtGui.QGroupBox('Звезда')

        self.star_settings.star_color_diag = QtGui.QColorDialog()
        self.star_settings.star_color_btn = QtGui.QPushButton('color', main)
        self.star_settings.star_color_btn.clicked.connect(self.star_color_click)

        self.star_graphicalview = QtGui.QGraphicsView()
        self.star_graphicalview.setMaximumHeight(self.tool.common_color_view_height)
        self.star_graphicalview.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.star_graphicalview.setBackgroundBrush(QtGui.QBrush(self.tool.star_color, QtCore.Qt.SolidPattern))
        self.star_graphicalscene = QtGui.QGraphicsScene()
        self.star_graphicalscene.setSceneRect(0,0,0,0)
        self.star_graphicalview.setScene(self.star_graphicalscene)

        self.star_settings.star_layout = QtGui.QVBoxLayout()
        self.star_settings.star_layout.addWidget(self.star_graphicalview)
        self.star_settings.star_layout.addWidget(self.star_settings.star_color_btn)

        self.star_settings.setLayout(self.star_settings.star_layout)

        main.toolbar2.addWidget(self.star_settings)

    def install_clone(self):
        self.tool.set = self.tool.CLONE
        self.graphicalview.setMouseTracking(False)

        main.toolbar2.clear()

        self.clone_settings = QtGui.QGroupBox('Выделение')

        self.clone_settings.move = QtGui.QPushButton('Moving', main)
        #self.star_settings.star_color_btn = QtGui.QPushButton('color', main)
        #self.star_settings.star_color_btn = QtGui.QPushButton('color', main)


        self.clone_settings.move.clicked.connect(self.tool.clone_settings_click)
        self.clone_settings.clone_layout = QtGui.QVBoxLayout()

        self.clone_settings.clone_layout.addWidget(self.clone_settings.move)

        self.clone_settings.setLayout(self.clone_settings.clone_layout)

        main.toolbar2.addWidget(self.clone_settings)


    def __init__(self, tool):
        super(Scene, self).__init__()

        self.tool = tool
        self.tool.btn_new.clicked.connect(self.install_new)

        self.backColor = QtGui.QColor(220,220,220)
        self.backBrush = QtGui.QBrush()
        self.backBrush.setColor(self.backColor)

        self.saveimage = QtGui.QImage()
        #Связь кнопок с инструментами
        self.tool.btn_pencil.clicked.connect(self.install_pencil)
        self.tool.btn_brush.clicked.connect(self.install_brush)
        self.tool.btn_elastic.clicked.connect(self.install_elastic)
        self.tool.btn_figure.clicked.connect(self.install_figure)
        self.tool.btn_fill.clicked.connect(self.install_fill)
        self.tool.btn_star.clicked.connect(self.install_star)
        self.tool.btn_clone.clicked.connect(self.install_clone)

        """КАРАНДАШ"""

        #self.gzPencil = QtGui.QPen()
        #self.gzPencil.setColor(self.pencil_color)

        """ФИГУРА"""


    def install_new(self):
        self.tool.width_workspace, ok = QtGui.QInputDialog.getText(self.tool.btn_new,'Input Dialog', 'Enter width of workspace:')
        self.tool.height_workspace, ok2 = QtGui.QInputDialog.getText(self.tool.btn_new,'Input Dialog', 'Enter width of height:')
        if ok:
            if ok2:
                print(self.tool.width_workspace)
                print(self.tool.height_workspace)

                self.setSceneRect(0, 0, int(self.tool.width_workspace), int(self.tool.height_workspace))
                self.graphicalview = QtGui.QGraphicsView()
                self.graphicalview.setRenderHint(QtGui.QPainter.Antialiasing)
                #self.graphicalview.setBaseSize(50, 50)
                print(self.graphicalview.sizeHint())

                self.graphicalview.setScene(self)
                main.setCentralWidget(self.graphicalview)

                self.gzpalette = QtGui.QPalette()
                self.gzpalette.setColor(QtGui.QPalette.Window, self.backColor)
                self.graphicalview.setPalette(self.gzpalette)
                self.graphicalview.setBackgroundBrush(QtGui.QBrush(self.backColor, QtCore.Qt.SolidPattern))

                #Заливка сцены.
                self.gzPixmap = QtGui.QPixmap(QtCore.QSize(self.height(), self.width()))
                self.gzcolor_gzPixmap = QtGui.QColor(255,255,255)
                self.gzPixmap.fill(self.gzcolor_gzPixmap)
                self.addPixmap(self.gzPixmap)

    def mouseMoveEvent(self, event):

        self.end_X = event.lastScenePos().x()
        self.end_Y = event.lastScenePos().y()
        if(self.tool.set == self.tool.PENCIL):
            print('This is PENCIL')

            self.tool.pencil_pen.setColor(self.tool.pencil_color)

            self.gzPainter = QtGui.QPainter()
            self.gzPath = QtGui.QPainterPath()

            self.gzPainter.begin(self.gzPixmap)
            self.gzPainter.setPen(self.tool.pencil_pen)
            self.gzPath.moveTo(self.begin_X, self.begin_Y)
            self.gzPath.lineTo(self.end_X, self.end_Y)
            self.gzPainter.drawPath(self.gzPath)
            self.gzPainter.end()

            self.addPixmap(self.gzPixmap)

            self.begin_X = event.lastScenePos().x()
            self.begin_Y = event.lastScenePos().y()

        if(self.tool.set == self.tool.BRUSH):
            print('This is BRUSH')
            #Подготавливаем кисть
            self.tool.brush_brush.setStyle(self.tool.brush_style)
            self.tool.brush_brush.setColor(self.tool.brush_color)
            self.tool.brush_pen.setBrush(self.tool.brush_brush)
            self.tool.brush_pen.setWidth(self.brush_settings.width)

            self.tool.brush_pen_move.setColor(self.tool.brush_color)

            if (self.brush_flag == False):
                self.gzPixmap.convertFromImage(self.saveimage)
                self.addPixmap(self.gzPixmap)
                self.draw_brush_move()
                self.addPixmap(self.gzPixmap)
            else:
                #Рисуем
                self.draw_brush_click()
                self.addPixmap(self.gzPixmap)
            #запоминаем корды для следующего шага
            self.begin_X = event.lastScenePos().x()
            self.begin_Y = event.lastScenePos().y()

        if(self.tool.set == self.tool.ELASTIC):
            if (self.elastic_flag == False):
                #Ластик около курсора
                self.gzPixmap.convertFromImage(self.saveimage)
                self.addPixmap(self.gzPixmap)
                self.draw_elastic_move()
                self.addPixmap(self.gzPixmap)
            else:
                #Непосредственно сам ластик
                self.gzPixmap.convertFromImage(self.saveimage)
                self.addPixmap(self.gzPixmap)
                self.draw_elastic_click()
                self.addPixmap(self.gzPixmap)
                #Чтобы при нажатии не пропадал ластик с обводкой около мыши
                self.saveimage = self.gzPixmap.toImage()
                self.draw_elastic_move()
                self.addPixmap(self.gzPixmap)

        if (self.tool.set == self.tool.FIGURE):
            print('This is FIGURE')
            raznica_x = self.end_X - self.begin_X
            raznica_y = self.end_Y - self.begin_Y
            self.tool.figure_pen.setColor(self.tool.figure_color)
            if (self.tool.figure_flag == 0):
                self.saveimage = QtGui.QImage()
                self.saveimage = self.gzPixmap.toImage()
                self.tool.figure_flag = 1
            else:
                if(self.tool.figure_style == self.tool.RECT):
                    self.gzPixmap.convertFromImage(self.saveimage)
                    self.addPixmap(self.gzPixmap)
                    self.gzPainter = QtGui.QPainter()
                    self.gzPainter.begin(self.gzPixmap)
                    self.gzPainter.setPen(self.tool.figure_pen)
                    self.gzPainter.drawRect(self.begin_X, self.begin_Y, raznica_x, raznica_y)

                    self.gzPainter.end()
                    self.addPixmap(self.gzPixmap)
                else:
                    print('OVAL')
                    self.gzPixmap.convertFromImage(self.saveimage)
                    self.addPixmap(self.gzPixmap)
                    self.gzPainter = QtGui.QPainter()
                    self.gzPainter.begin(self.gzPixmap)
                    self.gzPainter.setPen(self.tool.figure_pen)
                    self.gzPainter.drawEllipse(self.begin_X, self.begin_Y, raznica_x, raznica_y)

                    self.gzPainter.end()
                    self.addPixmap(self.gzPixmap)



        if(self.tool.set == self.tool.STAR):
            print('This is STAR')

            self.tool.star_pen.setColor(self.tool.star_color)

            self.gzPainter = QtGui.QPainter()
            self.gzPath = QtGui.QPainterPath()

            self.gzPainter.begin(self.gzPixmap)
            self.gzPainter.setPen(self.tool.star_pen)
            self.gzPath.moveTo(self.begin_X, self.begin_Y)
            self.gzPath.lineTo(self.end_X, self.end_Y)
            self.gzPainter.drawPath(self.gzPath)
            self.gzPainter.end()

            self.addPixmap(self.gzPixmap)



        if(self.tool.set == self.tool.CLONE):
            print('This is CLONE')
            #self.piece_pixmap = self.gzPixmap.copy(50,50,100,100)
            #self.testitem = QtGui.QGraphicsPixmapItem(self.piece_pixmap)
            #self.testitem.setPos(40,40)
            #self.testitem=self.addPixmap(self.piece_pixmap)

            #self.testitem.setPos(self.end_X, self.end_Y)
            raznica_x = self.end_X - self.begin_X
            raznica_y = self.end_Y - self.begin_Y
            #if self.tool.clone_move == True

            if (self.tool.clone_flag == 0):
                self.saveimage = QtGui.QImage()
                self.saveimage = self.gzPixmap.toImage()
                self.tool.clone_flag = 1
                print(self.tool.clone_flag)
            elif(self.tool.clone_moving == True and self.tool.clone_proc == True):
                print('loala')
                self.gzPixmap.convertFromImage(self.saveimage)
                #self.addPixmap(self.gzPixmap)

                self.removeItem(self.testitem)
                self.testitem.setPos(self.end_X,self.end_Y)
                self.addItem(self.testitem)
                #self.testitem = self.addPixmap(self.piece_pixmap)
                #self.addPixmap(self.gzPixmap)
            else:
                self.gzPixmap.convertFromImage(self.saveimage)
                self.addPixmap(self.gzPixmap)
                self.gzPainter = QtGui.QPainter()
                self.gzPainter.begin(self.gzPixmap)
                self.gzPainter.setPen(self.tool.clone_pen)
                self.gzPainter.drawRect(self.begin_X, self.begin_Y, raznica_x, raznica_y)
                self.gzPainter.end()
                self.addPixmap(self.gzPixmap)
                print(self.tool.clone_flag)





    def mousePressEvent(self, event):
        self.begin_X = event.lastScenePos().x()
        self.begin_Y = event.lastScenePos().y()

        if(self.tool.set == self.tool.CLONE):
            print('This is Clone')

            #if(self.tool.clone_proc==False):
             #   self.addItem(self.testitem)
                #self.draw_clone_move()
                #self.addPixmap(self.gzPixmap)
                #self.saveimage = self.gzPixmap.toImage()

            self.tool.clone_proc = True
            #self.piece_pixmap = self.gzPixmap.copy(50,50,100,100)
            #self.testitem = QtGui.QGraphicsPixmapItem(self.piece_pixmap)
            #self.testitem.setPos(40,40)

            #self.testitem=self.addPixmap(self.piece_pixmap)

        if(self.tool.set == self.tool.ELASTIC):
            self.elastic_flag = True
            self.draw_elastic_click()
            self.addPixmap(self.gzPixmap)
            self.saveimage = self.gzPixmap.toImage()
            self.draw_elastic_move()
            self.addPixmap(self.gzPixmap)
        if(self.tool.set == self.tool.BRUSH):
            self.brush_flag = True
            self.draw_brush_move()
            self.addPixmap(self.gzPixmap)
            self.saveimage = self.gzPixmap.toImage()

        if(self.tool.set == self.tool.FILL):


            print('This is FILL')
            #Преобразование канвы в картинку для работы.
            self.fill_proc = self.gzPixmap.toImage()
            #Грабим цвет пикселя
            self.fill_pixel = self.fill_proc.pixel(self.begin_X, self.begin_Y)
            #Грабим корды пикселя и загоняем в QPoint
            self.fill_point = QtCore.QPoint(self.begin_X, self.begin_Y)
            #Грабим цвет пикселя в rgb
            self.fill_color = QtGui.QColor(self.fill_pixel).getRgb()
            self.fill_proc.setPixel(self.fill_point, self.tool.fill_color.rgb())
            print(self.tool.fill_color.rgb())
            print(self.fill_pixel)
            import queue
            if (self.fill_pixel != self.tool.fill_color.rgb()):
                q = queue.Queue()
                q.put(self.fill_point)
                max_x = int(self.tool.width_workspace)
                max_y = int(self.tool.height_workspace)
                sps = [-1, 0, 1]
                while(q.empty()==False):
                    now_point = q.get()
                    for i in sps:
                        for j in sps:
                            if(i == 0 or j == 0):
                                if now_point.x() + i in range(0,max_x) and now_point.y() + j in range(0, max_y):
                                    next_point = QtCore.QPoint(now_point.x()+i,now_point.y()+j)
                                    next_point_color = QtGui.QColor(self.fill_proc.pixel(next_point)).getRgb()
                                    if (next_point_color == self.fill_color):
                                        q.put(next_point)
                                        self.fill_proc.setPixel(next_point, self.tool.fill_color.rgb())

                self.gzPixmap = self.gzPixmap.fromImage(self.fill_proc)
                self.addPixmap(self.gzPixmap)

    def mouseReleaseEvent(self, event):

        if(self.tool.set == self.tool.ELASTIC):
            self.elastic_flag = False
            self.gzPixmap.convertFromImage(self.saveimage)
            self.addPixmap(self.gzPixmap)
            self.saveimage = self.gzPixmap.toImage()
            self.draw_elastic_move()
            self.addPixmap(self.gzPixmap)

        if(self.tool.set == self.tool.BRUSH):
            self.saveimage = self.gzPixmap.toImage()
            self.brush_flag = False

        if(self.tool.set == self.tool.CLONE):
            #self.clone_rect = QtCore.QRectF()
            self.tool.clone_proc = False
            self.piece_pixmap = self.gzPixmap.copy(self.begin_X, self.begin_Y, self.end_X - self.begin_X, self.end_Y - self.begin_Y)
            self.testitem = QtGui.QGraphicsPixmapItem(self.piece_pixmap)
            self.saveimage = self.gzPixmap.toImage()
            if (self.tool.clone_moving == True):
                self.gzPainter = QtGui.QPainter(self.gzPixmap)
                self.render(self.gzPainter)
                self.gzPainter.end()
            # self.piece_pixmap = self.gzPixmap.copy(self.begin_X, self.begin_Y, self.end_X - self.begin_X, self.end_Y - self.begin_Y)
            # self.testitem = QtGui.QGraphicsPixmapItem(self.piece_pixmap)
            # self.testitem.setPos(self.begin_X, self.begin_Y)
            #
            # self.testitem=self.addPixmap(self.piece_pixmap)


        self.tool.figure_flag = 0
        self.tool.clone_flag = 0

    def draw_brush_click(self):
        self.gzPainter = QtGui.QPainter()
        self.gzPath = QtGui.QPainterPath()
        self.gzPainter.begin(self.gzPixmap)
        #self.gzPainter.setBrush(self.gzBrush)
        self.gzPainter.setPen(self.tool.brush_pen)
        self.gzPath.moveTo(self.begin_X, self.begin_Y)
        self.gzPath.lineTo(self.end_X, self.end_Y)
        self.gzPainter.drawPath(self.gzPath)
        self.gzPainter.end()
    def draw_brush_move(self):
        self.gzPainter = QtGui.QPainter()
        #self.gzPath = QtGui.QPainterPath()
        self.gzPainter.begin(self.gzPixmap)
        #self.gzPainter.setBrush(self.gzBrush)

        #self.gzPainter.setBrush(self.tool.brush_brush)
        self.gzPainter.setPen(self.tool.brush_pen_move)

        self.gzPainter.setBrush(self.tool.brush_brush)
        #self.gzPainter.setPen(self.tool.elastic_pen_move)
        #self.gzPath.moveTo(self.begin_X, self.begin_Y)
        #self.gzPath.lineTo(self.end_X, self.end_Y)
        x_for_brush = self.end_X - self.brush_settings.width / 2
        y_for_brush = self.end_Y - self.brush_settings.width / 2
        self.gzPainter.drawRect(x_for_brush, y_for_brush, self.brush_settings.width, self.brush_settings.width)
        self.gzPainter.end()

    def draw_elastic_move(self):

        self.gzPainter = QtGui.QPainter()
        self.gzPainter.begin(self.gzPixmap)
        self.gzPainter.setBrush(self.tool.elastic_brush)
        self.gzPainter.setPen(self.tool.elastic_pen_move)
        self.gzPainter.drawRect(self.end_X-5, self.end_Y-5, 10, 10)
        self.gzPainter.end()


    def draw_elastic_click(self):
        self.tool.elastic_rect.setRect(self.end_X-5, self.end_Y-5, 10, 10)
        self.gzPath = QtGui.QPainterPath()
        self.gzPainter = QtGui.QPainter()
        self.gzPainter.begin(self.gzPixmap)
        self.gzPainter.setBrush(self.tool.elastic_brush)
        self.gzPainter.setPen(self.tool.elastic_pen)
        self.gzPath.addRect(self.tool.elastic_rect)
        self.gzPainter.drawPath(self.gzPath)
        self.gzPainter.end()

    #def draw_clone_move(self):


class Canva(QtGui.QGraphicsView):
    def __init__(self, scene):
        super(Canva, self).__init__()