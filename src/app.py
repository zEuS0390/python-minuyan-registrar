from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QTabWidget, QTableWidget
)
from PyQt5.QtGui import QIcon
from src.jhs_addform import JHSAddForm
from src.jhs_options import JHSOptions
from src.constants import *
import os

# Main Application Widget
class MainApp(QWidget):

    # Constructor
    def __init__(self, parser, parent=None):
        super(MainApp, self).__init__(parent)
        self.parser = parser
        self.parser.read(os.path.join(CONFIG_DIR, APP_CONFIG))
        self.setup_UI()

    # Initial configuration of the widget
    def setup_UI(self):
        self.setWindowIcon(QIcon(":/main.png"))
        self.setMinimumSize(self.parser.getint("application", "min_width"), 
                            self.parser.getint("application", "min_height"))
        self.setWindowTitle(self.parser.get("application", "window_title"))
        self.mainlayout = QHBoxLayout()
        self.widget = JHSAddForm()
        self.options = JHSOptions()
        self.mainlayout.addWidget(self.options, 20)
        self.mainlayout.addWidget(self.widget, 60)
        self.setLayout(self.mainlayout)