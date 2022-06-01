import sys, keyboard, time
from telnetlib import STATUS
from pip import main
import pyautogui as pag
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (QWidget, QApplication, QHBoxLayout)
from PySide6 import QtCore
from PySide6.QtCore import Qt, QTimer
from Widgets import CloseButton, ModeButton, lineInput, RoundShadow



class Window(RoundShadow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickSearch")
        self.resize(400, 60)
        x, y = pag.position() #返回鼠标的坐标
        self.move(x, y)
        self.layout()
        self.setProperty("class", "window")

        self.checkTimer = QTimer(self)
        self.checkTimer.start(100)
        self.checkTimer.timeout.connect(self.check)
    
    def check(self):
        if self.closeBtn.status:
            self.show()
        else:
            self.hide()

    def lineInput(self):
        self.input = lineInput()
        self.input.setFixedSize(300, 30)
        self.input.textChanged.connect(self.textdeal)

    def textdeal(self):
        # 0 -- 翻译 1 -- Google
        print(self.input.text())
        if self.modeBtn.status == 0:
            print(self.input.text())
        else:
            print(self.input.text())

    def close_btn(self):
        global closeBtn
        self.closeBtn = closeBtn =  CloseButton(self)
        self.closeBtn.setFixedSize(15, 15)

    def mode_btn(self):
        self.modeBtn = ModeButton()
        self.modeBtn.setFixedSize(25, 25)

    def layout(self):
        self.close_btn()
        self.mode_btn()
        self.lineInput()

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.modeBtn)
        hbox.addStretch(1)
        hbox.addWidget(self.input)
        hbox.addStretch(2)
        hbox.addWidget(self.closeBtn)
        hbox.addStretch(2)
        self.setLayout(hbox)




def main_window():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


import threading
import time

def close_window():
    global closeBtn, status
    status = 0
    closeBtn.status = status

def open_window():
    global closeBtn, status
    status = 1
    closeBtn.status = status


if __name__ == '__main__':
    status = 1
    keyboard.add_hotkey('alt+q', open_window)
    keyboard.add_hotkey('esc', close_window)
    event = threading.Event()
    t1 = threading.Thread(target = main_window)
    t1.start()
    keyboard.wait()

