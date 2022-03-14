# https://medium.com/@rachit.bedi1/microsoft-face-apis-using-python-e16775622e3b

# import variables, headers and base_url
from header import *

# import modules
import requests

personGroupId="friends"

# Request URL
FaceApiCreateLargePersonGroup = base_url + 'persongroups/'+personGroupId


body = dict()
body["name"] = "F.R.I.E.N.D.S"
body["userData"] = "All friends cast"
body = str(body)


try:
    # REST Call
    response = requests.put(FaceApiCreateLargePersonGroup, data=body, headers=headers)
    print("RESPONSE:" + str(response.status_code))

except Exception as e:
    print(e)


