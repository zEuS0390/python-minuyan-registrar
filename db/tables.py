from sqlalchemy import (
    FLOAT, Column, 
    VARCHAR, ForeignKey, 
    Integer, Date, BLOB
)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

base = declarative_base()

"""
----- Junior High School Tables -----
"""

# SF10 Form Table
class JHSForm(base):
    __tablename__ = "jhs_form"
    jhs_form_id = Column(Integer, primary_key=True)
    jhs_learner_id = Column(Integer, ForeignKey('jhs_learner.jhs_learner_id'))
    jhs_record = relationship('JHSRecord', backref='jhs_form', cascade="all, delete-orphan")
    def __repr__(self):
        return f"JHSForm(jhs_form_id='{self.jhs_form_id}')"

# Learner Table
class JHSLearner(base):
    __tablename__ = "jhs_learner"
    jhs_learner_id = Column(Integer, primary_key=True)
    fname = Column(VARCHAR(50))
    mname = Column(VARCHAR(50))
    lname = Column(VARCHAR(50))
    name_ext = Column(VARCHAR(50), nullable=True)
    sex = Column(VARCHAR(50))
    birthdate = Column(Date)
    learner_ref = Column(Integer, unique=True)
    id_image = Column(BLOB)
    mother_name = Column(VARCHAR(100))
    father_name = Column(VARCHAR(100))
    guardian_name = Column(VARCHAR(100))
    mother_mobile = Column(VARCHAR(50))
    father_mobile = Column(VARCHAR(50))
    guardian_mobile = Column(VARCHAR(50))
    res_address = Column(VARCHAR(200))
    jhs_form = relationship('JHSForm', backref="jhs_learner", cascade="all, delete-orphan")
    def __repr__(self):
        return f"JHSLearner(jhs_learner_id={self.jhs_learner_id}, fname='{self.fname}', mname='{self.mname}', lname='{self.lname}', name_ext='{self.name_ext}', sex='{self.sex}', birthdate='{self.birthdate}',learner_ref='{self.learner_ref}')"

# Scholastic Record Table
class JHSRecord(base):
    __tablename__ = "jhs_record"
    jhs_record_id = Column(Integer, primary_key=True)
    school_name = Column(VARCHAR(100))
    school_id = Column(Integer)
    district = Column(VARCHAR(100))
    division = Column(VARCHAR(100))
    region = Column(VARCHAR(100))
    grade_level = Column(Integer)
    section = Column(VARCHAR(50))
    school_year = Column(VARCHAR(50))
    adviser_name = Column(VARCHAR(100))
    jhs_form_id = Column(Integer, ForeignKey("jhs_form.jhs_form_id"))
    jhs_grades = relationship("JHSGrades", backref="jhs_record", cascade="all, delete-orphan")
    remedials = relationship("JHSRemedials", backref="jhs_record", cascade="all, delete-orphan")
    def __repr__(self):
        return f"JHSRecord(jhs_record_id='{self.jhs_record_id}', school_name='{self.school_name}', school_id='{self.school_id}', district='{self.district}', division='{self.division}', region='{self.region}', grade_leve='{self.grade_level}', section='{self.section}', school_year='{self.school_year}', adviser_name='{self.adviser_name}', jhs_form_id='{self.jhs_form_id}')"

# Grades Group Table
class JHSGrades(base):
    __tablename__ = "jhs_grades"
    jhs_grades_id = Column(Integer, primary_key=True)
    jhs_record_id = Column(Integer, ForeignKey('jhs_record.jhs_record_id'))
    jhs_grade = relationship("JHSGrade", backref="jhs_grades", cascade="all, delete-orphan")
    def __repr__(self):
        return f"JHSGrades(jhs_grades_id='{self.jhs_grades_id}')"

# Grade Table
class JHSGrade(base):
    __tablename__ = "jhs_grade"
    jhs_grade_id = Column(Integer, primary_key=True)
    jhs_grades_id = Column(Integer, ForeignKey('jhs_grades.jhs_grades_id'))
    subject = Column(VARCHAR(50))
    first_rating = Column(FLOAT)
    second_rating = Column(FLOAT)
    third_rating = Column(FLOAT)
    fourth_rating = Column(FLOAT)
    final_rating = Column(FLOAT, nullable=True)
    remarks = Column(VARCHAR(100), nullable=True)
    def __repr__(self):
        return f"JHSGrade(jhs_grade_id='{self.jhs_grade_id}', subject='{self.subject}', first_rating='{self.first_rating}', second_rating='{self.second_rating}', third_rating='{self.third_rating}', fourth_rating='{self.fourth_rating}, final_rating='{self.final_rating}', remarks='{self.remarks}')"

# Remidials Group Table
class JHSRemedials(base):
    __tablename__ = "jhs_remedials"
    jhs_remedials_id = Column(Integer, primary_key=True)
    jhs_record_id = Column(Integer, ForeignKey('jhs_record.jhs_record_id'))
    initial_date = Column(Date)
    final_date = Column(Date)
    remedial = relationship("JHSRemedial", backref="remedial", cascade="all, delete-orphan")
    def __repr__(self):
        return f"JHSRemedials(jhs_remedials_id='{self.jhs_remedials_id}', jhs_record_id='{self.jhs_record_id}', initial_date='{self.initial_date}', final_date='{self.final_date}')"

