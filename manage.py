from app.student.views import student as student_blueprint
from app.cms.views import cms as cms_blueprint
from app import app
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from app.models import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from config import BASEDIR

app.config['SECRET_KEY'] = 'odinhj_123456'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS '] = False
app.config['UPLOAD_FOLDER'] = os.path.join(BASEDIR, 'app', 'static', 'dist', 'img')
Bootstrap(app)
debugs = DebugToolbarExtension(app)
app.register_blueprint(cms_blueprint, url_prefix="/cms")
app.register_blueprint(student_blueprint, url_prefix="/student")

Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
