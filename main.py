from PyQt5.QtWidgets import (
    QApplication
)
from configparser import ConfigParser
from src.app import MainApp
from src.login import Login
from src.constants import *
import os, sys

# Main entry point of the application
if __name__ == "__main__":
    parser = ConfigParser()
    app = QApplication(sys.argv)
    main_app = MainApp(parser)
    login = Login(parser)
    login.success.connect(main_app.show)
    login.show()
    sys.exit(app.exec())