from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QPushButton, QGroupBox
)
from PyQt5.QtCore import Qt

class JHSOptions(QWidget):

    def __init__(self, parent=None):
        super(JHSOptions, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setup_UI()

    def setup_UI(self):
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setup_option_btns()

    def setup_option_btns(self):
        formbtnsgroup = QGroupBox("Form Options")
        formbtnslayout = QVBoxLayout()
        formbtnsgroup.setLayout(formbtnslayout)

        self.add_form_btn = QPushButton("Add")
        self.find_form_btn = QPushButton("Find")
        self.archive_form_btn = QPushButton("Archives")

        self.logout_btn = QPushButton("Log Out")

        formbtnslayout.addWidget(self.add_form_btn)
        formbtnslayout.addWidget(self.find_form_btn)
        formbtnslayout.addWidget(self.archive_form_btn)
        self.mainlayout.addWidget(self.logout_btn)
        self.mainlayout.addWidget(formbtnsgroup)
        self.mainlayout.addStretch()
        