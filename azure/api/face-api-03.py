# https://medium.com/@rachit.bedi1/microsoft-face-apis-using-python-e16775622e3b

# import variables, headers and base_url
from header import *


# https://medium.com/@rachit.bedi1/microsoft-face-apis-using-python-e16775622e3b
personGroupId="friends"

# import modules
import requests



#Request Body
body = dict()
body["name"] = "Chandler"
body["userData"] = "Friends"
body = str(body)

#Request URL
FaceApiCreatePerson = base_url + personGroupId + '/persons'

try:
    # REST Call
    response = requests.post(FaceApiCreatePerson, data=body, headers=headers)
    responseJson = response.json()
    personId = responseJson["personId"]
    print("PERSONID: "+str(personId))

except Exception as e:
    print(e)


