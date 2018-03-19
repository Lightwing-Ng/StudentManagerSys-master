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


def get_student_by_qq(student_qq):
    '''
    Get the student's information by QQ number
    :param student_qq:
    :return:
    '''
    student = session.query(
        init_database.Student
    ).filter(
        init_database.Student.qq == student_qq
    ).first()

    return student


def get_grade(grade_name):
    '''
    Get the class's information by Name
    :param grade_name:
    :return:
    '''
    grade = session.query(
        init_database.Grade
    ).filter(
        init_database.Grade.name == grade_name
    ).first()

    return grade


def get_grade_record(grade_name, student_qq, date):
    '''
    Get Course records trough class name, student's QQ and dates.
    :param grade_name:
    :param student_qq:
    :param date:
    :return:
    '''
    grade = get_grade(grade_name)
    student = get_student_by_qq(student_qq)

    if grade != None and student != None:
        grade_record = session.query(
            init_database.GradeRecord
        ).filter(
            init_database.GradeRecord.grade == grade,
            init_database.GradeRecord.student == student,
            init_database.GradeRecord.date == date
        ).first()

        return grade_record
    else:
        return None
