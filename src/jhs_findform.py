from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QGroupBox, QGridLayout,
    QLineEdit, QLabel,
    QDateEdit, QComboBox,
    QHBoxLayout, QScrollArea,
    QPushButton, QTabWidget,
    QSizePolicy, QAbstractScrollArea,
    QHeaderView, QTableWidget
)
from PyQt5.QtGui import QFont, QPixmap
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
        self.imglayout = QVBoxLayout()

        self.learnerlayout = QGridLayout()
        self.fnamelayout = QVBoxLayout()
        self.mnamelayout = QVBoxLayout()
        self.lnamelayout = QVBoxLayout()
        self.extnamelayout = QVBoxLayout()
        self.lrnlayout = QVBoxLayout()
        self.bdatelayout = QVBoxLayout()
        self.sexlayout = QVBoxLayout()

        self.searchresultlayout = QVBoxLayout()
        self.recordlayout = QHBoxLayout()

        self.setup_learner_details()
        self.setup_form_btns()
        self.setup_learner_image()
        self.setup_record()

        self.learnergroup = QGroupBox("Learner's Information")
        font = QFont()
        font.setPointSize(12)
        self.learnergroup.setFont(font)

        self.searchresultgroup = QGroupBox("Found Record")
        font = QFont()
        font.setPointSize(12)
        self.searchresultgroup.setFont(font)

        self.learnergroup.setLayout(self.learnerlayout)
        self.searchresultgroup.setLayout(self.searchresultlayout)
        self.formlayout.addLayout(self.formhdrlayout)
        self.formlayout.addLayout(self.imglayout)
        self.formlayout.addWidget(self.learnergroup)
        self.formlayout.addWidget(self.searchresultgroup)
        self.formlayout.addStretch()

        # Form Scroll Area Widget
        self.formwidget = QWidget()
        self.formwidget.setLayout(self.formlayout)
        self.formscrollarea = QScrollArea()
        self.formscrollarea.setWidgetResizable(True)
        self.formscrollarea.setWidget(self.formwidget)
        self.mainlayout.addWidget(self.formscrollarea)
        self.mainlayout.addLayout(self.formbtnslayout)

        # self.mainlayout.setContentsMargins(0, 0, 0, 0)
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

    def setup_learner_image(self):
        # Profile picture
        self.image = QLabel()
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(":/profile_default")
        self.image.setPixmap(pixmap.scaled(224, 224, Qt.KeepAspectRatio))
        self.imglayout.addWidget(self.image)

    def setup_record(self):
        font = QFont()
        font.setPointSize(12)
        # Record Tabs Widget
        self.recordtabs = QTabWidget()
        self.recordtabs.setFont(font)
        self.recordlayout.addWidget(self.recordtabs)
        self.searchresultlayout.addWidget(self.recordtabs)
        # self.add_record()

    # Add record function
    def add_record(self, details, grades):
        record = QWidget()
        record.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.recordtabs.addTab(record, "Record")

        # Set up record
        record_layout = QVBoxLayout()
        detailsgroup = QGroupBox("Record Details")
        gradesgroup = QGroupBox("Grades")
        record_layout.addWidget(detailsgroup)
        record_layout.addWidget(gradesgroup)
        record.setLayout(record_layout)
        
        # Set up detail layouts
        detailslayout = QGridLayout()
        schoolnamelayout = QVBoxLayout()
        schoolidlayout = QVBoxLayout()
        districtlayout = QVBoxLayout()
        divisionlayout = QVBoxLayout()
        regionlayout = QVBoxLayout()
        gradelvllayout = QVBoxLayout()
        sectionlayout = QVBoxLayout()
        schoolyrlayout = QVBoxLayout()
        adviserlayout = QVBoxLayout()

        # Detail widgets
        schoolname_label = QLabel("School Name:")
        schoolname_input = QLineEdit()
        schoolid_label = QLabel("School ID:")
        schoolid_input = QLineEdit()
        district_label = QLabel("District:")
        district_input = QLineEdit()
        division_label = QLabel("Division:")
        division_input = QLineEdit()
        region_label = QLabel("Region:")
        region_input = QLineEdit()
        gradelvl_label = QLabel("Grade Level:")
        gradelvl_input = QLineEdit()
        section_label = QLabel("Section:")
        section_input = QLineEdit()
        schoolyr_label = QLabel("School Year:")
        schoolyr_input = QLineEdit()
        adviser_label = QLabel("Adviser:")
        adviser_input = QLineEdit()

        # Detail layout configurations
        schoolnamelayout.addWidget(schoolname_label)
        schoolnamelayout.addWidget(schoolname_input)
        schoolidlayout.addWidget(schoolid_label)
        schoolidlayout.addWidget(schoolid_input)
        districtlayout.addWidget(district_label)
        districtlayout.addWidget(district_input)
        divisionlayout.addWidget(division_label)
        divisionlayout.addWidget(division_input)
        regionlayout.addWidget(region_label)
        regionlayout.addWidget(region_input)
        gradelvllayout.addWidget(gradelvl_label)
        gradelvllayout.addWidget(gradelvl_input)
        sectionlayout.addWidget(section_label)
        sectionlayout.addWidget(section_input)
        schoolyrlayout.addWidget(schoolyr_label)
        schoolyrlayout.addWidget(schoolyr_input)
        adviserlayout.addWidget(adviser_label)
        adviserlayout.addWidget(adviser_input)
        detailslayout.addLayout(schoolnamelayout, 0, 0)
        detailslayout.addLayout(schoolidlayout, 0, 1)
        detailslayout.addLayout(districtlayout, 0, 2)
        detailslayout.addLayout(divisionlayout, 1, 0)
        detailslayout.addLayout(regionlayout, 1, 1)
        detailslayout.addLayout(gradelvllayout, 1, 2)
        detailslayout.addLayout(sectionlayout, 2, 0)
        detailslayout.addLayout(schoolyrlayout, 2, 1)
        detailslayout.addLayout(adviserlayout, 2, 2)
        detailsgroup.setLayout(detailslayout)

        # Set up grades layout
        gradeslayout = QVBoxLayout()
        gradeshdrlayout = QHBoxLayout()
        gradesbtnlayout = QHBoxLayout()
        gaveragelayout = QHBoxLayout()

        # Set up grade widgets
        gradestable = QTableWidget()
        add_grades_btn = QPushButton("Add")
        delete_grades_btn = QPushButton("Delete")
        gaverage_label = QLabel("General Average:")
        gaverage_val = QLabel()

        # Grade table headers
        gradestable_hdrs = [
            "Subject",
            "Q1",
            "Q2",
            "Q3",
            "Q4",
            "Final",
            "Remarks"
        ]

        # Grade widget configurations
        gradestable.setColumnCount(len(gradestable_hdrs))
        gradestable.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        gradestable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        gradestable.horizontalHeader().setStretchLastSection(True)
        gradestable.verticalHeader().setVisible(True)
        gradestable.setAlternatingRowColors(True)
        gradestable.setHorizontalHeaderLabels(gradestable_hdrs)
        gradestable.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        gradestable.verticalHeader().setVisible(False)
        gradestable_hdr = gradestable.horizontalHeader()
        for row, _ in enumerate(gradestable_hdrs):
            gradestable_hdr.setSectionResizeMode(row, QHeaderView.ResizeMode.Stretch)
        
        # Add row in grades table
        def add_grades_row():
            rowcount = gradestable.rowCount()+1
            gradestable.setRowCount(rowcount)
        add_grades_btn.clicked.connect(add_grades_row)

        # Delete the selected row in grades table
        def delete_grades_row():
            rowcount = gradestable.rowCount()-1
            gradestable.setRowCount(rowcount)
        delete_grades_btn.clicked.connect(delete_grades_row)

        # Grade layout configurations
        gradesbtnlayout.addWidget(add_grades_btn)
        gradesbtnlayout.addWidget(delete_grades_btn)
        gaveragelayout.addWidget(gaverage_label)
        gaveragelayout.addWidget(gaverage_val)
    
        gradeshdrlayout.addLayout(gradesbtnlayout)
        gradeshdrlayout.addStretch()
        gradeshdrlayout.addLayout(gaveragelayout)

        gradeslayout.addLayout(gradeshdrlayout)
        gradeslayout.addWidget(gradestable)
        gradeslayout.addStretch()
        
        gradesgroup.setLayout(gradeslayout)

        schoolname_input.setText(details["school_name"])
        schoolid_input.setText(str(details["school_id"]))
        district_input.setText(details["district"])
        division_input.setText(details["division"])
        region_input.setText(details["region"])
        gradelvl_input.setText(str(details["grade_level"]))
        section_input.setText(details["section"])
        schoolyr_input.setText(details["school_year"])
        adviser_input.setText(details["adviser_name"])

    # Set up submit function
    def submit(self):
        learnerinfo = [
            self.fname_input.text().strip(), self.mname_input.text().strip(),
            self.lname_input.text().strip(), self.extname_input.text().strip(),
            self.lrn_input.text().strip(), self.bdate_input.date().toPyDate(),
            self.sex_input.currentText().strip()
        ]
        learner = self.db.jhs_search_form(learnerinfo)
        if learner is not None:
            result = self.db.jhs_search_record(learner.jhs_learner_id)
            pixmap = QPixmap()
            pixmap.loadFromData(learner.id_image)
            self.image.setPixmap(pixmap)
            for index in range(len(result[0])):
                details = {
                    "school_name": result[0][index].school_name,
                    "school_id": result[0][index].school_id,
                    "district": result[0][index].district,
                    "division": result[0][index].division,
                    "region": result[0][index].region,
                    "grade_level": result[0][index].grade_level,
                    "section": result[0][index].section,
                    "school_year": result[0][index].school_year,
                    "adviser_name": result[0][index].adviser_name
                }
                grades = []
                for gsindex in range(len(result[1][index])):
                    gs = {
                        "subject": result[1][index][gsindex].subject,
                        "first_rating": result[1][index][gsindex].first_rating,
                        "second_rating": result[1][index][gsindex].second_rating,
                        "third_rating": result[1][index][gsindex].third_rating,
                        "fourth_rating": result[1][index][gsindex].fourth_rating,
                        "final_rating": result[1][index][gsindex].final_rating,
                        "remarks": result[1][index][gsindex].remarks
                    }
                    grades.append(gs)
                while self.recordtabs.count() > 0:
                    self.delete_record()
                self.add_record(details, grades)

    # Delete the record tab
    def delete_record(self):
        if self.recordtabs.count() > 0:
            index = self.recordtabs.currentIndex()
            self.recordtabs.removeTab(index)

    # Clear found data
    def clear(self):
        pixmap = QPixmap(":/profile_default")
        self.image.setPixmap(pixmap.scaled(224, 224, Qt.KeepAspectRatio))

        # Clear the learner information inputs
        self.fname_input.clear()
        self.mname_input.clear()
        self.lname_input.clear()
        self.extname_input.clear()
        self.lrn_input.clear()
        self.bdate_input.date().toPyDate()
        self.sex_input.setCurrentIndex(0)

        # Record inputs
        for n in range(self.recordtabs.count()):
            w = self.recordtabs.widget(n) # # Widget
            wl = w.layout() # Widget layout
            groupboxes = [] # A list of groupboxes
            for m in range(wl.count()):
                groupboxes.append(wl.itemAt(m).widget())
            dl = groupboxes[0].layout() # Details layout
            # Loop on every vertical layout in details group
            for m in range(dl.count()):
                dvl = dl.itemAt(m) # Vertical layout
                dvl.itemAt(1).widget().clear()
            tb = groupboxes[1].layout().itemAt(1).widget() # Grades table layout            
            tbrc = tb.rowCount() # Grades table row count
            tbcc = tb.columnCount() # Grades table column count
            for m in range(tbrc):
                for k in range(tbcc):
                    it = tb.item(m, k) # Get widget item in row (m) and column (k)
                    if it is not None:
                        it.setText("")

        while self.recordtabs.count() > 0:
            self.delete_record()