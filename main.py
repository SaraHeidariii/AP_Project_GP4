import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("main.ui", self)
        self.Boards = [
            self.board_1,
            self.board_2,
            self.board_3,
            self.board_4,
            self.board_5,
            self.board_6,
            self.board_7,
            self.board_8,
            self.board_9,
            self.board_10,
            self.board_11,
            self.board_12,
        ]
        self.Results = [
            self.Res1,
            self.Res2,
            self.Res3,
            self.Res4,
            self.Res5,
            self.Res6,
            self.Res7,
            self.Res8,
            self.Res9,
            self.Res10,
            self.Res11,
            self.Res12,
        ]

        self.hide_object(self.Boards)
        self.hide_object(self.Results)
        self.board.hide()
        self.color_btn.hide()
        self.goal.hide()
        self.cover.hide()
        self.confirmbtn.hide()
        self.resetbtn.hide()

        self.startbtn.clicked.connect(self.start)
        self.resetbtn.clicked.connect(self.restart)
        self.hex_color = {
            "red": "#ff0000",
            "blue": "#00007f",
            "green": "#005500",
            "white": "#ffffff",
            "pink": "#fcaf95",
            "orange": "#ffaa00",
            "yellow": "#ffff00",
            "purple": "#800080",
        }
        self.goal_color = [self.goal1, self.goal2, self.goal3, self.goal4, self.goal5]
        self.color_index = 0
        self.mycolor = [
            self.my_color1,
            self.my_color2,
            self.my_color3,
            self.my_color4,
            self.my_color5,
        ]

        self.red.clicked.connect(lambda: self.set_color("red"))
        self.orange.clicked.connect(lambda: self.set_color("orange"))
        self.blue.clicked.connect(lambda: self.set_color("blue"))
        self.purple.clicked.connect(lambda: self.set_color("purple"))
        self.pink.clicked.connect(lambda: self.set_color("pink"))
        self.white.clicked.connect(lambda: self.set_color("white"))
        self.yellow.clicked.connect(lambda: self.set_color("yellow"))
        self.green.clicked.connect(lambda: self.set_color("green"))

        self.board1 = [
            self.color11,
            self.color12,
            self.color13,
            self.color14,
            self.color15,
        ]
        self.board2 = [
            self.color21,
            self.color22,
            self.color23,
            self.color24,
            self.color25,
        ]
        self.board3 = [
            self.color31,
            self.color32,
            self.color33,
            self.color34,
            self.color35,
        ]
        self.board4 = [
            self.color41,
            self.color42,
            self.color43,
            self.color44,
            self.color45,
        ]
        self.board5 = [
            self.color51,
            self.color52,
            self.color53,
            self.color54,
            self.color55,
        ]
        self.board6 = [
            self.color61,
            self.color62,
            self.color63,
            self.color64,
            self.color65,
        ]
        self.board7 = [
            self.color71,
            self.color72,
            self.color73,
            self.color74,
            self.color75,
        ]
        self.board8 = [
            self.color81,
            self.color82,
            self.color83,
            self.color84,
            self.color85,
        ]
        self.board9 = [
            self.color91,
            self.color92,
            self.color93,
            self.color94,
            self.color95,
        ]
        self.board10 = [
            self.color101,
            self.color102,
            self.color103,
            self.color104,
            self.color105,
        ]
        self.board11 = [
            self.color111,
            self.color112,
            self.color113,
            self.color114,
            self.color115,
        ]
        self.board12 = [
            self.color121,
            self.color122,
            self.color123,
            self.color124,
            self.color125,
        ]
        self.color_boards = [
            self.board1,
            self.board2,
            self.board3,
            self.board4,
            self.board5,
            self.board6,
            self.board7,
            self.board8,
            self.board9,
            self.board10,
            self.board11,
            self.board12,
        ]
        self.color_board_index = 0

        self.res1 = [self.res11, self.res12, self.res13, self.res14, self.res15]
        self.res2 = [self.res21, self.res22, self.res23, self.res24, self.res25]
        self.res3 = [self.res31, self.res32, self.res33, self.res34, self.res35]
        self.res4 = [self.res41, self.res42, self.res43, self.res44, self.res45]
        self.res5 = [self.res51, self.res52, self.res53, self.res54, self.res55]
        self.res6 = [self.res61, self.res62, self.res63, self.res64, self.res65]
        self.res7 = [self.res71, self.res72, self.res73, self.res74, self.res75]
        self.res8 = [self.res81, self.res82, self.res83, self.res84, self.res85]
        self.res9 = [self.res91, self.res92, self.res93, self.res94, self.res95]
        self.res10 = [self.res101, self.res102, self.res103, self.res104, self.res105]
        self.res11 = [self.res111, self.res112, self.res113, self.res114, self.res115]
        self.res12 = [self.res121, self.res122, self.res123, self.res124, self.res125]
        self.res_boards = [
            self.res1,
            self.res2,
            self.res3,
            self.res4,
            self.res5,
            self.res6,
            self.res7,
            self.res8,
            self.res9,
            self.res10,
            self.res11,
            self.res12,
        ]

        self.this_step_color = []
        self.confirmbtn.clicked.connect(self.confirm)
        self.win_board.hide()
        self.lose_board.hide()

    def hide_object(self, objects):
        for obj in objects:
            obj.hide()

    def start(self):
        self.this_step_color = []
        self.win_board.hide()
        self.lose_board.hide()
        for i in range(5):
            self.mycolor[i].setStyleSheet(f"background-color: #9e9e9e;")
        self.color_board_index = 0
        self.confirmbtn.show()
        self.board.show()
        self.color_btn.show()
        # self.cover.show()  fln bara check krdne rangaye entekhabie comp
        self.goal.show()
        self.resetbtn.show()

        self.hide_object(self.Boards)
        self.hide_object(self.Results)

        colors = ["red", "blue", "green", "white", "pink", "orange", "yellow", "purple"]

        self.Goal = []
        num = 7
        for i in range(5):
            index = random.randint(0, num)
            self.goal_color[i].setStyleSheet(
                f"background-color: {self.hex_color[colors[index]]};"
            )
            self.Goal.append(colors[index])
            colors.pop(index)
            num = num - 1
        self.goal.show()

    def restart(self):
        self.this_step_color = []
        self.win_board.hide()
        self.lose_board.hide()
        for i in range(5):
            self.mycolor[i].setStyleSheet(f"background-color: #9e9e9e;")
        self.color_index = 0

    def set_color(self, color):
        if color not in self.this_step_color:
            self.my_color[self.color_index].setStylesheet(
                f"background-color: {self.hex_color[color]};"
            )
            if len(self.this_step_color) == 5:
                self.this_step_color[self.color_index] = color
            else:
                self.this_step_color.append(color)
            self.color_index += 1
            if self.color_index == 5:
                self.color_index = 0

    def confirm(self):
        if len(self.this_step_color) == 5:
            self.black = 0
            self.white = 0
            self.this_res = 0
            for i in range(5):
                self.color_boards[self.color_board_index][i].setStylesheet(
                    f"background-color: {self.this_step_color[i]};"
                )
            for j in range(5):
                if self.this_step_color[j] in self.Goal:
                    if self.Goal.index(self.this_step_color[j]) == j:
                        self.black += 1
                    else:
                        self.white += 1
            for n in range(self.black):
                self.res_boards[self.color_board_index][self.this_res].setStyleSheet(
                    f"background-color: #000000;"
                )
                self.this_res += 1
                for m in range(self.white):
                    self.res_boards[self.color_board_index][
                        self.this_res
                    ].setStyleSheet(f"background-color: #ffffff;")
                    self.this_res += 1
                for t in range(5 - self.black - self.white):
                    self.res_boards[self.color_board_index][-1 * (t + 1)].hide()
                self.Boards[self.color_board_index].show()
                self.Results[self.color_board_index].show()
                self.this_step_color = []
                self.color_board_index += 1
                for i in range(5):
                    self.mycolor[i].setStyleSheet(f"background-color: #9e9e9e;")
                if self.black == 5:
                    self.win_board.show()
                    self.cover.hide()
                    self.resetbtn.hide()
                if self.color_board_index == 12:
                    self.lose_board.show()
                    self.cover.hide()
                    self.resetbtn.hide()


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = Mainwindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(1000)
widget.setFixedWidth(800)
widget.show()
app.exec_()
