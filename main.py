from PyQt5.QtWidgets import (
    QApplication
)
from configparser import ConfigParser
from src.app import MainApp
from src.constants import *
import os, sys, argparse, rc.resources

# Main entry point of the application
if __name__ == "__main__":
    # Initialize argument parser
    argparser = argparse.ArgumentParser(
        description="This program contains optional arguments for other purposes."
    )
    # Add argument for admin creation
    argparser.add_argument("-ca", "--createadmin", action="store_true", help="Create an admin user.")
    # Parse console arguments
    args = argparser.parse_args()
    if args.createadmin:
        from db.manager import Manager
        from db.tables import *
        username = input("Username: ")
        password = input("Password: ")
        manager = Manager()
        user = User(username=username, password=password, isAdmin=True)
        manager.session.add(user)
        manager.session.commit()
        manager.session.close()
    else:
        confparser = ConfigParser()
        app = QApplication(sys.argv)
        main_app = MainApp(confparser)
        main_app.openLogin()
        sys.exit(app.exec())