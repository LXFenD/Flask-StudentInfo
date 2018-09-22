from flask import Flask, redirect, url_for
from flask_login import LoginManager

import config

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object(config)
login_manager = LoginManager()
login_manager.init_app(app)



@app.route('/')
def index():
    return redirect(url_for('cms.login'))
