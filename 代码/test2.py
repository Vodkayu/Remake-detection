import requests
from json import JSONDecoder
import time
import cv2
import os

key = "31p3ooxDXcsg1trVaykFPeHla8fC8jio"
secret = "nYm6-mBnXJY4XmdX0sqvrpzhFzh5-s9Q"

def face_search(image_file1,faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {"image_file": open(image_file1, "rb")}
    params = {
            "api_key":key,
            "api_secret":secret,
            "faceset_token":"338bf95e3268d1a3c802f03a3f78fff1"
            }
    r = requests.post(url,files = files,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

if __name__ == "__main__":
    capInput = cv2.VideoCapture(0)#开摄像头1
    faceCascade = cv2.CascadeClassifier('E:\\haarcascade\\haarcascade_frontalface_default.xml')#载入脸的特征
    face_right = 0  #识别的人脸有没有在faceset中发现，有置1
    recognize_inf = 0 #识别的人脸在faceset中发现，置1,持续显示id信息一定时间标志位
    font = cv2.FONT_HERSHEY_SIMPLEX#字体设置
    i=0#自加每20次访问API，每一帧都访问代价太高，且容易卡顿
    while(1):
        ret, img = capInput.read()#摄像头获取该帧图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#图像转灰度
        faces = faceCascade.detectMultiScale(gray,1.1,7)#送入Haar特征分类器
        if cv2.waitKey(1) & 0xFF == ord('q'):#键入q退出
             break
        if len(faces) == 0 :#视频中无脸出现不用请求API
            cv2.imshow('ImageCaptured', img)
        else:    
            if i >= 20 and face_right == 0:
                i = 0#清零
                cv2.imwrite(r"C:\\Users\\tzmzy\Desktop\\Face_Search\\1.jpg",img)#写入该帧图像文件
                face_information = face_search(r"C:\\Users\\tzmzy\Desktop\\Face_Search\\1.jpg",'e55232f11a305f9165caf50ef16ae053')#该帧与faceset中人脸进行匹配
                if face_information['faces'] :#[faces]数组不能为空，能在图像中找到脸
                    confidence = face_information['results'][0]['confidence']#读取置信度
                    thresholds = face_information['thresholds']['1e-5']
                    os.remove(r"C:\\Users\\tzmzy\Desktop\\Face_Search\\1.jpg")#删除该帧图像文件，为下一次处理准备
                    if confidence > 75 and thresholds < confidence:  #置信度阈值判断
                        user_id = face_information['results'][0]['user_id'] #获得唯一人脸id
                        recognize_inf = 1
                        face_right = 1
                    else: 
                        face_right = 0
                else:
                    face_right = 0#未能在图像中找到脸
            else:
                i = i + 1
                    
            for x, y, w, h in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)#人脸矩形框
            
            if face_right == 1:
                cv2.putText(img, user_id, (x,y-5), font,1, (0,0,255),1)
                cv2.putText(img, "Welcome:", (x-20,y-50), font,2, (0,0,0),2)
                cv2.imshow('ImageCaptured', img)
                if recognize_inf:
                    b = (time.localtime()[5])   
                    a = (time.localtime()[5])
                    recognize_inf = 0
                if(abs(a-b)<=3):#现在该提示信息3s
                    a = (time.localtime()[5])
                else:
                    face_right = 0
            else:
                cv2.putText(img, "Stranger", (x,y-5), font,1, (0,255,0),1)
                cv2.imshow('ImageCaptured', img)
            
capInput.release()        
cv2.destroyAllWindows()