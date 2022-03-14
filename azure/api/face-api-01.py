
# https://medium.com/@rachit.bedi1/microsoft-face-apis-using-python-e16775622e3b

# import variables, headers and base_url
from header import *

# import modules
import requests

# Request URL
FaceApiDetect = base_url + 'detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair'



body = dict()
body["url"] = "http://www.imagozone.com/var/albums/vedete/Matthew%20Perry/Matthew%20Perry.jpg?m=1355670659"
body = str(body)

try:
    # REST Call
    response = requests.post(FaceApiDetect, data=body, headers=headers)
    print("RESPONSE:" + str(response.json()))

except Exception as e:
    print(e)


