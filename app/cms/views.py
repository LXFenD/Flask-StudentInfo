from app.cms import cms
from flask import render_template, abort, Response, flash, url_for, redirect, request, session, jsonify
from app.models import db, User, User_Detail, UserLog, CZ_JD_School, CZ_JD_Department
from app.cms.froms import LoginFrom
from flask_login import login_user, logout_user, login_required
from app import login_manager
from app import app
from flask_wtf import CSRFProtect
import os
from config import UEDITOR_CONFIG_PATH
import json
import re

csrf = CSRFProtect(app)


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


@cms.route('/')
@login_required
def index():
    if request.args.get('teacher'):
        cz = CZ_JD_Department.query.all()
        labels = []
        student_dataes = []
        teacher_dataes = []
        class_dataes = []
        for c in cz:
            labels.append(c.dep_name)
            teacher_dataes.append(c.dep_teacher_num)
            student_dataes.append(c.dep_student_num)
            class_dataes.append(c.dep_class_num)
        return jsonify({'data': {'labels': labels, 'teacher_dataes': teacher_dataes,
                                 'student_dataes': student_dataes, 'class_dataes': class_dataes}})
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


@cms.app_context_processor
def school_detail():
    school = CZ_JD_School.query.first()
    return dict(school=school)


@cms.app_context_processor
def school_detail():
    deps = CZ_JD_Department.query.all()
    return dict(deps=deps)


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


@cms.route('/sch_detail/', methods=['POST'])
@login_required
def sch_detail():
    sch_name = request.form.get('sch_name')
    sch_address = request.form.get('sch_address')
    sch_email = request.form.get('sch_email')
    sch_phone = request.form.get('sch_phone')
    sch_time = request.form.get('sch_time')
    sch_area = request.form.get('sch_area')
    sch_content = request.form.get('sch_content')
    school = CZ_JD_School.query.first()
    dep_num = CZ_JD_Department.query.count()
    if school:
        school.sch_name = sch_name
        school.sch_address = sch_address
        school.sch_buldtime = sch_time
        school.sch_phone = sch_phone
        school.sch_emial = sch_email
        school.sch_areas = int(sch_area)
        school.sch_info = sch_content
        school.sch_dep_num = dep_num
    else:
        school = CZ_JD_School(sch_name=sch_name, sch_phone=sch_phone, sch_info=sch_content, sch_areas=int(sch_area),
                              sch_emial=sch_email, sch_dep_num=dep_num, sch_address=sch_address
                              )
    db.session.add(school)
    db.session.commit()
    return jsonify({'code': 200})


@cms.route('/dep_index/')
@login_required
def dep_index():
    dep_id = request.args.get('dep_id')
    dep_detail  = None
    if dep_id:
        dep_detail = CZ_JD_Department.query.filter_by(id=int(dep_id)).first()

    return render_template('cms/school/dep_index.html',dep_detail=dep_detail)