class JHSRemedial(base):
    __tablename__ = "jhs_remedial"
    jhs_remedial_id = Column(Integer, primary_key=True)
    jhs_remedials_id = Column(Integer, ForeignKey('jhs_remedials.jhs_remedials_id'))
    subject = Column(VARCHAR(50))
    final_rating = Column(FLOAT)
    class_mark = Column(VARCHAR(50))
    recomputed = Column(FLOAT)
    remarks = Column(VARCHAR(50))
    def __repr__(self):
        return f"JHSRemedial(jhs_remedial_id={self.jhs_remedial_id}, subject='{self.subject}', final_rating='{self.final_rating}', class_mark='{self.class_mark}', recomputed='{self.recomputed}', remarks='{self.remarks}')"

"""
----- Senior High School Tables -----
"""

# SF10 Form Table
class SHSForm(base):
    __tablename__ = "shs_form"
    shs_form_id = Column(Integer, primary_key=True)
    shs_learner_id = Column(Integer, ForeignKey('shs_learner.shs_learner_id'))
    shs_record = relationship('SHSRecord', backref='shs_form', cascade="all, delete-orphan")
    def __repr__(self):
        return f"SF10Form(shs_form_id='{self.shs_form_id}')"

# Learner Table
class SHSLearner(base):
    __tablename__ = "shs_learner"
    shs_learner_id = Column(Integer, primary_key=True)
    fname = Column(VARCHAR(50))
    mname = Column(VARCHAR(50))
    lname = Column(VARCHAR(50))
    name_ext = Column(VARCHAR(50), nullable=True)
    sex = Column(VARCHAR(50))
    birthdate = Column(Date)
    learner_ref = Column(Integer, unique=True)
    id_image = Column(BLOB)
    mother_name = Column(VARCHAR(100))
    father_name = Column(VARCHAR(100))
    guardian_name = Column(VARCHAR(100))
    mother_mobile = Column(VARCHAR(50))
    father_mobile = Column(VARCHAR(50))
    guardian_mobile = Column(VARCHAR(50))
    res_address = Column(VARCHAR(200))
    shs_form = relationship('SHSForm', backref="shs_learner", cascade="all, delete-orphan")
    def __repr__(self):
        return f"SHSLearner(fname='{self.fname}', mname='{self.mname}', lname='{self.lname}', name_ext='{self.name_ext}', sex='{self.sex}', birthdate='{self.birthdate}',learner_ref='{self.learner_ref}')"

# Scholastic Record Table
class SHSRecord(base):
    __tablename__ = "shs_record"
    shs_record_id = Column(Integer, primary_key=True)
    school_name = Column(VARCHAR(100))
    school_id = Column(Integer)
    grade_level = Column(Integer)
    section = Column(VARCHAR(50))
    school_year = Column(VARCHAR(50))
    adviser_name = Column(VARCHAR(100))
    shs_form_id = Column(Integer, ForeignKey("shs_form.shs_form_id"))
    shs_grades = relationship("SHSGrades", backref="shs_record", cascade="all, delete-orphan")
    def __repr__(self):
        return f"SHSRecord(record_id='{self.shs_record_id}', school_name='{self.school_name}', school_id='{self.school_id}', grade_level='{self.grade_level}', section='{self.section}', school_year='{self.school_year}', adviser_name='{self.adviser_name}')"

# Grades Group Table
class SHSGrades(base):
    __tablename__ = "shs_grades"
    shs_grades_id = Column(Integer, primary_key=True)
    record_id = Column(Integer, ForeignKey('shs_record.shs_record_id'))
    shs_grade = relationship("SHSGrade", backref="shs_grade", cascade="all, delete-orphan")
    def __repr__(self):
        return f"SHSGrades(grades_id='{self.shs_grades_id}')"

# Grade Table
class SHSGrade(base):
    __tablename__ = "shs_grade"
    shs_grade_id = Column(Integer, primary_key=True)
    grades_id = Column(Integer, ForeignKey('shs_grades.shs_grades_id'))
    subject = Column(VARCHAR(50))
    subject_type = Column(VARCHAR(50))
    first_rating = Column(FLOAT)
    second_rating = Column(FLOAT)
    final_rating = Column(FLOAT, nullable=True)
    action_taken = Column(VARCHAR(100), nullable=True)
    def __repr__(self):
        return f"SHSGrade(shs_grade_id='{self.shs_grade_id}', subject='{self.subject}', first_rating='{self.first_rating}', second_rating='{self.second_rating}', final_rating='{self.final_rating}', action='{self.action_taken}')"

"""
----- Others -----
"""

# School Year Table
class SchoolYear(base):
    __tablename__ = "school_year"
    school_year_id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(50))
    def __repr__(self):
        return f"SchoolYear(school_year_id={self.school_year_id}, title='{self.title}')"