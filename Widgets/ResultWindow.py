from tkinter import Widget
from PySide6.QtWidgets import (QLabel, QFrame, QVBoxLayout, QFormLayout, QTableWidget, QHBoxLayout, QGridLayout, QTableWidgetItem)
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
import requests
from Widgets import RoundShadow

class ResultWindow(RoundShadow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("result")
        self.setFocusPolicy(Qt.NoFocus)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        self.setFixedWidth(390)
        self.table_init()

    def table_init(self):
        self.table = QTableWidget()
        self.table.setFixedWidth(350)
        self.table.setShowGrid(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnWidth(0, 200)
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setShowGrid(False)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
    def generateWord(self, word):
        tableWord = QTableWidgetItem()
        tableWord.setFont(QFont("Microsoft YaHei", 12, QFont.Bold))
        tableWord.setForeground(QColor(0, 0, 0))
        tableWord.setText(word)
        return tableWord

    def generateExplain(self, explain):
        tableExplain = QTableWidgetItem()
        tableExplain.setFont(QFont("Microsoft YaHei", 12, QFont.Normal))
        tableExplain.setForeground(QColor(88, 88, 88))
        tableExplain.setText(explain)
        return tableExplain
        
    def mousePressEvent():
        pass

    def translate(self, text):
        url = "https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q={0}".format(text)
        session = requests.session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Referer': 'https://dict.youdao.com/',

            }

        res = session.get(url, headers=headers).json()["data"]
        if not res:
            res = {"entries":[{"entry":"NoRes", "explain":"NoRes"}]}      
        res = res["entries"]
        word = []
        explain = []
        for i in res:
            word.append(i["entry"])
            explain.append(i["explain"])
        self.generateLabel(word, explain)

        return res

    def generateLabel(self, word = "", explain = ""):
        if word and explain:
            self.table.setRowCount(len(word))
            self.table.setColumnCount(2)
            self.table.setColumnWidth(1, 300)
            self.table.clearContents()
            for i, j, n in zip(word, explain, range(len(word))):
                self.table.setItem(n, 0, self.generateWord(i))
                self.table.setItem(n, 1, self.generateExplain(j))
            layout = QHBoxLayout()  
            layout.addWidget(self.table)  
            self.setLayout(layout)
        