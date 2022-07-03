from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QGroupBox, QGridLayout,
    QLineEdit, QLabel,
    QDateEdit, QComboBox,
    QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class JHSFindForm(QWidget):

    def __init__(self, parent=None):
        super(JHSFindForm, self).__init__(parent)
        self.setup_UI()

    def setup_UI(self):
        self.mainlayout = QVBoxLayout()
        self.formlayout = QVBoxLayout()
        self.formhdrlayout = QVBoxLayout()
        self.formbtnslayout = QHBoxLayout()

        self.learnerlayout = QGridLayout()
        self.fnamelayout = QVBoxLayout()
        self.mnamelayout = QVBoxLayout()
        self.lnamelayout = QVBoxLayout()
        self.extnamelayout = QVBoxLayout()
        self.lrnlayout = QVBoxLayout()
        self.bdatelayout = QVBoxLayout()
        self.sexlayout = QVBoxLayout()

        self.setup_learner_details()

        self.learnergroup = QGroupBox("Learner's Information")
        font = QFont()
        font.setPointSize(12)
        self.learnergroup.setFont(font)

        self.learnergroup.setLayout(self.learnerlayout)
        self.formlayout.addWidget(self.learnergroup)
        self.formlayout.addStretch(1)
        self.mainlayout.addLayout(self.formlayout)
        self.setLayout(self.mainlayout)

    # Set up learner information function
    def setup_learner_details(self):
        # Form Header Widgets
        self.formhdr_title = QLabel("Learner's Permanent Academic Record for Junior High School (SF10-JHS)")

        # Learner Information Widgets
        self.fname_label = QLabel("First Name:")
        self.fname_input = QLineEdit()
        self.mname_label = QLabel("Middle Name:")
        self.mname_input = QLineEdit()
        self.lname_label = QLabel("Last Name:")
        self.lname_input = QLineEdit()
        self.extname_label = QLabel("Name Ext.:")
        self.extname_input = QLineEdit()
        self.lrn_label = QLabel("LRN: ")
        self.lrn_input = QLineEdit()
        self.bdate_label = QLabel("Birthdate:")
        self.bdate_input = QDateEdit()
        self.sex_label = QLabel("Sex:")
        self.sex_input = QComboBox()

        # Form Header Widget Configurations
        self.formhdr_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Learner Information Widget Configurations
        self.sex_input.addItems(["Male", "Female"])
        self.bdate_input.setCalendarPopup(True)
        self.formhdrlayout.addWidget(self.formhdr_title)

        # Learner Information Layout Configurations
        self.fnamelayout.addWidget(self.fname_label)
        self.fnamelayout.addWidget(self.fname_input)
        self.mnamelayout.addWidget(self.mname_label)
        self.mnamelayout.addWidget(self.mname_input)
        self.lnamelayout.addWidget(self.lname_label)
        self.lnamelayout.addWidget(self.lname_input)
        self.extnamelayout.addWidget(self.extname_label)
        self.extnamelayout.addWidget(self.extname_input)
        self.lrnlayout.addWidget(self.lrn_label)
        self.lrnlayout.addWidget(self.lrn_input)
        self.bdatelayout.addWidget(self.bdate_label)
        self.bdatelayout.addWidget(self.bdate_input)
        self.sexlayout.addWidget(self.sex_label)
        self.sexlayout.addWidget(self.sex_input)
        self.learnerlayout.addLayout(self.lnamelayout, 0, 0)
        self.learnerlayout.addLayout(self.fnamelayout, 0, 1)
        self.learnerlayout.addLayout(self.extnamelayout, 0, 2)
        self.learnerlayout.addLayout(self.mnamelayout, 0, 3)
        self.learnerlayout.addLayout(self.lrnlayout, 1, 0)
        self.learnerlayout.addLayout(self.bdatelayout, 1, 1)
        self.learnerlayout.addLayout(self.sexlayout, 1, 2)
