import requests
from json import JSONDecoder
import cv2

key = "31p3ooxDXcsg1trVaykFPeHla8fC8jio"
secret = "nYm6-mBnXJY4XmdX0sqvrpzhFzh5-s9Q"
 
filepath ="C:\\Users\\tzmzy\\Desktop\\6.png"


#传入图片文件
def detect_face(filepath):
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}
    data = {"api_key":key, "api_secret": secret}
    response = requests.post(http_url, data=data, files=files)
    req_dict = response.json()
    print(req_dict)
    return req_dict

if __name__ == "__main__":
    detect_face(filepath)

#将face加入到faceset
def addface(faceset,facetokens):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    params = {
            'api_key':key,
            'api_secret':secret,
            'outer_id':"Zain",
            'face_tokens':facetokens
            }
    r = requests.post(url,data = params)
    req_dict = r.json()
    print(req_dict)
    return req_dict
    
if __name__ == "__main__":
    image1 = detect_face(filepath)
    faceId1 = image1['faces'][0]['face_token']
    addface('338bf95e3268d1a3c802f03a3f78fff1',faceId1)

def face_SetUserID(user_id,faceId1):#为检测出的某一个人脸添加标识信息，该信息会在Search接口结果中返回，用来确定用户身份。
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    params = {
            'api_key':key,
            'api_secret':secret,
            'face_token':faceId1,
            'user_id':"Ma Zhenyu"
            }
    r = requests.post(url,data = params)
    req_dict = r.json()
    print(req_dict)
    return req_dict
