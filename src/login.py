from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QLabel, QLineEdit,
    QHBoxLayout, QPushButton,
    QComboBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
from configparser import ConfigParser
from src.constants import *
import os

# Login Widget
class Login(QWidget):

    success = pyqtSignal()
    
    # Constructor
    def __init__(self, parser: ConfigParser, parent=None):
        super(Login, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.parser = parser
        self.parser.read(os.path.join(CONFIG_DIR, APP_CONFIG))
        self.setup_UI()

    # Set up user interface of the widget
    def setup_UI(self):
        self.setWindowTitle("Log In")
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.setMinimumSize(self.parser.getint("application", "min_width"),
                            self.parser.getint("application", "min_height"))
        self.mainlayout.setContentsMargins(50, 50, 50, 50)

        font = QFont()
        font.setPointSize(14)

        # Form Selection
        self.formselect_layout = QVBoxLayout()
        self.formselect_label = QLabel("Form:")
        self.formselect_input = QComboBox()
        self.formselect_label.setFont(font)
        self.formselect_input.setFont(font)
        self.formselect_input.addItems(["Junior High School", "Senior High School"])
        self.formselect_layout.addWidget(self.formselect_label)
        self.formselect_layout.addWidget(self.formselect_input)
        self.formselect_layout.addStretch()
        self.mainlayout.addLayout(self.formselect_layout)

        # User name input
        self.username_layout = QVBoxLayout()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_label.setFont(font)
        self.username_input.setFont(font)
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)
        self.username_layout.addStretch()
        self.mainlayout.addLayout(self.username_layout)

        # Password input
        self.password_layout = QVBoxLayout()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_label.setFont(font)
        self.password_input.setFont(font)
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)
        self.password_layout.addStretch()
        self.mainlayout.addLayout(self.password_layout)

        # Login button
        self.login_btn_layout = QHBoxLayout()
        self.login_btn = QPushButton()
        self.login_btn.setFont(font)
        self.login_btn.setText("Log In")
        self.login_btn.clicked.connect(self.authenticate)
        self.login_btn_layout.addWidget(self.login_btn)
        self.mainlayout.addLayout(self.login_btn_layout)

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.success.emit()
        self.close()