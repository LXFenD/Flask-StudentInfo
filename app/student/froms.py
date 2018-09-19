

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,FileField
from wtforms.validators import Required

class UploadForm(FlaskForm):
    upfiled = FileField('上传文件',validators=[Required(),])
    submit = SubmitField('提交')

