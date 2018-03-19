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


class Student(object):
    def __init__(self, qq):
        self.qq = qq

    def get_qq(self):
        return init_data.get_qq()

    def submit_task(self, grade_name, grade_date):
        '''
        Summit the taske
        :param grade_name: Course Name
        :param grade_date: Course Date(2018-02-04)
        :return:
        '''
        grade_record = common.get_grade_record(grade_name, self.qq, grade_date)

        if grade_record != None:
            grade_record.task_status = 1
            session.commit()
            return True
        else:
            return False

    def get_score(self, grade_name):
        '''
        Check the results
        :param grade_name:
        :return:
        '''
        grade = common.get_grade(grade_name)
        student = common.get_student_by_qq(self.qq)

        if grade != None and student != None:
            grade_record = session.query(
                init_database.GradeRecord
            ).filter(
                init_database.GradeRecord.grade == grade,
                init_database.GradeRecord.student == student,
            ).first()

            if grade_record != None:
                return grade_record.score
        else:
            return None

    def get_rank(self, grade_name):
        '''
        Get the final ranks
        :param grade_name:
        :return:
        '''
        grade = common.get_grade(grade_name)
        student = common.get_student_by_qq(self.qq)

        if grade != None and student != None:
            grade_records = session.query(
                init_database.GradeRecord
            ).filter(
                init_database.GradeRecord.grade == grade
            ).order_by(
                init_database.GradeRecord.score.desc()
            ).all()
            students = list(map(lambda record: record.student, grade_records))

            if student in students:
                rank = students.index(student)
                return rank + 1
        else:
            return None


if __name__ == '__main__':
    s = Student('0123456')
    ret = s.get_score('Math')
    print(ret)
    ret = s.get_rank('Math')
    print(ret)
