from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tools.singleton import Singleton
from tools.utils import Config
from db.tables import *

class Manager(metaclass=Singleton):

    JHS = 1
    SHS = 2

    def __init__(self):
        self.cfg = Config()
        self.db_name = self.cfg.parser.get("database", "name")
        self.engine = create_engine("sqlite:///{db_name}.db".format(db_name=self.db_name))
        self.session = Session(self.engine)
