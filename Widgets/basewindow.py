from win32.lib import win32con
from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt, QRectF
from win32.win32api import SendMessage
from win32.win32gui import ReleaseCapture
from PySide6.QtGui import QPainter, QColor, QBrush, QPainterPath

class RoundShadow(QFrame):
    """圆角边框毛玻璃类"""

    BORDER_WIDTH = 5
    def __init__(self, parent=None):
        super(RoundShadow, self).__init__(parent)
        self.resize(400, 52)
        self.border_width = 8
        # 设置 窗口无边框和背景透明 *必须
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.SplashScreen | Qt.WindowStaysOnTopHint)

        # frosted glass effect or set opacity

    def paintEvent(self, event):
    	# 阴影
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)

        pat = QPainter(self)
        pat.setRenderHint(pat.Antialiasing)
        pat.fillPath(path, QBrush(Qt.white))

        color = QColor(192, 192, 192, 50)
        for i in range(10):
            i_path = QPainterPath()
            i_path.setFillRule(Qt.WindingFill)
            ref = QRectF(10-i, 10-i, self.width()-(10-i)*2, self.height()-(10-i)*2)
            # i_path.addRect(ref)
            i_path.addRoundedRect(ref, 8, 8)
            color.setAlpha(150 - i**0.5*50)
            pat.setPen(color)
            pat.drawPath(i_path)

        # 圆角
        pat2 = QPainter(self)
        pat2.setRenderHint(pat2.Antialiasing)  # 抗锯齿
        pat2.setBrush(Qt.white)
        pat2.setPen(Qt.transparent)

        rect = self.rect()
        rect.setLeft(9)
        rect.setTop(9)
        rect.setWidth(rect.width()-9)
        rect.setHeight(rect.height()-9)
        pat2.drawRoundedRect(rect, 15, 15)

    def mousePressEvent(self, event):
        """ Move the window """
        ReleaseCapture()
        SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,
                    win32con.SC_MOVE + win32con.HTCAPTION, 0)
        event.ignore()