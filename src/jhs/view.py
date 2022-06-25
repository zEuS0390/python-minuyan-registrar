from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QStackedWidget
)
from .addform import AddForm

class View(QStackedWidget):

    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        self.setup_UI()

    def setup_UI(self):
        self.addWidget(AddForm())