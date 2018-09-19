
from app.student import student
from flask import render_template

@student.route('/')
def index():
    return  render_template('cms/index.html')

@student.route('/404')
def index_404():
    return  render_template('common/404.html')

@student.route('/500')
def index_500():
    return  render_template('common/500.html')

@student.errorhandler(404)
def get_page_found(e):
    return render_template('common/404.html')

@student.errorhandler(500)
def get_page_found(e):
    return render_template('common/500.html')
