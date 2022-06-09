from genericpath import exists
import sys, keyboard, time, threading
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout)
from PySide6.QtCore import Qt, QTimer
from Widgets import CloseButton, ModeButton, lineInput, RoundShadow, ResultWindow



class Window(RoundShadow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickSearch")
        self.resize(400, 60)
        x, y = 500, 500
        self.move(x, y)
        self.layout()
        self.resWindowInit()
        self.checkInit()

    def checkInit(self):
        def check():
            if self.closeBtn.status:
                self.show()
                self.input.setFocusPolicy(Qt.StrongFocus)
            else:
                if hasattr(self, "resWindow") and self.resWindow:
                    self.resWindow.hide()

                self.input.clear()
                self.input.setFocusPolicy(Qt.NoFocus)
                self.close()
        self.checkTimer = QTimer(self)
        self.checkTimer.start(100)
        self.checkTimer.timeout.connect(check)


    def resWindowInit(self):
        def follow(pos):
            self.resWindow.move(pos.x() + 5, pos.y() + 43)
        self.resWindow = ResultWindow()
        self.resWindow.move(self.pos().x() + 5, self.pos().y() + 43)
        self.input.textChanged.connect(lambda: self.textdeal(time.time()))
        self.followTimer = QTimer(self)
        self.followTimer.start(1)
        self.followTimer.timeout.connect(lambda: follow(self.pos()))

    def layout(self):
        global closeBtn
        self.closeBtn = closeBtn =  CloseButton(self)
        self.closeBtn.setFixedSize(15, 15)

        self.modeBtn = ModeButton()
        self.modeBtn.setFixedSize(25, 25)

        self.input = lineInput()
        self.input.setFixedSize(300, 30)


        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.modeBtn)
        hbox.addStretch(1)
        hbox.addWidget(self.input)
        hbox.addStretch(2)
        hbox.addWidget(self.closeBtn)
        hbox.addStretch(2)
        self.setLayout(hbox)

    def textdeal(self, new_time):
        # 0 -- 翻译 
        # 1 -- Google
        def deal():
            # self.dealTimer = None
            if self.modeBtn.status == 0:                
                self.resWindow.translate(self.input.text())
                self.resWindow.show()
                self.activateWindow()
            else:
                print(self.input.text())
        if hasattr(self, "dealTimer"):
            self.dealTimer.stop()
        if self.input.text():
            self.dealTimer = QTimer(self)
            self.dealTimer.setSingleShot(True)
            self.dealTimer.start(500)
            self.dealTimer.timeout.connect(deal)
        else:
            self.resWindow.hide()




def main_window():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()

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

