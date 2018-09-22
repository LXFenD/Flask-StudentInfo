
from app.student import student
from flask import render_template, request, redirect, url_for,jsonify
from app.student.froms import UploadForm
import os
from app import app


@student.route('/index/')
def index():
    return render_template('stuinfo/stuinfo_index.html')


@student.route('/404')
def index_404():
    return render_template('common/404.html')


@student.route('/500')
def index_500():
    return render_template('common/500.html')


@student.errorhandler(404)
def get_page_found(e):
    return render_template('common/404.html')

@student.errorhandler(500)
def get_page_found(e):
    return render_template('common/500.html')


@student.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        form.upfiled.data.save(os.path.join(app.config['UPLOAD_FOLDER'], form.upfiled.data.filename))
        return redirect(url_for('student.index'))
    return render_template('cms/common/upload.html', form=form)

@student.route('/video/')
def video():
    return render_template('cms/common/video.html')

