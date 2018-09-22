from wtforms import SubmitField, PasswordField, StringField, BooleanField
from flask_wtf import FlaskForm

from wtforms.validators import Required, Length


class LoginFrom(FlaskForm):

    username = StringField("账号", validators=(Required(),),
                           render_kw={'class': 'form-control', 'placeholder': '用户名/手机/邮件'})
    password = StringField('密码', validators=(Required(), Length(min=6, max=16)),
                           render_kw={'class': 'form-control', 'placeholder': '密码'})
    is_remember = BooleanField('remember',default=False)
    submit = SubmitField('登陆',render_kw={'class':'btn btn-primary btn-block btn-flat','value':'提交'})