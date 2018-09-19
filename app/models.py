from flask_sqlalchemy import SQLAlchemy
from app import app
from config import BASEDIR
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/studentinfo"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

"""
学院相关的表数据
"""


class CZ_JD_School(db.Model):
    """
    学校的主体信息表
    """
    __tablename__ = "cz_jd_school"
    id = db.Column(db.Integer, primary_key=True)  # ID
    sch_name = db.Column(db.String(100), unique=True)  # 学院名称
    sch_address = db.Column(db.String(255))  # 学院地址
    sch_buldtime = db.Column(db.DateTime, index=True, default=None)  # 建校时间
    sch_phone = db.Column(db.String(11), unique=True)  # 学校的电话
    sch_emial = db.Column(db.String(100), unique=True)  # 学院的电子邮件
    sch_areas = db.Column(db.Integer)  # 学校的占地面积
    sch_info = db.Column(db.Text)  # 学校的信心
    sch_dep_num = db.Column(db.Integer)  # 院系的数量
    sch_deps = db.relationship('CZ_JD_Department', backref='cz_jd_school')


"""
各院系的数据表
"""


class CZ_JD_Department(db.Model):
    """
    院系数据表
    """
    __tablename__ = 'cz_jd_department'
    id = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(100), unique=True)  # 院系的名称
    dep_level = db.Column(db.Integer, unique=True)  # 院系的级别
    dep_buldtime = db.Column(db.DateTime, default=None)  # 院系成立的时间
    dep_teacher_num = db.Column(db.Integer)  # 教师的的人数
    dep_student_num = db.Column(db.BigInteger)  # 学生数量
    dep_class_num = db.Column(db.BigInteger)  # 班级数量
    dep_shcs = db.Column(db.ForeignKey('cz_jd_school.id'))  # 所属学校
    dep_teachs = db.relationship('CZ_JD_Teacher', backref="cz_jd_department")


"""
    班级和老师多对多关联
"""
classes = db.Table('classes',
                   db.Column('class_id', db.Integer, db.ForeignKey('cz_jd_classinfo.id'), primary_key=True),
                   db.Column('teach_id', db.Integer, db.ForeignKey('cz_jd_teacher.id'), primary_key=True),
                   )

class CZ_JD_Teacher(db.Model):
    """
    教师信息表
    """
    __tablename__ = "cz_jd_teacher"
    id = db.Column(db.Integer, primary_key=True)
    teach_name = db.Column(db.String(100), unique=True)
    teach_age = db.Column(db.Integer)
    teach_deps = db.Column(db.ForeignKey('cz_jd_department.id'))
    teach_record = db.Column(db.String(100))
    teach_addschool_time = db.Column(db.DateTime, default=None)
    teach_profess = db.relationship('CZ_JD_Profess', backref='cz_jd_teacher')
    classes = db.relationship('CZ_JD_Classinfo', secondary=classes, backref='cz_jd_teacher')
    teach_cur = db.relationship('CZ_JD_Course',backref = 'cz_jd_teacher')

class CZ_JD_Profess(db.Model):
    """
    专业信息表
    """
    __tablename__ = 'cz_jd_profess'
    id = db.Column(db.Integer, primary_key=True)
    pro_name = db.Column(db.String(100), unique=True)
    pro_info = db.Column(db.Text)
    pro_studentnum = db.Column(db.Integer)
    pro_buildertime = db.Column(db.DateTime, default=None)
    pro_teachs = db.Column(db.ForeignKey('cz_jd_teacher.id'))
    pro_classinfos = db.relationship('CZ_JD_Classinfo', backref='cz_jd_profess')


class CZ_JD_Classinfo(db.Model):
    """
    班级信息表
    """
    __tablename__ = 'cz_jd_classinfo'
    id = db.Column(db.Integer, primary_key=True)
    cl_name = db.Column(db.String(100), unique=True)
    cl_student_num = db.Column(db.Integer)
    cl_pros = db.Column(db.ForeignKey("cz_jd_profess.id"))



class CZ_JD_Course(db.Model):
    """
    课程信心表
    """
    __tablename__ = "cz_jd_course"
    id = db.Column(db.Integer,primary_key=True)
    cur_name = db.Column(db.String(100),unique=True)
    cur_time = db.Column(db.Integer)
    cur_teach =  db.Column(db.ForeignKey('cz_jd_teacher.id'))
    cur_addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow)


