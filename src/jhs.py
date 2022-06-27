from PyQt5.QtWidgets import (
    QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout
)
from src.jhs_addform import JHSAddForm
from src.jhs_options import JHSOptions
from src.constants import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

class JHS(QWidget):

    def __init__(self, parser, parent=None):
        super(JHS, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.parser = parser
        self.parser.read(os.path.join(CONFIG_DIR, APP_CONFIG))
        self.setup_UI()

    def setup_UI(self):
        self.setWindowIcon(QIcon(":/main.png"))
        self.setMinimumSize(self.parser.getint("application", "min_width"), 
                            self.parser.getint("application", "min_height"))
        self.setWindowTitle(self.parser.get("application", "window_title"))
        self.mainlayout = QVBoxLayout()
        self.contentlayout = QHBoxLayout()
        self.stackedwidget = QStackedWidget()
        self.jhsaddform = JHSAddForm()
        self.stackedwidget.addWidget(self.jhsaddform)
        self.options = JHSOptions()
        self.contentlayout.addWidget(self.options, 20)
        self.contentlayout.addWidget(self.stackedwidget, 60)
        self.mainlayout.addLayout(self.contentlayout)
        self.setLayout(self.mainlayout)