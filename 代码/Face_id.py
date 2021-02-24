import requests
from json import JSONDecoder
import cv2

http_url = "https://api-cn.faceplusplus.com/facepp/v3/face/setuserid"
key = "31p3ooxDXcsg1trVaykFPeHla8fC8jio"
secret = "nYm6-mBnXJY4XmdX0sqvrpzhFzh5-s9Q"

data = {"api_key": key, "api_secret": secret, "outer_id": "Zain","face_token":"8b4a91bddd07b1948b3823cccfdc7ad2","user_id": "Zheng Yuying"}
response = requests.post(http_url, data=data)
print(response)
print(response.text)

