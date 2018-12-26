# -*- coding: utf-8 -*-

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
from flask import current_app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy import func, case, or_
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from math import sin, cos, sqrt, atan2, radians
from sqlalchemy import desc, exc, asc


db = SQLAlchemy()


class Mybase():

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class tb_course(db.Model, Mybase):
    __tablename__ = 'tb_course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.String(255), index=True)
    type = db.Column(db.String(255))
    course_name = db.Column(db.String(255))
    teacher = db.Column(db.String(255))
    credit = db.Column(DOUBLE)
    duration = db.Column(db.String(255))
    sun = db.Column(db.String(255))
    mon = db.Column(db.String(255))
    tues = db.Column(db.String(255))
    wed = db.Column(db.String(255))
    thur = db.Column(db.String(255))
    fri = db.Column(db.String(255))
    sat = db.Column(db.String(255))
    material = db.Column(db.String(255))
    semester_id = db.Column(db.String(255))
    class_room = db.Column(db.String(255))
    limit_id = db.Column(db.Integer)
    all_degree = db.Column(db.Integer)
    already_degree = db.Column(db.Integer)
    remarks = db.Column(db.String(255))
    machmism_id = db.Column(db.Integer)


class tb_class(db.Model, Mybase):
    __tablename__ = 'tb_class'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_room = db.Column(db.String(255))


class tb_teacher(db.Model, Mybase):
    __tablename__ = 'tb_teacher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher = db.Column(db.String(255))
    email = db.Column(db.String(255))


class tb_reservation(db.Model, Mybase):
    __tablename__ = 'tb_reservation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.String(255), index=True)
    user_id = db.Column(db.String(255), index=True)
    submit_date = db.Column(db.DateTime)
    jieshu = db.Column(db.String(255))
    reason = db.Column(db.String(255))
    status = db.Column(db.String(255))



class tb_course_student(db.Model, Mybase):
    __tablename__ = 'tb_course_student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.String(255), index=True)
    student_id = db.Column(db.String(255), index=True)
    chosen_date = db.Column(db.DateTime)
    priority = db.Column(db.String(255))
    order_x = db.Column(db.String(255))


class tb_major(db.Model, Mybase):
    __tablename__ = 'tb_major'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    major_name = db.Column(db.String(255))


class tb_mechmism(db.Model, Mybase):
    __tablename__ = 'tb_mechmism'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mechmism_name = db.Column(db.String(255))
    mechmism_id = db.Column(db.Integer)


class tb_student(db.Model, Mybase):
    __tablename__ = 'tb_student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_name = db.Column(db.String(255))
    student_id = db.Column(db.String(255), index=True)
    sex = db.Column(db.String(255))
    major = db.Column(db.String(255))
    grade = db.Column(db.Integer)
    dormitory = db.Column(db.String(255))
    telephone = db.Column(db.String(11))
    birthday = db.Column(db.DateTime)
    pinyin = db.Column(db.String(255))
	
class tb_exam_table(db.Model,Mybase):
    __tablename__='tb_exam_table'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(255))
    day = db.Column(db.String(255))
    week = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(255))
    class_room = db.Column(db.String(255))

class tb_classroom_table(db.Model,Mybase):
    __tablename__='tb_classroom_table'
    course_name = db.Column(db.String(255),primary_key=True,autoincrement=True)
    sun = db.Column(db.String(255))
    mon = db.Column(db.String(255))
    tues = db.Column(db.String(255))
    wed = db.Column(db.String(255))
    thur = db.Column(db.String(255))
    fri = db.Column(db.String(255))
    sat = db.Column(db.String(255))
    number = db.Column(db.Integer)