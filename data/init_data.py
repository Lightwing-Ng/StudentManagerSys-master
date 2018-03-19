#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 19, 2018, 5:55 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import sys, os, datetime, random, string, time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from sqlalchemy.orm import sessionmaker
from data import init_database

Session = sessionmaker(init_database.engine)
session = Session()  # Instantiate a session


def get_qq():
    '''
    Generate 6-bit random numbers of QQ number
    :return:
    '''
    nums = string.digits
    QQ = ''.join(random.sample(nums, 6))

    return QQ


def get_time():
    '''
    Get the local time when running
    :return:
    '''
    return datetime.datetime.now()


def get_date_from_str(string):
    '''
    Get the real time by a string input
    :param string:
    :return:
    '''

    return datetime.date(string)


def init_data():
    '''
    Initialize the database
    :return:
    '''

    student_1 = init_database.Student(
        name='Tom', qq=get_qq()
    )
    student_2 = init_database.Student(
        name='Jack', qq=get_qq()
    )
    student_3 = init_database.Student(
        name='Jimi', qq=get_qq()
    )
    student_4 = init_database.Student(
        name='Ben', qq=get_qq()
    )
    student_5 = init_database.Student(
        name='Jone', qq=get_qq()
    )

    teacher_1 = init_database.Teacher(
        name='Sir Lee'
    )
    teacher_2 = init_database.Teacher(
        name='Sir Wong'
    )
    teacher_3 = init_database.Teacher(
        name='Sir Park'
    )

    grade_1 = init_database.Grade(
        name='Chinese'
    )
    grade_2 = init_database.Grade(
        name='Math'
    )
    grade_3 = init_database.Grade(
        name='English'
    )

    grade_record_1 = init_database.GradeRecord(
        grade=grade_1,
        student=student_1,
        date=get_time()
    )
    grade_record_2 = init_database.GradeRecord(
        grade=grade_1,
        student=student_2,
        date=get_time()
    )
    grade_record_3 = init_database.GradeRecord(
        grade=grade_3,
        student=student_3,
        date=get_time()
    )

    session.add_all(
        [student_1, student_2, student_3, student_4, student_5]
    )
    session.add_all(
        [teacher_1, teacher_2, teacher_3]
    )
    session.add_all(
        [grade_1, grade_2, grade_3]
    )
    session.add_all(
        [grade_record_1, grade_record_2, grade_record_3]
    )

    session.commit()
    print('The database is initialized.'.center(50, ' '))

if __name__ == '__main__':
    init_data()
    session.close()
