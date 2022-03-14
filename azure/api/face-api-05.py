#Request Body
body = dict()

#Request URL 
FaceApiTrain = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/train'

try:
    # REST Call 
    response = requests.post(FaceApiTrain, data=body, headers=headers) 
    print("RESPONSE:" + str(response.status_code))

except Exception as e:
    print(e)

