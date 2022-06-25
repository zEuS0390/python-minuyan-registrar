from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QGridLayout, QLabel,
    QLineEdit
)

class AddForm(QWidget):

    def __init__(self, parent=None):
        super(AddForm, self).__init__(parent)
        self.setup_UI()

    def setup_UI(self):
        self.setup_layouts()
        self.setup_personal_details()

    def setup_layouts(self):
        self.mainlayout = QVBoxLayout()
        self.personallayout = QGridLayout()
        self.fnamelayout = QVBoxLayout()
        self.mnamelayout = QVBoxLayout()
        self.lnamelayout = QVBoxLayout()
        self.mainlayout.addLayout(self.personallayout)
        self.setLayout(self.mainlayout)

    def setup_personal_details(self):
        self.fname_label = QLabel("First Name:")
        self.fname_input = QLineEdit()
        self.mname_label = QLabel("Middle Name:")
        self.mname_input = QLineEdit()
        self.lname_label = QLabel("Last Name:")
        self.lname_input = QLineEdit()

        self.fnamelayout.addWidget(self.fname_label)
        self.fnamelayout.addWidget(self.fname_input)
        self.fnamelayout.addStretch()
        self.mnamelayout.addWidget(self.mname_label)
        self.mnamelayout.addWidget(self.mname_input)
        self.mnamelayout.addStretch()
        self.lnamelayout.addWidget(self.lname_label)
        self.lnamelayout.addWidget(self.lname_input)
        self.lnamelayout.addStretch()

        self.personallayout.addLayout(self.fnamelayout, 0, 0)
        self.personallayout.addLayout(self.mnamelayout, 0, 1)
        self.personallayout.addLayout(self.lnamelayout, 0, 2)