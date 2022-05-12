
import sys
import requests
import re
import pyperclip

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from fact_ui import Ui_MainWindow


class App(QMainWindow):
    def __init__(self: classmethod):
        super(App, self).__init__()
        self.app = Ui_MainWindow()
        self.app.setupUi(self)
        self.setWindowTitle('Парсер фактов')
        self.app.lbl_text.setText(self.parse_new_fact())
        self.preloaded_fact = self.parse_new_fact()
        self.app.btn_more.clicked.connect(self.get_new_fact)
        self.app.btn_copy.clicked.connect(self.copy_fact)
        self.get_new_fact()

    def copy_fact(self: classmethod):
        pyperclip.copy(self.now_fact)

    def change_fact_font(self: classmethod, font_size: int):
        font = QtGui.QFont()
        font.setPointSize(font_size)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.app.lbl_text.setFont(font)

    def parse_new_fact(self: classmethod) -> str:
        return re.findall(r'<td>[^<]*</td>', requests.get('https://randstuff.ru/fact/').text)[0][4:-5]

    def get_new_fact(self: classmethod):
        self.font_size = 26 if len(self.preloaded_fact) < 100 else 18
        self.change_fact_font(self.font_size)
        self.now_fact = self.preloaded_fact
        self.app.lbl_text.setText(self.now_fact)
        self.preloaded_fact = self.parse_new_fact()


if __name__ == '__main__':
    brun = QtWidgets.QApplication([])
    app = App()
    app.show()
    sys.exit(brun.exec())
