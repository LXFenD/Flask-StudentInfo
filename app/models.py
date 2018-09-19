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
    id = db.Column(db.Integer, primary_key=True)  # id
    teach_name = db.Column(db.String(100), unique=True)  # 教师名称
    teach_age = db.Column(db.Integer)  # 教师年龄
    teach_zhicheng = db.Column(db.String(100))  # 教师职称
    teach_id = db.Column(db.String(100), unique=True)  # 教师的编号
    teach_deps = db.Column(db.ForeignKey('cz_jd_department.id'))  # 教师的职业技能
    teach_record = db.Column(db.String(100))  # 教师的学历
    teach_addschool_time = db.Column(db.DateTime, default=None)  # 当教师的时间
    teach_profess = db.relationship('CZ_JD_Profess', backref='cz_jd_teacher')  # 教师的学历
    classes = db.relationship('CZ_JD_Classinfo', secondary=classes, backref='cz_jd_teacher')  # 教师所教 的班级
    teach_cur = db.relationship('CZ_JD_Course', backref='cz_jd_teacher')  # 教师所教的课程


class CZ_JD_Profess(db.Model):
    """
    专业信息表
    """
    __tablename__ = 'cz_jd_profess'
    id = db.Column(db.Integer, primary_key=True)  # id
    pro_name = db.Column(db.String(100), unique=True)  # 专业的名称
    pro_info = db.Column(db.Text)  # 专业的信息
    pro_studentnum = db.Column(db.Integer)  # 专业的学生人数
    pro_buildertime = db.Column(db.DateTime, default=None)  # 专业的建立时间
    pro_teachs = db.Column(db.ForeignKey('cz_jd_teacher.id'))  # 此专业的老师
    pro_classinfos = db.relationship('CZ_JD_Classinfo', backref='cz_jd_profess')  # 此专业专业的班级
    pro_stu = db.relationship('CZ_JD_Student', backref='cz_jd_profess')  # 此专业的学生

class CZ_JD_Classinfo(db.Model):
    """
    班级信息表
    """
    __tablename__ = 'cz_jd_classinfo'
    id = db.Column(db.Integer, primary_key=True)  # id
    cl_id = db.Column(db.String(100), unique=True)  # 班级的编号
    cl_name = db.Column(db.String(100), unique=True)  # 班级的名称
    cl_student_num = db.Column(db.Integer)  # 班级的学生人数
    cl_pros = db.Column(db.ForeignKey("cz_jd_profess.id"))  # 班级的专业
    cl_stu = db.relationship('CZ_JD_Student', backref='cz_jd_classinfo')

"""
课程和学生的之间的多对多关系
"""
courses = db.Table('course',
                   db.Column('student_id', db.Integer, db.ForeignKey('cz_jd_student.id'), primary_key=True),
                   db.Column('course_id', db.Integer, db.ForeignKey('cz_jd_course.id'), primary_key=True),
                   )

class CZ_JD_Course(db.Model):
    """
    课程信心表
    """
    __tablename__ = "cz_jd_course"
    id = db.Column(db.Integer, primary_key=True)
    cur_id = db.Column(db.String(100), unique=True)  # 课程的编号
    cur_name = db.Column(db.String(100), unique=True)  # 课程的名称
    cur_time = db.Column(db.Integer)  # 课程的必修课时
    cur_teach = db.Column(db.ForeignKey('cz_jd_teacher.id'))  # 课程的老师
    cur_addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 课程的添加的时间
    courses = db.relationship('CZ_JD_Student', secondary='courses', backref='cz_jd_course')

class CZ_JD_Student(db.Model):
    """
    学生信息表
    """
    __tablename__ = 'cz_jd_student'
    id = db.Column(db.Integer, primary_key=True)
    stu_name = db.Column(db.String(100), unique=True)  # 学生的姓名
    stu_age = db.Column(db.Integer)  # 学生的年龄
    stu_pros = db.Column(db.ForeignKey('cz_jd_profess.id'))  # 学生的专业
    stu_classes = db.Column(db.ForeignKey('cz_jd_classinfo.id'))  # 学生的班级
    stu_open_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 学生的入学时间
    stu_close_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 学生的毕业时间
