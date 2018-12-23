# -*- coding: utf-8 -*-

import forgery_py
from project.models import (db, tb_teacher)

from project import create_app

app = create_app()

app.app_context().push()

reservation = tb_teacher.query.all()

for r in reservation:
    r.email = forgery_py.internet.email_address()

db.session.commit()
