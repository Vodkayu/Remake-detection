import requests
from json import JSONDecoder
import cv2

http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail"
key = "31p3ooxDXcsg1trVaykFPeHla8fC8jio"
secret = "nYm6-mBnXJY4XmdX0sqvrpzhFzh5-s9Q"

data = {"api_key": key, "api_secret": secret,"display_name":"faces","outer_id":"Zain"}

response = requests.post(http_url, data=data)
print(response)
print(response.text)
