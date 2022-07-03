from PyQt5.QtWidgets import (
    QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout,
    QSplitter
)
from src.jhs_addform import JHSAddForm
from src.jhs_findform import JHSFindForm
from src.jhs_options import JHSOptions
from src.constants import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal
import os

class JHS(QWidget):

    loggedOut = pyqtSignal()

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
        self.jhsfindform = JHSFindForm()
        self.stackedwidget.addWidget(self.jhsaddform)
        self.stackedwidget.addWidget(self.jhsfindform)
        self.options = JHSOptions(self.parser)
        self.options.logout_btn.clicked.connect(self.logout)
        self.options.add_form_btn.clicked.connect(lambda: self.stackedwidget.setCurrentIndex(0))
        self.options.find_form_btn.clicked.connect(lambda: self.stackedwidget.setCurrentIndex(1))

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.options)
        self.splitter.addWidget(self.stackedwidget)
        self.contentlayout.addWidget(self.splitter)
        self.mainlayout.addLayout(self.contentlayout)
        self.setLayout(self.mainlayout)

    def logout(self):
        self.loggedOut.emit()
        self.close()