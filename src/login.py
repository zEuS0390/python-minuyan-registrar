from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QLabel, QLineEdit,
    QHBoxLayout, QPushButton,
    QComboBox, QFrame,
    QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, pyqtSignal,QRect
from configparser import ConfigParser
from src.constants import *
from db.manager import Manager
import os

# Login Widget
class Login(QWidget):

    success = pyqtSignal(int)
    
    # Constructor
    def __init__(self, parser: ConfigParser, parent=None):
        super(Login, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.parser = parser
        self.db = Manager()
        self.parser.read(os.path.join(CONFIG_DIR, APP_CONFIG))
        self.setup_UI()
        self.setup_style_configurations()

    # Check key press events
    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key.Key_Return:
            self.authenticate()
        elif key_event.key() == Qt.Key.Key_Escape:
            self.close()
        return super().keyPressEvent(key_event)

    # Set up user interface of the widget
    def setup_UI(self):
        self.setWindowIcon(QIcon(":/main.png"))
        self.setWindowTitle("Log In")
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.setMinimumSize(self.parser.getint("application", "min_width"),
                            self.parser.getint("application", "min_height"))
        self.mainlayout.setContentsMargins(50, 50, 50, 50)

        font = QFont()
        font.setPointSize(self.parser.getint("application:login", "font_size"))

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

        self.line = QFrame()
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(320, 150, 118, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.mainlayout.addWidget(self.line)

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
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
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

        self.mainlayout.addStretch()

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()
        response = self.db.user_authenticate(username, password)
        if response == True:
            formselect_index = self.formselect_input.currentIndex()
            self.success.emit(formselect_index)
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Incorrect username or password")
            msg.setWindowTitle("Response")
            msg.exec()

    def setup_style_configurations(self):
        self.setStyleSheet("QWidget {background-color: rgb(255, 246, 222);}")
        self.username_input.setStyleSheet("QLineEdit {background-color: white;}")
        self.password_input.setStyleSheet("QLineEdit {background-color: white;}")
        self.formselect_input.setStyleSheet("QComboBox {background-color: white;}")
        self.login_btn.setStyleSheet("QPushButton {background-color: white;} ")