#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 19, 2018, 5:54 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from data import init_data, init_database
from data.init_data import session
from core import common


class Teacher(object):
    def __init__(self, name):
        self.name = name

    def add_grade(self, grade_name):
        '''
        Add a course
        :param grade_name:
        :return: True if success, else False
        '''
        try:
            grade = init_database.Grade(name=grade_name)
            session.add(grade)
            session.commit()
            return True
        except:
            print('Adding course failed.'.center(50, ' '))
            return False

    def add_student_to_grade(self, student_qq, grade_name):
        '''
        Add a student to the Course
        :param student_qq:
        :param grade_name:
        :return: True if success, else False
        '''
        try:
            student = common.get_student_by_qq(student_qq)
            grade = common.get_grade(grade_name)
            grade.students.append(student)
            session.commit()
            return True
        except:
            print('Adding student failed.'.center(50, ' '))

    def add_grade_record(self, grade_name):
        '''
        Add a grade record
        :param grade_name:
        :return:
        '''
        try:
            grade = common.get_grade(grade_name)
            students = grade.students
            records = []
            for student in students:
                grade_record = common.get_grade_record(
                    grade_name,
                    student.qq,
                    init_data.get_time()
                )

                if grade_record == None:
                    # Add if empty
                    grade_record = init_data.GradeRecord(
                        grade=grade,
                        student=student,
                        date=init_data.get_time()
                    )
                    records.append(grade_record)

            session.add_all(records)
            session.commit()
            return True

        except:
            return False

    def modify_score(self, grade_name, student_qq, date, score):
        '''
        Modify students scores
        :param grade_name:
        :param student_qq:
        :param date:
        :param score:
        :return: True if success, else False
        '''
        grade_record = common.get_grade_record(grade_name, student_qq, date)

        if grade_record != None:
            grade_record.score = score
            session.commit()
            return True
        else:
            return False


if __name__ == '__main__':
    t = Teacher('Wong Sir')
    ret = t.modify_score('Math', '012465', '2018-02-04', 12)
    print(ret)
