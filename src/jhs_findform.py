from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout
)

class JHSFindForm(QWidget):

    def __init__(self, parent=None):
        super(JHSFindForm, self).__init__(parent)
        self.setup_UI()

    def setup_UI(self):
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)