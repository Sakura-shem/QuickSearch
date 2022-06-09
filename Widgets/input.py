from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

class lineInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QLineEdit{border:none;background:transparent;font-size:14px;font-family:Microsoft YaHei;font-weight:bold;}")
        self.setPlaceholderText("QuickSearch")
        self.setFocusPolicy(Qt.StrongFocus)

    def enterEvent(self, event):
        # self.selectAll()
        super().enterEvent(event)
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()
    
    