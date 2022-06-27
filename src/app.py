from src.jhs import JHS
from src.shs import SHS

# # Main Application Widget
class MainApp:

    # Constructor
    def __init__(self, parser):
        self.parser = parser

    def showSelected(self, formselect_index):
        if formselect_index == 0:
            self.jhs = JHS(self.parser)
            self.jhs.show()
        elif formselect_index == 1:
            self.shs = SHS(self.parser)
            self.shs.show()