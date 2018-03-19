#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 19, 2018, 5:55 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import sys, os

from sqlalchemy import Integer, String, DATE, Column, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The absolute path of the database
engine = create_engine('sqlite:///%s/data/database.db' % BASE_DIR)

BASE = declarative_base()


class Teacher(BASE):
    __tablename__ = 'teachers'
    id = Column(
        Integer, primary_key=True, autoincrement=True
    )
    name = Column(String(32))

    def ____repr__(self):
        return '%s | %s' % (self.id, self.name)


class GradeRecord(BASE):
    __tablename__ = 'grade_records'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    grade_id = Column(
        Integer, ForeignKey('grades.id')
    )
    stu_id = Column(
        Integer, ForeignKey('students.id')
    )
    date = Column(DATE)
    task_status = Column(Integer, default=0)
    score = Column(Integer, default=0)

    # One-to-many Relational Tables
    grade = relationship(
        'Grade',
        foreign_keys=[grade_id],
        backref='grade_records',
    )
    student = relationship(
        'Student',
        foreign_keys=[stu_id],
        backref='grade_records'
    )

    def __repr__(self):
        return '%s | %s | %s | %s | %s | %s' % (
            self.id,
            self.grade.name,
            self.student.name,
            self.date,
            self.task_status,
            self.score
        )


class Student(BASE):
    __tablename__ = 'students'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(32))
    qq = Column(String(32))

    def __repr__(self):
        return '%s | %s | %s' % (
            self.id,
            self.name,
            self.qq
        )


# Create a Relationship table, connecting grade and student
grade2student = Table(
    'grade2student',
    BASE.metadata,
    Column(
        'grade_id',
        Integer,
        ForeignKey('grades.id')
    ),
    Column(
        'student_id',
        Integer,
        ForeignKey('students.id')
    )
)


class Grade(BASE):
    __tablename__ = 'grades'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(32), unique=True)

    # Add a many-to-many relational tables
    students = relationship(
        'Student',
        secondary=grade2student,
        backref='grades'
    )

    def __repr__(self):
        return '%s | %s' % (
            self.id, self.name
        )

if __name__ == '__main__':
    BASE.metadata.create_all(engine)
    print('The database is initialized.'.center(50, ' '))