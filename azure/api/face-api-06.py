# Request Body
body = dict()
body["url"] = "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Matthew_Perry_as_Chandler_Bing.jpg/220px-Matthew_Perry_as_Chandler_Bing.jpg"
body = str(body)

# Request URL 
FaceApiDetect = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true' 

try:
    # REST Call 
    response = requests.post(FaceApiDetect, data=body, headers=headers) 
    responseJson = response.json()
    faceId = responseJson[0]["faceId"]
    print("FACE ID: "+str(faceId))

except Exception as e:
    print(e)
