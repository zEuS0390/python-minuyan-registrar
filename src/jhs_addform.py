from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QGridLayout, QLabel,
    QLineEdit, QComboBox,
    QGroupBox, QScrollArea,
    QTabWidget, QPushButton,
    QHBoxLayout, QTableWidget,
    QAbstractScrollArea, QHeaderView, 
    QSizePolicy, QFileDialog, QDateEdit
)
from PyQt5.QtCore import Qt
from db.manager import Manager

class JHSAddForm(QWidget):

    def __init__(self, parent=None):
        super(JHSAddForm, self).__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.db = Manager()
        self.setup_UI()

    # Set up user interface function
    def setup_UI(self):
        self.setup_layouts()
        self.setup_form_upload()
        self.setup_learner_details()
        self.setup_record()
        self.setup_form_btns()

    def setup_layouts(self):
        # Create layouts
        self.mainlayout = QVBoxLayout()
        self.formlayout = QVBoxLayout()
        self.formhdrlayout = QVBoxLayout()
        self.formbtnslayout = QHBoxLayout()

        # Image file upload layouts
        self.imageuploadlayout = QVBoxLayout()
        self.uploadinputlayout = QHBoxLayout()

        # Learner layouts
        self.learnerlayout = QGridLayout()
        self.fnamelayout = QVBoxLayout()
        self.mnamelayout = QVBoxLayout()
        self.lnamelayout = QVBoxLayout()
        self.extnamelayout = QVBoxLayout()
        self.lrnlayout = QVBoxLayout()
        self.bdatelayout = QVBoxLayout()
        self.sexlayout = QVBoxLayout()

        # Record layouts
        self.recordlayout = QVBoxLayout()
        self.recordbtnslayout = QHBoxLayout()

        # Set up form
        self.formwidget = QWidget()
        self.formwidget.setLayout(self.formlayout)
        self.imageuploadgroup = QGroupBox("Image Upload")
        self.learnergroup = QGroupBox("Learner's Information")
        self.recordgroup = QGroupBox("Scholastic Record")
        self.learnergroup.setLayout(self.learnerlayout)
        self.recordgroup.setLayout(self.recordlayout)
        self.formlayout.addLayout(self.formhdrlayout)
        self.formlayout.addWidget(self.imageuploadgroup)
        self.formlayout.addWidget(self.learnergroup)
        self.formlayout.addWidget(self.recordgroup)
        self.formlayout.addStretch(1)
        self.formscrollarea = QScrollArea()
        self.formscrollarea.setWidgetResizable(True)
        self.formscrollarea.setWidget(self.formwidget)

        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.addWidget(self.formscrollarea)
        self.mainlayout.addLayout(self.formbtnslayout)
        self.setLayout(self.mainlayout)

    def setup_form_upload(self):
        self.imageuploadgroup.setLayout(self.imageuploadlayout)
        imageupload_btn = QPushButton("...")
        self.imageupload_input = QLineEdit()
        imageupload_btn.clicked.connect(self.uploadImage)
        self.uploadinputlayout.addWidget(self.imageupload_input)
        self.uploadinputlayout.addWidget(imageupload_btn)
        self.imageuploadlayout.addLayout(self.uploadinputlayout)

    # Set up form buttons
    def setup_form_btns(self):
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        clear_btn = QPushButton("Clear")
        submit_btn.clicked.connect(self.submit)
        cancel_btn.clicked.connect(self.cancel)
        clear_btn.clicked.connect(self.clear)
        self.formbtnslayout.addStretch()
        self.formbtnslayout.addWidget(clear_btn)
        self.formbtnslayout.addWidget(cancel_btn)
        self.formbtnslayout.addWidget(submit_btn)

    def uploadImage(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Upload Image File", r"C:\\", "Image Files (*.jpg *.png *.gif)")
        if len(filename) != 0:
            self.imageupload_input.setText(filename)

    # Submit form
    def submit(self):
        # Learner information inputs
        filepath = self.imageupload_input.text()
        learnerinfo = [
            self.fname_input.text(), self.mname_input.text(),
            self.lname_input.text(), self.extname_input.text(),
            self.lrn_input.text(), self.bdate_input.date().toPyDate(),
            self.sex_input.currentText()
        ]
        record = []
        # Record inputs
        for n in range(self.recordtabs.count()):
            w = self.recordtabs.widget(n) # # Widget
            wl = w.layout() # Widget layout
            groupboxes = [] # A list of groupboxes
            for m in range(wl.count()):
                groupboxes.append(wl.itemAt(m).widget())
            dl = groupboxes[0].layout() # Details layout
            # Loop on every vertical layout in details group
            ins = [] # Inputs
            for m in range(dl.count()):
                dvl = dl.itemAt(m) # Vertical layout
                i = dvl.itemAt(1).widget().text() # Input
                ins.append(i)
            tb = groupboxes[1].layout().itemAt(1).widget() # Grades table layout            
            gins = [] # Grade inputs
            tbrc = tb.rowCount() # Grades table row count
            tbcc = tb.columnCount() # Grades table column count
            for m in range(tbrc):
                ginsi = [] # Grade inputs item
                for k in range(tbcc):
                    it = tb.item(m, k) # Get widget item in row (m) and column (k)
                    if it is not None:
                        ginsi.append(it.text())
                    else:
                        ginsi.append("")
                gins.append(ginsi)
            record.append((ins, gins))
        try:
            self.db.jhs_add_form(filepath, learnerinfo, record)
            print("Successfully submitted the form")
        except:
            print("Failed submitting the form!")
                        
    # Cancel form
    def cancel(self):
        pass

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

    # Set up scholastic record
    def setup_record(self):
        # Record Tabs Widget
        self.recordtabs = QTabWidget()
        self.add_record()

        # Button Widgets
        self.add_record_btn = QPushButton("Add")
        self.delete_record_btn = QPushButton("Delete")
        self.add_record_btn.clicked.connect(self.add_record)
        self.delete_record_btn.clicked.connect(self.delete_record)

        self.recordbtnslayout.addWidget(self.add_record_btn)
        self.recordbtnslayout.addWidget(self.delete_record_btn)

        self.recordlayout.addLayout(self.recordbtnslayout)
        self.recordlayout.addWidget(self.recordtabs)

    # Add record function
    def add_record(self):
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
            pass
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

    # Delete the record tab
    def delete_record(self):
        if self.recordtabs.count() > 0:
            index = self.recordtabs.currentIndex()
            self.recordtabs.removeTab(index)

    # Clear the form inputs
    def clear(self):
        # Clear the file path
        self.imageupload_input.clear()

        # Clear the learner information inputs
        self.fname_input.clear()
        self.mname_input.clear()
        self.lname_input.clear()
        self.extname_input.clear()
        self.lrn_input.clear()
        self.bdate_input.date().toPyDate()
        self.sex_input.setCurrentIndex(0)