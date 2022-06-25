from db.tables import base
from db.manager import Manager
from test import *
import os, sys

if __name__ == "__main__":
    try:
        os.remove("registrar.db")
    except FileNotFoundError:
        pass
    manager = Manager()
    base.metadata.create_all(manager.engine)