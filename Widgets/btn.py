# coding:utf-8
from PySide6.QtSvgWidgets import QSvgWidget

class CloseButton(QSvgWidget):
    def __init__(self, w) -> None:
        self.url = r"resource\images\title_bar\open.svg"
        super().__init__(self.url)
        self.w = w
        self.status = 1

    def enterEvent(self, e):
        self.load(r"resource\images\title_bar\close.svg")
        
    def leaveEvent(self, e):
        self.load(r"resource\images\title_bar\open.svg")

    def mousePressEvent(self, e):
        self.status = 0
        self.w.hide()


class ModeButton(QSvgWidget):
    def __init__(self) -> None:
        self.url = [r"resource\images\Mode\translate.svg", r"resource\images\Mode\search.svg"]
        super().__init__(self.url[0])
        self.status = 0
        self.modeChange = 0

    def mouseDoubleClickEvent(self, e):
        self.status = (self.status + 1) % 2
        self.modeChange = 1
        self.load(self.url[self.status])