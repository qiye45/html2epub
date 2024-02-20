# coding:utf-8
import html
from telnetlib import Telnet
from datetime import datetime
from multiprocessing.pool import ThreadPool
from re import sub,compile
import requests
from bs4 import BeautifulSoup
from pypandoc import convert_file
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
from inscriptis import get_text
from requests.adapters import HTTPAdapter, Retry
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_untitled import Ui_MainWindow
from PIL import Image
from collections import defaultdict
import resource

class Mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Mywindow()
    # apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True)
    mywindow.show()
    sys.exit(app.exec_())

