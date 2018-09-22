from app.cms import cms
from flask import render_template, abort, Response, flash, url_for, redirect, request, session, jsonify
from app.models import db, User, User_Detail, UserLog
from app.cms.froms import LoginFrom
from flask_login import login_user, logout_user, login_required
from app import login_manager
from app import app
from flask_wtf import CSRFProtect
import os
from config import BASEDIR, UEDITOR_CONFIG_PATH
import json
import re

csrf = CSRFProtect(app)


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


@cms.route('/')
@login_required
def index():
    print(session.get('user_id'))
    return render_template('cms/common/index.html')


@cms.route('/school_info/')
@login_required
def school_info():
    """
    详情页面
    """
    return render_template('cms/school/sch_cms_index.html')


@cms.route('/login/', methods=['GET', 'POST'])
def login():
    """
    登录系统
    """
    form = LoginFrom()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        is_remember = form.is_remember.data
        user = User.query.filter_by(phone=username, password=password).first()
        next = request.args.get('next')
        if user and is_remember:
            login_user(user, remember=True)
            flash("登陆成功")
            ip = request.remote_addr
            print(ip)
            user_log = UserLog(user_id=session.get('user_id'), userlog_ip=ip)
            db.session.add(user_log)
            db.session.commit()
            return redirect(next or url_for('cms.index'))
        elif user and is_remember == False:
            login_user(user)
            flash("登陆成功")
            ip = request.remote_addr
            print(ip)
            user_log = UserLog(user_id=session.get('user_id'), userlog_ip=ip)
            db.session.add(user_log)
            db.session.commit()
            return redirect(next or url_for('cms.index'))
            flash("登陆成功")
        else:
            abort(400)
    else:
        print(form.errors)
        return render_template('cms/common/login.html', form=form)


@cms.route('/login_out/')
@login_required
def login_out():
    """
    退出系统
    """
    logout_user()
    return redirect(url_for('cms.login'))


@cms.route('/myself/')
@login_required
def myself():
    value = request.args.get('value')
    if value:
        detail = User_Detail.query.filter_by(user_id=session.get('user_id')).first()
        detail.user_mingyan = value
        db.session.add(detail)
        db.session.commit()
        return jsonify({'data': {'value': value}})
    return render_template('cms/common/myself.html')


@cms.route('/upload_file/', methods=['POST'])
@login_required
def upload_file():
    up_img = request.files.get('file')
    url = 'http://127.0.0.1:8081/static/dist/img/' + up_img.filename
    if up_img:
        up_img.save(os.path.join(app.config['UPLOAD_FOLDER'], up_img.filename))
        user = User.query.filter_by(id=session.get('user_id')).first()
        user.face_image = url
        db.session.add(user)
        db.session.commit()
    return jsonify({'data': {'url': url}})


@cms.app_context_processor
def user_face_img():
    user = User.query.filter_by(id=session.get('user_id')).first()
    return dict(users=user)


@cms.app_context_processor
def user_face_img():
    detail = User_Detail.query.filter_by(user_id=session.get('user_id')).first()
    return dict(detail=detail)


def _get_config():
    """

    读取上传配置文件
    :return:
    """
    with open(UEDITOR_CONFIG_PATH, 'r', encoding='utf-8') as fp:
        result = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        return result


@csrf.exempt
@cms.route('/editor/', methods=['GET', 'POST'])
def editor():
    """
    富文本
    :return:
    """
    action = request.args.get('action')
    if action == 'config':
        """
        返回配置文件
        """
        return jsonify(_get_config())
    elif action in ['uploadimage', 'uploadvideo', 'uploadfile']:
        """
        上传文件并在编辑器上显示
        """
        file = request.files.get('upfile')
        filename = file.filename
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        url = url_for('cms.send_file', filename=filename)
        """
            富文本返回指定的json数据    
        """
        return jsonify({'state': 'SUCCESS', 'url': url, 'title': filename, 'original': filename})
    else:
        return jsonify({'state': 'FAIL', 'url': None, 'title': None, 'original': None})


@cms.route('/f/<filename>', methods=['get', 'post'])
def send_file(filename):
    """
    富文本会回调上传的json中url地址
    把上传的图片显示在富文本中
    :param filename:
    :return:
    """
    fp = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb')
    response = Response(fp)
    response.headers['Content-Type'] = 'application/octet-stream'
    return response


@cms.route('/up_detail/')
@login_required
def up_detail():
    content = request.args.get('detail')
    if content:
        detail = User_Detail.query.filter_by(user_id=session.get('user_id')).first()
        detail.user_detail = content
        db.session.add(detail)
        db.session.commit()
        return jsonify({'code': 200})
    else:
        return jsonify({'code': 400})
