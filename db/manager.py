from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tools.singleton import Singleton
from tools.utils import Config
from db.tables import *
from tools.utils import toBinary
from datetime import datetime

class Manager(metaclass=Singleton):

    JHS = 1
    SHS = 2

    def __init__(self):
        self.cfg = Config()
        self.db_name = self.cfg.parser.get("database", "name")
        self.engine = create_engine("sqlite:///{db_name}.db".format(db_name=self.db_name))
        base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def user_authenticate(self, username, password):
        query = self.session.query(User).filter(User.username==username, User.password==password).first()
        if query is not None:
            return True
        return False

    def jhs_add_form(self, filepath, learnerinfo, record):
        jhs_learner = JHSLearner()
        jhs_form = JHSForm(jhs_learner=jhs_learner)
        jhs_form.jhs_date_submitted = datetime.now()
        jhs_learner.fname = learnerinfo[0]
        jhs_learner.mname = learnerinfo[1]
        jhs_learner.lname = learnerinfo[2]
        jhs_learner.name_ext = learnerinfo[3]
        jhs_learner.sex = learnerinfo[6]
        jhs_learner.birthdate = learnerinfo[5]
        jhs_learner.learner_ref = learnerinfo[4]
        jhs_learner.id_image = toBinary(filepath)
        for i in record:
            details = i[0]
            grades = i[1]
            schoolname = details[0]
            schoolid = int(details[1])
            district = details[2]
            division = details[3]
            region = details[4]
            gradelvl = int(details[5])
            section = details[6]
            schoolyr = details[7]
            adviser = details[8]
            record = JHSRecord()
            record.school_name = schoolname
            record.school_id = schoolid
            record.district = district
            record.division = division
            record.region = region
            record.grade_level = gradelvl
            record.section = section
            record.school_year = schoolyr
            record.adviser_name = adviser
            grades_group = JHSGrades()
            for j in grades:
                subject = j[0]
                q1 = float(j[1])
                q2 = float(j[2])
                q3 = float(j[3])
                q4 = float(j[4])
                final = float(j[5])
                remarks = j[6]
                grades = JHSGrade()
                grades.subject = subject
                grades.first_rating = q1
                grades.second_rating = q2
                grades.third_rating = q3
                grades.fourth_rating = q4
                grades.final_rating = final
                grades.remarks = remarks
                grades_group.jhs_grade.append(grades)
            record.jhs_grades.append(grades_group)
            jhs_form.jhs_record.append(record)
        self.session.add(jhs_learner)
        self.session.add(jhs_form)
        self.session.commit()
        self.session.close()

    def jhs_search_form(self, learnerinfo):
        fname = learnerinfo[0]
        mname = learnerinfo[1]
        lname = learnerinfo[2]
        name_ext = learnerinfo[3]
        sex = learnerinfo[6]
        birthdate = learnerinfo[5]
        learner_ref = learnerinfo[4]
        query = self.session.query(JHSLearner).filter(
            JHSLearner.fname == fname,
            JHSLearner.mname == mname,
            JHSLearner.lname == lname,
            JHSLearner.name_ext == name_ext,
            JHSLearner.sex == sex,
            JHSLearner.birthdate == birthdate,
            JHSLearner.learner_ref == learner_ref
        ).all()
        if query is not None:
            return query
        return []