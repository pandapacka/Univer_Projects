__author__ = 'gazik'

from menu import *
#from tools import *
from window import *
from canva import *
from tools import *
import sys
#widget.show()

class Class():
    def __init__(self):
        main.show()
        self.tool = Tool()
        self.scene = Scene(self.tool)
        self.canva = Canva(self.scene)
        self.menu = Menu(self.scene)
c = Class()
sys.exit(app.exec_())