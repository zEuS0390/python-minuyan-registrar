from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QGroupBox, QGridLayout,
    QLineEdit, QLabel,
    QDateEdit, QComboBox,
    QHBoxLayout, QScrollArea,
    QPushButton, QTableWidget,
    QAbstractScrollArea, QAbstractItemView,
    QHeaderView
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from db.manager import Manager

"""
JHSFindForm Class Members
    Functions:
        __init__(self, parent=None)
        setup_UI(self)
        setup_learner_details(self)
"""

class JHSFindForm(QWidget):

    def __init__(self, parent=None):
        super(JHSFindForm, self).__init__(parent)
        self.db = Manager()
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

        self.searchresultlayout = QVBoxLayout()

        self.setup_learner_details()
        self.setup_form_btns()
        self.setup_search_result()

        self.learnergroup = QGroupBox("Learner's Information")
        font = QFont()
        font.setPointSize(12)
        self.learnergroup.setFont(font)

        self.learnergroup.setLayout(self.learnerlayout)
        self.formlayout.addLayout(self.formhdrlayout)
        self.formlayout.addWidget(self.learnergroup)
        self.formlayout.addLayout(self.searchresultlayout)

        # Form Scroll Area Widget
        self.formwidget = QWidget()
        self.formwidget.setLayout(self.formlayout)
        self.formscrollarea = QScrollArea()
        self.formscrollarea.setWidgetResizable(True)
        self.formscrollarea.setWidget(self.formwidget)
        self.mainlayout.addWidget(self.formscrollarea)
        self.mainlayout.addLayout(self.formbtnslayout)

        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainlayout)

    # Set up learner information function
    def setup_learner_details(self):
        font = QFont()
        font.setPointSize(12)

        # Form Header Widgets
        self.formhdr_title = QLabel("Learner's Permanent Academic Record for Junior High School (SF10-JHS) | Search Learner")
        self.formhdr_title.setFont(font)

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

    # Set up form buttons
    def setup_form_btns(self):
        font = QFont()
        font.setPointSize(12)
        submit_btn = QPushButton("Search")
        clear_btn = QPushButton("Clear")
        submit_btn.setFont(font)
        clear_btn.setFont(font)
        submit_btn.clicked.connect(self.submit)
        clear_btn.clicked.connect(self.clear)
        self.formbtnslayout.addStretch()
        self.formbtnslayout.addWidget(clear_btn)
        self.formbtnslayout.addWidget(submit_btn)

    def setup_search_result(self):
        font = QFont()
        font.setPointSize(12)
        searchresulttable_headers = {
            "no_of_record": "Number of Record",
            "date_created": "Date Created",
            "open_btn": "",
            "delete_btn": ""
        }
        self.searchresulttable = QTableWidget()
        self.searchresulttable.setFont(font)
        self.searchresulttable.setColumnCount(len(searchresulttable_headers))
        self.searchresulttable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.searchresulttable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.searchresulttable.horizontalHeader().setStretchLastSection(True)
        self.searchresulttable.verticalHeader().setVisible(True)
        self.searchresulttable.setAlternatingRowColors(True)
        self.searchresulttable.setHorizontalHeaderLabels(searchresulttable_headers.values())
        self.searchresulttable.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.searchresulttable.verticalHeader().setVisible(False)
        self.searchresulttable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.searchresulttable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.searchresulttable_header = self.searchresulttable.horizontalHeader()
        for row, _ in enumerate(searchresulttable_headers):
            self.searchresulttable_header.setSectionResizeMode(row, QHeaderView.ResizeMode.Stretch)
        self.searchresultlayout.addWidget(self.searchresulttable)

    # Set up submit function
    def submit(self):
        learnerinfo = [
            self.fname_input.text(), self.mname_input.text(),
            self.lname_input.text(), self.extname_input.text(),
            self.lrn_input.text(), self.bdate_input.date().toPyDate(),
            self.sex_input.currentText()
        ]
        self.db.jhs_search_form(learnerinfo)
        self.clear()

    def clear(self):
        # Clear the learner information inputs
        self.fname_input.clear()
        self.mname_input.clear()
        self.lname_input.clear()
        self.extname_input.clear()
        self.lrn_input.clear()
        self.bdate_input.date().toPyDate()
        self.sex_input.setCurrentIndex(0)