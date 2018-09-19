# -*- coding: UTF-8 -*-
from app.voduploadsdk.AliyunVodUtils import *
from app.voduploadsdk.AliyunVodUploader import AliyunVodUploader
from app.voduploadsdk.UploadVideoRequest import UploadVideoRequest


# 测试上传本地视频
def testUploadLocalVideo(accessKeyId, accessKeySecret, filePath, storageLocation=None):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(filePath, 'test upload local video')
        # 可以设置视频封面，如果是本地或网络图片可使用UploadImageRequest上传图片到点播，获取到ImageURL
        # uploadVideoRequest.setCoverURL('https://sample.com/sample.jpg')
        # uploadVideoRequest.setTags('test1,test2')
        if storageLocation:
            uploadVideoRequest.setStorageLocation(storageLocation)
        videoId = uploader.uploadLocalVideo(uploadVideoRequest)

        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))

    except AliyunVodException as e:
        print(e)


# 测试上传网络视频
def testUploadWebVideo(accessKeyId, accessKeySecret, fileUrl, storageLocation=None):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(fileUrl, 'test upload web video')
        uploadVideoRequest.setTags('test1,test2')
        if storageLocation:
            uploadVideoRequest.setStorageLocation(storageLocation)
        videoId = uploader.uploadWebVideo(uploadVideoRequest)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))

    except AliyunVodException as e:
        print(e)


# 测试上传m3u8本地视频
def testUploadLocalM3u8(accessKeyId, accessKeySecret, m3u8LocalFile):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(m3u8LocalFile, 'test upload local m3u8')
        # 分片文件和m3u8文件位于同一目录，SDK会自动解析上传
        videoId = uploader.uploadLocalM3u8(uploadVideoRequest)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))

    except AliyunVodException as e:
        print(e)


# 测试上传m3u8网络视频
def testUploadWebM3u8(accessKeyId, accessKeySecret, m3u8FileUrl):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(m3u8FileUrl, 'test upload web m3u8')
        uploadVideoRequest.setTemplateGroupId('19e0dd6310a5161f900bfac4838305a0')
        # 解析分片文件地址（适用于分片地址和m3u8文件签名相同或无签名的情况，其它情况需要您自行解析）
        sliceFileUrls = uploader.parseWebM3u8(m3u8FileUrl)
        videoId = uploader.uploadWebM3u8(uploadVideoRequest, sliceFileUrls)
        print("ssss",videoId)
        print("file: %s, videoId: %s" % (uploadVideoRequest.filePath, videoId))

    except AliyunVodException as e:
        print(e)


####  执行测试代码   ####
accessKeyId = 'LTAIyS9RFbHA4WFI'
accessKeySecret = 'ixzUo9ZFi854NS03X5uh9YSzH5xYYD'

localFilePath = 'D:\迅雷下载\map\851.mp4'
testUploadLocalVideo(accessKeyId, accessKeySecret, localFilePath)

# fileUrl = 'http://vod-test2.cn-shanghai.aliyuncs.com/72f8b5e970024318b672f2e9c7f610f2/0e9fb231b82b41ef8703a5c1882a7478-5287d2089db37e62345123a1be272f8b.mp4'
# testUploadWebVideo(accessKeyId, accessKeySecret, fileUrl)

m3u8LocalFile = '/Users/hufan/Desktop/Video/sample.m3u8'
# testUploadLocalM3u8(accessKeyId, accessKeySecret, m3u8LocalFile)

m3u8FileUrl = 'https://vod-test2.cn-shanghai.aliyuncs.com/d0261195719f401f8bb0ac09840b57b6/9de23b0134744701831bb503d0da57ca-4b6ffae84f2e1d243955ecaedcf11a3e.m3u8'
# testUploadWebM3u8(accessKeyId, accessKeySecret, m3u8FileUrl)
