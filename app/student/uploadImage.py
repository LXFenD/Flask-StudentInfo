# -*- coding: UTF-8 -*-
from app.voduploadsdk.AliyunVodUtils import *
from app.voduploadsdk.AliyunVodUploader import AliyunVodUploader
from app.voduploadsdk.UploadImageRequest import UploadImageRequest

# 测试上传本地图片
def testUploadLocalImage(accessKeyId, accessKeySecret, filePath):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadImageRequest = UploadImageRequest(filePath)
        uploadImageRequest.setImageType('cover')        # 设置图片使用类型为封面，默认为default
        uploadImageRequest.setTitle('test upload local image')  # 设置图片标题，默认为空
        imageId, imageUrl = uploader.uploadImage(uploadImageRequest, True)
        print( "file: %s, imageId: %s, imageUrl: %s" % (uploadImageRequest.filePath, imageId, imageUrl))
        
    except AliyunVodException as e:
        print(e)

# 测试上传网络图片
def testUploadWebImage(accessKeyId, accessKeySecret, fileUrl):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadImageRequest = UploadImageRequest(fileUrl)
        uploadImageRequest.setImageType('cover')        # 设置图片使用类型为封面，默认为default
        uploadImageRequest.setTitle('test upload web image')  # 设置图片标题，默认为空
        imageId, imageUrl = uploader.uploadImage(uploadImageRequest, False)
        print ("file: %s, imageId: %s, imageUrl: %s" % (uploadImageRequest.filePath, imageId, imageUrl))
        
    except AliyunVodException as e:
        print (e)

####  执行测试代码   ####   
accessKeyId = '<您的AccessKeyId>'
accessKeySecret = '<您的AccessKeySecret>'

localFilePath = '/Users/hufan/Desktop/Image/sample.jpg'
testUploadLocalImage(accessKeyId, accessKeySecret, localFilePath)

fileUrl = 'http://vod-test2.cn-shanghai.aliyuncs.com/snapshot/952706d113674569883a243a655e7ed800002.jpg'
testUploadWebImage(accessKeyId, accessKeySecret, fileUrl)

        

