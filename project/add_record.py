# -*- coding: utf-8 -*-

from project.models import (db, tb_teacher, tb_class, tb_course)
from datetime import datetime, timedelta
from sqlalchemy import and_


from project import create_app

app = create_app()

app.app_context().push()

courses = tb_course.query.all()

for c in courses:
    _class = tb_class.query.filter_by(class_room=c.class_room).first()
    if _class is None:
        _class = tb_class(class_room=c.class_room)
        db.session.add(_class)
    _teacher = tb_teacher.query.filter_by(teacher=c.teacher).first()
    if _teacher is None:
        _teacher = tb_teacher(teacher=c.teacher)
        db.session.add(_teacher)

db.session.commit()
