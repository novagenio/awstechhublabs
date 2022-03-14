# https://medium.com/@rachit.bedi1/microsoft-face-apis-using-python-e16775622e3b
personGroupId="friends"

# import modules
import requests


# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '99a1f1cdc635475e83152b0d3837cc39',
}

# 5 random images of chandler
chandlerImageList = ["http://www.imagozone.com/var/albums/vedete/Matthew%20Perry/Matthew%20Perry.jpg?m=1355670659",
                     "https://i.pinimg.com/236x/b0/57/ff/b057ff0d16bd5205e4d3142e10f03394--muriel-matthew-perry.jpg",
                     "https://qph.fs.quoracdn.net/main-qimg-74677a162a39c79d6a9aa2b11cc195b1",
                     "https://pbs.twimg.com/profile_images/2991381736/e2160154f215a325b0fc73f866039311_400x400.jpeg",
                     "https://i.pinimg.com/236x/f2/9f/45/f29f45049768ddf5c5d75ff37ffbfb3f--hottest-actors-matthew-perry.jpg"]

#Request URL
FaceApiCreatePerson = 'https://leogamboaface.cognitiveservices.azure.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId+'/persistedFaces'

for image in chandlerImageList:
    body = dict()
    body["url"] = image
    body = str(body)

    try:
        # REST Call
        response = requests.post(FaceApiCreatePerson, data=body, headers=headers)
        responseJson = response.json()
        persistedFaceId = responseJson["persistedFaceId"]
        print("PERSISTED FACE ID: "+str(persistedFaceId))

    except Exception as e:
        print(e)



