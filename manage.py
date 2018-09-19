from app.student.views import student as student_blueprint
from app import app
from flask_debugtoolbar import DebugToolbarExtension


import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'odinhj_123456'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////{0}/sutdentinfo.sqlite3".format(BASEDIR)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
debugs = DebugToolbarExtension(app)
app.register_blueprint(student_blueprint)



