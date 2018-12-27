# -*- coding: utf-8 -*-


from flask import Blueprint, request, current_app, g, abort
import json
from ..models import (db, tb_course_student,
                      tb_major, tb_mechmism, tb_student,
                      tb_class, tb_teacher, tb_reservation,
                      tb_course, tb_exam_table, tb_classroom_table)
from sqlalchemy import desc, exc, asc
from datetime import datetime
from flask.views import MethodView
from ..utildef import wrap_jsonify, to_dict


main = Blueprint('main', __name__)


class Tb_courseAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_course.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_course(**data)
        db.session.add(course)
        db.session.commit()

        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_course.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)

        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_course
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_course_view = wrap_jsonify(Tb_courseAPI.as_view('tb_course_api'))

main.add_url_rule('/tb_course',
                  view_func=tb_course_view,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_course_studentAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_course_student.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_course_student(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_course_student.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)

        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_course_student
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_course_studentview = wrap_jsonify(Tb_course_studentAPI
                                     .as_view('tb_course_studentapi'))

main.add_url_rule('/tb_course_student',
                  view_func=tb_course_studentview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_majorAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_major.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_major(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_major.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_major
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_majorview = wrap_jsonify(Tb_majorAPI
                            .as_view('tb_majorapi'))

main.add_url_rule('/tb_major',
                  view_func=tb_majorview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_mechmismAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_mechmism.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_mechmism(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_mechmism.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_mechmism
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_mechmismview = wrap_jsonify(Tb_mechmismAPI
                               .as_view('tb_mechmismapi'))

main.add_url_rule('/tb_mechmism',
                  view_func=tb_mechmismview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_studentAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_student.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_student(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_student.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_student
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_studentview = wrap_jsonify(Tb_studentAPI
                              .as_view('tb_studentapi'))

main.add_url_rule('/tb_student',
                  view_func=tb_studentview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_classAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_class.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_class(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_class.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_class
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_classview = wrap_jsonify(Tb_classAPI
                            .as_view('tb_classapi'))

main.add_url_rule('/tb_class',
                  view_func=tb_classview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_teacherAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_teacher.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_teacher(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_teacher.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_teacher
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_teacherview = wrap_jsonify(Tb_teacherAPI
                              .as_view('tb_teacherapi'))

main.add_url_rule('/tb_teacher',
                  view_func=tb_teacherview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])


class Tb_reservationAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_reservation.query.filter_by(**data).all()

        if courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_reservation(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_reservation.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_reservation
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_reservationview = wrap_jsonify(Tb_reservationAPI
                                  .as_view('tb_reservationapi'))

main.add_url_rule('/tb_reservation',
                  view_func=tb_reservationview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])

				  
class Tb_classroom_tableAPI(MethodView):

    def get(self):

        data = request.args.to_dict()
        mode = data["mode"]
        new_courses =[]
        if  mode=='1':
            day = data["day"]
            time = data["time"]
            number = int(data["number"])
            courses = tb_classroom_table.query.filter(tb_classroom_table.number>=number).all()
            courses = [to_dict(c) for c in courses]
            for item in courses:
                if  time not in item[day]:
                    new_item = {'course_name':item['course_name'],'number':item['number']}
                    new_courses.append(new_item)     
        if mode=='0':
            course_name = data['course_name']
            day = data['day']
            time = data['time']
            courses = tb_classroom_table.query.filter(tb_classroom_table.course_name==course_name).all()
            courses = [to_dict(c) for c in courses]
            for item in courses:
                if  time not in item[day]:
                    return  {'result':1}
                else:
                    return {'result':0}
        if  new_courses is None:
            return []
        else:
            return new_courses#[to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_classroom_table(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_classroom_table.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_classroom_table
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_classroom_tableview = wrap_jsonify(Tb_classroom_tableAPI
                              .as_view('tb_classroom_tableapi'))

main.add_url_rule('/tb_classroom_table',
                  view_func=tb_classroom_tableview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])



class Tb_exam_tableAPI(MethodView):

    def get(self):
        data = request.args.to_dict()
        courses = tb_exam_table.query.filter_by(**data).all()

        if  courses is None:
            return []
        else:
            return [to_dict(c) for c in courses]

    def put(self):
        data = json.loads(request.data)
        course = tb_exam_table(**data)
        db.session.add(course)
        db.session.commit()
        return 'ok'

    def delete(self):
        data = json.loads(request.data)
        courses = tb_exam_table.query.filter_by(**data).all()
        if not courses:
            return '空'
        for c in courses:
            db.session.delete(c)
        db.session.commit()

        return 'ok'

    def post(self):
        data = json.loads(request.data)
        filter_data = json.loads(data['filter'])
        update_data = json.loads(data['update'])
        (tb_exam_table
         .query
         .filter_by(**filter_data)
         .update(update_data))
        db.session.commit()

        return 'ok'


tb_exam_tableview = wrap_jsonify(Tb_exam_tableAPI
                              .as_view('tb_exam_tableapi'))

main.add_url_rule('/tb_exam_table',
                  view_func=tb_exam_tableview,
                  methods=['GET', 'PUT', 'DELETE', 'POST'])