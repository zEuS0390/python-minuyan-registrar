from .singleton import Singleton
from configparser import ConfigParser

class Config(metaclass=Singleton):
    parser = ConfigParser()
    def __init__(self):
        self.read()
    def read(self, filename="cfg/app.cfg"):
        self.parser.read(filename)

def toBinary(filename: str):
    with open(filename, "rb") as file:
        binary = file.read()
        file.close()
    return binary