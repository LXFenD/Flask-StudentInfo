"""empty message

Revision ID: fa99c176eefe
Revises: 
Create Date: 2018-09-21 22:19:21.034194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa99c176eefe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cz_jd_school',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sch_name', sa.String(length=100), nullable=True),
    sa.Column('sch_address', sa.String(length=255), nullable=True),
    sa.Column('sch_buldtime', sa.DateTime(), nullable=True),
    sa.Column('sch_phone', sa.String(length=11), nullable=True),
    sa.Column('sch_emial', sa.String(length=100), nullable=True),
    sa.Column('sch_areas', sa.Integer(), nullable=True),
    sa.Column('sch_info', sa.Text(), nullable=True),
    sa.Column('sch_dep_num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sch_emial'),
    sa.UniqueConstraint('sch_name'),
    sa.UniqueConstraint('sch_phone')
    )
    op.create_index(op.f('ix_cz_jd_school_sch_buldtime'), 'cz_jd_school', ['sch_buldtime'], unique=False)
    op.create_table('quanxuan',
    sa.Column('quanxian_id', sa.Integer(), nullable=False),
    sa.Column('quanxian_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('quanxian_id'),
    sa.UniqueConstraint('quanxian_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('face_image', sa.String(length=600), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.Column('user_addtime', sa.DateTime(), nullable=True),
    sa.Column('user_ip', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_user_addtime'), 'user', ['user_addtime'], unique=False)
    op.create_table('cz_jd_department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dep_name', sa.String(length=100), nullable=True),
    sa.Column('dep_num', sa.String(length=100), nullable=True),
    sa.Column('dep_level', sa.Integer(), nullable=True),
    sa.Column('dep_buldtime', sa.DateTime(), nullable=True),
    sa.Column('dep_teacher_num', sa.Integer(), nullable=True),
    sa.Column('dep_student_num', sa.BigInteger(), nullable=True),
    sa.Column('dep_class_num', sa.BigInteger(), nullable=True),
    sa.Column('dep_shcs', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dep_shcs'], ['cz_jd_school.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dep_level'),
    sa.UniqueConstraint('dep_name'),
    sa.UniqueConstraint('dep_num')
    )
    op.create_table('user_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_mingyan', sa.String(length=100), nullable=True),
    sa.Column('user_detail', sa.Text(), nullable=True),
    sa.Column('user_age', sa.Integer(), nullable=True),
    sa.Column('user_pro', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('cz_jd_teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teach_name', sa.String(length=100), nullable=True),
    sa.Column('teach_num', sa.String(length=100), nullable=True),
    sa.Column('teach_age', sa.Integer(), nullable=True),
    sa.Column('teach_zhicheng', sa.String(length=100), nullable=True),
    sa.Column('teach_id', sa.String(length=100), nullable=True),
    sa.Column('teach_deps', sa.Integer(), nullable=True),
    sa.Column('teach_face_img', sa.String(length=600), nullable=True),
    sa.Column('teach_shenfen', sa.String(length=18), nullable=True),
    sa.Column('teach_record', sa.String(length=100), nullable=True),
    sa.Column('teach_addschool_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['teach_deps'], ['cz_jd_department.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('teach_id'),
    sa.UniqueConstraint('teach_name'),
    sa.UniqueConstraint('teach_num'),
    sa.UniqueConstraint('teach_shenfen')
    )
    op.create_table('cz_jd_course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cur_id', sa.String(length=100), nullable=True),
    sa.Column('cur_name', sa.String(length=100), nullable=True),
    sa.Column('cur_num', sa.String(length=100), nullable=True),
    sa.Column('cur_time', sa.Integer(), nullable=True),
    sa.Column('cur_teach', sa.Integer(), nullable=True),
    sa.Column('cur_addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cur_teach'], ['cz_jd_teacher.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cur_id'),
    sa.UniqueConstraint('cur_name'),
    sa.UniqueConstraint('cur_num')
    )
    op.create_index(op.f('ix_cz_jd_course_cur_addtime'), 'cz_jd_course', ['cur_addtime'], unique=False)
    op.create_table('cz_jd_profess',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pro_name', sa.String(length=100), nullable=True),
    sa.Column('pro_num', sa.String(length=100), nullable=True),
    sa.Column('pro_info', sa.Text(), nullable=True),
    sa.Column('pro_studentnum', sa.Integer(), nullable=True),
    sa.Column('pro_buildertime', sa.DateTime(), nullable=True),
    sa.Column('pro_teachs', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pro_teachs'], ['cz_jd_teacher.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pro_name'),
    sa.UniqueConstraint('pro_num')
    )
    op.create_table('cz_jd_classinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cl_id', sa.String(length=100), nullable=True),
    sa.Column('cl_name', sa.String(length=100), nullable=True),
    sa.Column('cl_num', sa.String(length=100), nullable=True),
    sa.Column('cl_student_num', sa.Integer(), nullable=True),
    sa.Column('cl_pros', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cl_pros'], ['cz_jd_profess.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cl_id'),
    sa.UniqueConstraint('cl_name'),
    sa.UniqueConstraint('cl_num')
    )
    op.create_table('classes',
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('teach_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['cz_jd_classinfo.id'], ),
    sa.ForeignKeyConstraint(['teach_id'], ['cz_jd_teacher.id'], ),
    sa.PrimaryKeyConstraint('class_id', 'teach_id')
    )
    op.create_table('cz_jd_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stu_name', sa.String(length=100), nullable=True),
    sa.Column('stu_num', sa.String(length=100), nullable=True),
    sa.Column('stu_age', sa.Integer(), nullable=True),
    sa.Column('stu_face_img', sa.String(length=600), nullable=True),
    sa.Column('stu_shenfen', sa.String(length=18), nullable=True),
    sa.Column('stu_pros', sa.Integer(), nullable=True),
    sa.Column('stu_classes', sa.Integer(), nullable=True),
    sa.Column('stu_open_time', sa.DateTime(), nullable=True),
    sa.Column('stu_close_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stu_classes'], ['cz_jd_classinfo.id'], ),
    sa.ForeignKeyConstraint(['stu_pros'], ['cz_jd_profess.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stu_name'),
    sa.UniqueConstraint('stu_num'),
    sa.UniqueConstraint('stu_shenfen')
    )
    op.create_index(op.f('ix_cz_jd_student_stu_close_time'), 'cz_jd_student', ['stu_close_time'], unique=False)
    op.create_index(op.f('ix_cz_jd_student_stu_open_time'), 'cz_jd_student', ['stu_open_time'], unique=False)
    op.create_table('CZ_JD__stu__sushe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sushe_name', sa.String(length=100), nullable=True),
    sa.Column('sushe_num_id', sa.String(length=20), nullable=True),
    sa.Column('sueshe_stu', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sueshe_stu'], ['cz_jd_student.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sushe_num_id')
    )
    op.create_table('CZ_JD__stu__weigui',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weigui_name', sa.String(length=100), nullable=True),
    sa.Column('weigui_num_id', sa.String(length=20), nullable=True),
    sa.Column('weigui_stu', sa.Integer(), nullable=True),
    sa.Column('weigui_info', sa.Text(), nullable=True),
    sa.Column('weigui_chongfa', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['weigui_stu'], ['cz_jd_student.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('weigui_num_id')
    )
    op.create_table('courses',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['cz_jd_course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['cz_jd_student.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    op.create_table('user_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('userlog_ip', sa.String(length=100), nullable=True),
    sa.Column('userlog_addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['cz_jd_student.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['cz_jd_teacher.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_log_userlog_addtime'), 'user_log', ['userlog_addtime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_log_userlog_addtime'), table_name='user_log')
    op.drop_table('user_log')
    op.drop_table('courses')
    op.drop_table('CZ_JD__stu__weigui')
    op.drop_table('CZ_JD__stu__sushe')
    op.drop_index(op.f('ix_cz_jd_student_stu_open_time'), table_name='cz_jd_student')
    op.drop_index(op.f('ix_cz_jd_student_stu_close_time'), table_name='cz_jd_student')
    op.drop_table('cz_jd_student')
    op.drop_table('classes')
    op.drop_table('cz_jd_classinfo')
    op.drop_table('cz_jd_profess')
    op.drop_index(op.f('ix_cz_jd_course_cur_addtime'), table_name='cz_jd_course')
    op.drop_table('cz_jd_course')
    op.drop_table('cz_jd_teacher')
    op.drop_table('user_detail')
    op.drop_table('cz_jd_department')
    op.drop_index(op.f('ix_user_user_addtime'), table_name='user')
    op.drop_table('user')
    op.drop_table('quanxuan')
    op.drop_index(op.f('ix_cz_jd_school_sch_buldtime'), table_name='cz_jd_school')
    op.drop_table('cz_jd_school')
    # ### end Alembic commands ###