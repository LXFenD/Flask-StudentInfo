
from app.student import student
from flask import render_template,request,redirect,url_for
from app.student.froms import UploadForm
import os
from  app import app
from aliyunsdkvod.request.v20170321 import GetVideoPlayAuthRequest
# -*- coding: UTF-8 -*-
import json
from aliyunsdkcore import client
from aliyunsdkvod.request.v20170321 import GetPlayInfoRequest


def init_vod_client(accessKeyId, accessKeySecret):
    """
    初始化客户端
    :param accessKeyId:
    :param accessKeySecret:
    :return:
    """
    regionId = 'cn-shanghai'
    connectTimeout = 10
    return client.AcsClient(accessKeyId, accessKeySecret, regionId, auto_retry=True, max_retry_time=3, timeout=connectTimeout)

def get_video_playauth(clt, videoId):
    """
    获取播放凭证
    :param clt:
    :param videoId:
    :return:
    """
    request = GetVideoPlayAuthRequest.GetVideoPlayAuthRequest()
    request.set_accept_format('JSON')
    request.set_VideoId(videoId)
    request.set_AuthInfoTimeout(3600)    # 播放凭证过期时间，默认为100秒，取值范围100~3600；注意：播放凭证用来传给播放器自动换取播放地址，凭证过期时间不是播放地址的过期时间
    response = json.loads(clt.do_action(request))
    return response

def get_play_info(clt, videoId):
    """

    :param clt:
    :param videoId:
    :return:
    """
    request = GetPlayInfoRequest.GetPlayInfoRequest()
    request.set_accept_format('JSON')
    request.set_VideoId(videoId)
    request.set_AuthTimeout(3600*24)
    response = json.loads(clt.do_action(request))
    return response


@student.route('/index/')
def index():
    return  render_template('cms/base.html')

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

@student.route('/',methods=['GET','POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        form.upfiled.data.save(os.path.join(app.config['UPLOAD_FOLDER'],form.upfiled.data.filename))
        return redirect(url_for('student.index'))
    return  render_template('cms/upload.html', form=form)



@student.route('/video/')
def video():
    # clt = init_vod_client('LTAIyS9RFbHA4WFI', '<您的AccessKeySecret>')
    # playInfo = get_video_playauth(clt, 'cd85167814774b55a61dd12214f9dfe2')
    # data  = json.dumps(playInfo, ensure_ascii=False, indent=4)
    # data = eval(data)
    return render_template('cms/video.html')


