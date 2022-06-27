from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class SHS(QWidget):

    def __init__(self, parser, parent=None):
        super(SHS, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.parser = parser
        self.setup_UI()

    def setup_UI(self):
        self.setWindowIcon(QIcon(":/main.png"))
        self.setMinimumSize(self.parser.getint("application", "min_width"), 
                            self.parser.getint("application", "min_height"))
        self.setWindowTitle(self.parser.get("application", "window_title"))
        self.mainlayout = QHBoxLayout()
        self.setLayout(self.mainlayout)
