import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import random


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        loadUi("main.ui",self)
        self.Boards = [self.board_1,self.board_2,self.board_3,self.board_4,self.board_5,self.board_6,self.board_7,self.board_8,self.board_9,self.board_10,self.board_11,self.board_12]
        self.Results = [self.Res1,self.Res2,self.Res3,self.Res4,self.Res5,self.Res6,self.Res7,self.Res8,self.Res9,self.Res10,self.Res11,self.Res12]
        
        self.hide_object(self.Boards)
        self.hide_object(self.Results)
        self.board.hide()
        self.color_btn.hide()
        self.goal.hide()
        self.cover.hide()
        self.confirmbtn.hide()
        
        self.startbtn.clicked.connect(self.start)
        self.hex_color = {"red" : "#ff0000" , "blue" : "#00007f" , "green" : "#005500" , "white" : "#ffffff" , "pink" : "#fcaf95" , "orange" : "#ffaa00" , "yellow" : "#ffff00" , "purple" : "#800080"}
        self.goal_color = [self.goal1,self.goal2,self.goal3,self.goal4,self.goal5]
        self.color_index = 0
        self.mycolor = [self.my_color1,self.my_color2,self.my_color3,self.my_color4,self.my_color5]
        
        self.red.clicked.connect(lambda: self.set_color("red"))
        self.orange.clicked.connect(lambda: self.set_color("orange"))
        self.blue.clicked.connect(lambda: self.set_color("blue"))
        self.purple.clicked.connect(lambda: self.set_color("purple"))
        self.pink.clicked.connect(lambda: self.set_color("pink"))
        self.white.clicked.connect(lambda: self.set_color("white"))
        self.yellow.clicked.connect(lambda: self.set_color("yellow"))
        self.green.clicked.connect(lambda: self.set_color("green"))

    def hide_object(self, objects):
        for obj in objects:
            obj.hide()

    def start(self):
        self.confirmbtn.show()
        self.board.show()
        self.color_btn.show()
        # self.cover.show()  fln bara check krdne rangaye entekhabie comp
        self.goal.show()
        
        self.hide_object(self.Boards)
        self.hide_object(self.Results)
        
        colors = ["red" , "blue" , "green" , "white" , "pink" , "orange" , "yellow" , "purple"]
        self.Goal = []
        num = 7
        for i in range(5):
            index = random.randint(0,num)
            self.goal_color[i].setStyleSheet(f"background-color: {self.hex_color[colors[index]]};")
            self.Goal.append(colors[index])
            colors.pop(index)
            num = num - 1
        self.goal.show()

    def set_color(self,color):
        self.mycolor[self.color_index].setStyleSheet(f"background-color: {self.hex_color[color]};")
        self.color_index += 1
        if self.color_index == 5:
            self.color_index = 0

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = Mainwindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(1000)
widget.setFixedWidth(800)
widget.show()
app.exec_()