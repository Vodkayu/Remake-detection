import requests
from json import JSONDecoder
import cv2

http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface"
key = "31p3ooxDXcsg1trVaykFPeHla8fC8jio"
secret = "nYm6-mBnXJY4XmdX0sqvrpzhFzh5-s9Q"

data = {"api_key": key, "api_secret": secret,"display_name":"faces","outer_id":"Zain","face_tokens":"6eeb4ac17f097c4fc3ba4dd67f7e046f,40e89b4556edc744cf6ece1d44f95887,0838d316fb1eea5629275a33ddc0ad14"}

response = requests.post(http_url, data=data)
print(response)
print(response.text)
