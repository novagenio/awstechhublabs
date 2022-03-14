faceIdsList = [faceId]

# Request Body
body = dict()
body["personGroupId"] = personGroupId
body["faceIds"] = faceIdsList
body["maxNumOfCandidatesReturned"] = 1 
body["confidenceThreshold"] = 0.5
body = str(body)

# Request URL 
FaceApiIdentify = 'https://westus.api.cognitive.microsoft.com/face/v1.0/identify' 

try:
    # REST Call 
    response = requests.post(FaceApiIdentify, data=body, headers=headers) 
    responseJson = response.json()
    personId = responseJson[0]["candidates"][0]["personId"]
    confidence = responseJson[0]["candidates"][0]["confidence"]
    print("PERSON ID: "+str(personId)+ ", CONFIDENCE :"+str(confidence))
        
except Exception as e:
    print("Could not detect")

