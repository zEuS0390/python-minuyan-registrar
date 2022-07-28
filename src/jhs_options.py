from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QPushButton, QGroupBox,
    QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect
from src.constants import *
from configparser import ConfigParser
import os

"""
JHSOptions Class Members
    Functions:
        __init__(self, parser, parent=None)
        setup_UI(self)
        setup_option_btns(self)
"""

class JHSOptions(QWidget):

    def __init__(self, parser: ConfigParser, parent=None):
        super(JHSOptions, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.parser = parser
        self.parser.read(os.path.join(CONFIG_DIR, APP_CONFIG))
        self.setup_UI()

    def setup_UI(self):
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setup_option_btns()

    def setup_option_btns(self):
        formbtnsgroup = QGroupBox("Form Options")
        formbtnslayout = QVBoxLayout()
        formbtnsgroup.setLayout(formbtnslayout)

        self.add_form_btn = QPushButton("New")
        self.find_form_btn = QPushButton("Find")
        self.archive_form_btn = QPushButton("Archives")
        self.settings_btn = QPushButton("Settings")
        self.logout_btn = QPushButton("Log Out")

        font = QFont()
        font.setPointSize(self.parser.getint("application:jhs_options", "font_size"))
        formbtnsgroup.setFont(font)
        self.settings_btn.setFont(font)
        self.logout_btn.setFont(font)

        self.line = QFrame()
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(320, 150, 118, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        formbtnslayout.addWidget(self.add_form_btn)
        formbtnslayout.addWidget(self.find_form_btn)
        formbtnslayout.addWidget(self.archive_form_btn)
        self.mainlayout.addWidget(formbtnsgroup)
        self.mainlayout.addWidget(self.line)
        self.mainlayout.addWidget(self.settings_btn)
        self.mainlayout.addWidget(self.logout_btn)
        self.mainlayout.addStretch()
        