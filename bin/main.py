#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 19, 2018, 5:53 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.student import Student
from core.teacher import Teacher


def student_view():
    '''
    Student View
    :return:
    '''
    QQ_Number = input('Please input your QQ Number: ').strip()
    student = Student(QQ_Number)  # find the student by function
    stayFlag = True
    while stayFlag:
        print('Welcome to Student System'.center(50, ' '))
        choice = input(
        '''
            1) Hand in the homework;
            2) Check Results;
            3) View Rankings;
            4) Exit the System.
            :
        '''
        ).strip()

        if choice == '1':
            grade_name = input('Grade Name: ')
            grade_date = input('Grade Date(Ex. 2018-02-03): ')
            ret = student.submit_task(grade_name, grade_date)
            print(ret)
        elif choice == '2':
            grade_name = input('Grade Name: ')
            ret = student.get_score(grade_name)
            print(ret)
        elif choice == '3':
            grade_name = input('Grade Name: ')
            ret = student.get_rank(grade_name)
            print(ret)
        elif choice == '4':
            stayFlag = False
        else:
            print('Invalid Options!'.center(50, ' '))


def teacher_view():
    '''
    Teacher's View
    :return:
    '''
    teacher_name = input('Please input your name: ').strip()
    teacher = Teacher(teacher_name)
    stayFlag = True

    while True:
        choice = input(
            '''
                1) Add a Course;
                2) Add Course Records;
                3) Add student to a class;
                4) Modify students' grades;
                5) Exit.
            :
            '''
        ).strip()

        if choice == '1':
            grade_name = input('Course Name: ')
            ret = teacher.add_grade(grade_name)
            print(ret)
        elif choice == '2':
            grade_name = input('Course Name: ').strip()
            ret = teacher.add_grade_record(grade_name)
            print(ret)
        elif choice == '3':
            QQ_Number = input("Please input the Student's QQ Number: ").strip()
            grade_name = input('Course Name: ').strip()
            ret = teacher.add_student_to_grade(QQ_Number, grade_name)
            print(ret)
        elif choice == '4':
            QQ_Number = input("Please input the Student's QQ Number: ").strip()
            grade_name = input('Course Name: ').strip()
            date = input('Course Date(2018-02-20): ').strip()
            score = input('Score: ').strip()
            ret = teacher.modify_score(grade_name, QQ_Number, date, score)
            print(ret)
        elif choice == '5':
            stayFlag = False
        else:
            print('Invalid Options!'.center(50, ' '))


def main():
    '''
    Entry of the programe
    :return: None
    '''
    role = input(
        '''
        Hi,
            Welcome to use the system, you are:
            
            1) Teacher;
            2) Student;
            3) Exit.
        :
        '''
    ).strip()

    if role == '1':
        teacher_view()
    elif role == '2':
        student_view()
    elif role == '3':
        exit('Thanks for using the system.'.center(50, ' '))
    else:
        print('Invalid Options!'.center(50, ' '))


if __name__ == '__main__':
    main()
