# Request URL 
FaceApiGetPerson = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId

try:
    response = requests.get(FaceApiGetPerson, headers=headers) 
    responseJson = response.json()
    print("This Is "+str(responseJson["name"]))
    
except Exception as e:
    print(e)

