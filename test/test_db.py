from db.manager import Manager
from db.tables import *
from faker import Faker
from datetime import datetime

id = 0

def test_add_jhs():
    global id
    subject_names = [
        "Science", 
        "Mathematics", 
        "English", 
        "Filipino", 
        "Physical Education",
        "MAPEH"
    ]
    id += 1
    faker = Faker()
    manager = Manager()
    jhs_learner = JHSLearner(
        fname=faker.unique.first_name(),
        mname=faker.unique.last_name(),
        lname=faker.unique.last_name(),
        sex=faker.random.choice(["Male", "Female"]),
        birthdate=datetime.now(),
        learner_ref=id,
        mother_name=" ".join([faker.unique.first_name(), faker.unique.last_name()]),
        father_name=" ".join([faker.unique.first_name(), faker.unique.last_name()]),
        guardian_name=" ".join([faker.unique.first_name(), faker.unique.last_name()]),
    )
    jhs_form = JHSForm(jhs_learner=jhs_learner)
    jhs_record = JHSRecord(jhs_form=jhs_form)
    jhs_grades = JHSGrades(jhs_record=jhs_record)
    for _ in range(4):
        jhs_grade = JHSGrade(
            subject=faker.random.choice(subject_names),
            first_rating=faker.random.randint(85, 95),
            second_rating=faker.random.randint(85, 95),
            third_rating=faker.random.randint(85, 95),
            fourth_rating=faker.random.randint(85, 95),
            final_rating=faker.random.randint(85, 95),
            remarks=faker.random.choice(["Good", "Very Good", "Excellent"])
        )
        jhs_grades.jhs_grade.append(jhs_grade)
    manager.session.add(jhs_form)
    manager.session.add(jhs_learner)
    manager.session.commit()
    manager.session.close()
    print("OK...")

def test_view_jhs():
    manager = Manager()
    jhs_forms = manager.session.query(JHSForm).all()
    for jhs_form in jhs_forms:
        print(jhs_form)
        print(jhs_form.jhs_learner)
        jhs_records = jhs_form.jhs_record
        for jhs_record in jhs_records:
            print(jhs_record)
            jhs_grades_group = jhs_record.jhs_grades
            for grades in jhs_grades_group:
                jhs_subject_grades = grades.jhs_grade
                for grade in jhs_subject_grades:
                    print(grade.subject)
        print("\n\n\n")