from src.jhs import JHS
from src.shs import SHS
from src.login import Login

# # Main Application Widget
class MainApp:

    # Constructor
    def __init__(self, parser):
        self.parser = parser

    # Create and show widget based on the selected form
    def showSelected(self, formselect_index):
        if formselect_index == 0:
            self.jhs = JHS(self.parser)
            self.jhs.loggedOut.connect(self.openLogin)
            self.login.hide()
            self.jhs.showMaximized()
        elif formselect_index == 1:
            self.shs = SHS(self.parser)
            self.shs.showMaximized()

    # Create and show login widget
    def openLogin(self):
        self.login = Login(self.parser)
        self.login.username_input.setText("admin")
        self.login.password_input.setText("passadmin123")
        self.login.success.connect(self.showSelected)
        self.login.show()