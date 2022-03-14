import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
from constantes  import *

#--------------------------------------------------------------------------------------------------------
def Play_Polly(texto):
        session = Session(profile_name="adminuser")
        polly = session.client("polly", region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
        response = polly.synthesize_speech(Text=texto, OutputFormat="mp3", VoiceId="Conchita")
        if "AudioStream" in response:
                with closing(response["AudioStream"]) as stream:
                     output = os.path.join(gettempdir(), "speech.mp3")
                     with open(output, "wb") as file:
                          file.write(stream.read())
        else:
            print("Could not stream audio")
            sys.exit(-1)
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])


#----------------------------------------------------------------------------
# DetectFaces: recive una fichero imagen , busca rostros e identifica caracteristicas del rostro
def DetectFaces(photo):  # https://docs.aws.amazon.com/es_es/rekognition/latest/dg/faces-detect-images.html
    client=boto3.client('rekognition',
	region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    frase = ""
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print("Entro en Funcion FaceDetail")
    for faceDetail in response['FaceDetails']:

        print(json.dumps(faceDetail, indent=4, sort_keys=True))
        maximo = 0
        index_max = 0
        emosion = "llevar una mascarilla"
        i =	 0
        for i in range(0, 7):
            if faceDetail['Emotions'][i]['Confidence'] > maximo:
               maximo = faceDetail['Emotions'][i]['Confidence']
               index_max = i

        print(faceDetail['Emotions'][index_max]['Type'])
        print(faceDetail['Gender']['Value'])
        print(faceDetail['Smile']['Value'])

        if faceDetail['Emotions'][index_max]['Type'] == "HAPPY": emosion = " alegre "
        if faceDetail['Emotions'][index_max]['Type'] == "SAD": emosion = " triste "
        if faceDetail['Emotions'][index_max]['Type'] == "ANGRY": emosion = " mal humor "
        if faceDetail['Emotions'][index_max]['Type'] == "CONFUSED": emosion = " confucion "
        if faceDetail['Emotions'][index_max]['Type'] == "SURPRISED": emosion = " sorpresa "
        if faceDetail['Emotions'][index_max]['Type'] == "CALM": emosion = " calma "
        if faceDetail['Emotions'][index_max]['Type'] == "UNKNOW": emosion = " indiferencia "
       
        if faceDetail['Gender']['Value'] == "Male": sexo = " un chico "
        elif  faceDetail['Gender']['Value'] == "Female": sexo = " una chica "
     
        if faceDetail['Smile']['Value'] == True: sonrisa = ", estas sonrriendo "
        elif faceDetail['Smile']['Value'] == False: sonrisa = ", no estas sonrriendo "

        if faceDetail['Eyeglasses']['Value'] == True: gafas = ", llevas gafas "
        elif faceDetail['Eyeglasses']['Value'] == False: gafas = ", no llevas gafas "

        if faceDetail['EyesOpen']['Value'] == True: ojos = " , tienes los ojos abiertos "
        elif faceDetail['EyesOpen']['Value'] == False: ojos = ",  no tienes los ojos  abiertos "

        if faceDetail['MouthOpen']['Value'] == True: boca = " , tienes la boca un poco abierta "
        elif faceDetail['MouthOpen']['Value'] == False: boca = ",  tienes la boca cerrada "

        if faceDetail['Mustache']['Value'] == True: barba = ", tienes barba "
        elif faceDetail['Mustache']['Value'] == False: barba = " "


        frase = "   Hola,  veo que eres " + sexo + "de entre " + str(faceDetail['AgeRange']['Low']) + " y " + str(faceDetail['AgeRange']['High']) + " de edad, "
        frase = frase + ", estas  " + emosion +  boca +  sonrisa + ojos + gafas + barba + " "  
#        Play_Polly(frase)       

        print (frase)
    return frase

#-----------------------------------------------------------------------------
def BuscaEnBd(face_id):  # recive como parametro un  FaceId y los busca en la base de datos y despliega los datos
              dynamodb = boto3.resource("dynamodb", 
			region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

              table = dynamodb.Table('Rekognition')
              nombre = "Desconocido o no encontro ningun rostro en la base de datos  .."
              print("GetItem succeeded:")
              try:
                     response = table.query(KeyConditionExpression=Key('FaceId').eq(face_id))
              except ClientError as e:
                     print(e.response['Error']['Message'])
              else:
                     for i in response['Items']:
                        print(i['FaceId'], ":", i['nombre'])
                        nombre=i['nombre']
              face_id=""
              return nombre


#-------------------------------------------------------------------------
# SearchFacesByImage: recive como parametro un fichero, detecta el rostro y busca la imagen en mycollection.
def SearchFacesByImage(fileName):          # https://docs.aws.amazon.com/es_es/rekognition/latest/dg/search-face-with-image-procedure.html
    threshold = 70
    maxFaces=2
    face_id=0
    porcentaje=0
    client=boto3.client('rekognition',
		region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    try:
	    response=client.search_faces_by_image(CollectionId=collectionId,
                               Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                               FaceMatchThreshold=threshold,
                               MaxFaces=maxFaces)
    except ClientError as e:
            print(e.response['Error']['Message'])
    else:
            faceMatches=response['FaceMatches']
            print("Inicio funcion faceMatch")
            for match in faceMatches:
                face_id=match['Face']['FaceId']
                print ('face_id:' + face_id + "/")
                print ('FaceId:' + match['Face']['FaceId'])
                print ('ImageId:' + match['Face']['ImageId'])
                print ('ExternalImageId:' + match['Face']['ExternalImageId'])
                porcentaje="{:.2f}".format(match['Similarity'])
                print(porcentaje)
                print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                print("Fin Función FaceMatch, retorna face_id: " + face_id )	
    return face_id, porcentaje
		
#----------------------------------------------------------------------
def upload_file_s3(origen, destino): # recive como arametro la ruta y fichero origen y nombre  con que se quedara en el S3
    s3 = boto3.resource('s3',region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    s3.Bucket(bucket).upload_file(origen, destino)


def delete_file_s3(fichero):
    client = boto3.client('s3', region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    client.delete_object(Bucket=bucket, Key=fichero)


def add_faceid(fileName, nombre_capturado):
            client = boto3.client('s3',region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
            FaceId = 0
            client=boto3.client('rekognition', region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
            try:
                response=client.index_faces
                response=client.index_faces(CollectionId=collectionId,
                         Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                         ExternalImageId=fileName,
                         DetectionAttributes=['ALL'])

                # entrega el detalle del rostro
                print(json.dumps(response, indent=4, sort_keys=True))

            except ClientError as e:
                print("No encontro ningun rostro en la imagen............")
                print(e.response['Error']['Message'])
                
            else:
                print ('Faces in ' + fileName)
                for faceRecord in response['FaceRecords']:
                    print (faceRecord['Face']['FaceId'])
                    FaceId=faceRecord['Face']['FaceId']
                    print (faceRecord['Face']['ImageId'])
                    print (faceRecord['Face']['ExternalImageId'])
                    FaceId = 1
                    
                if FaceId == 0:
                    print("No encontro ningun rstro a catalogar............")
                    return
                # sube registro con datos de Rekognition /
                dynamodb = boto3.resource('dynamodb', region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
                table = dynamodb.Table('Rekognition')
                
                response = table.put_item(
                  Item={
                       'FaceId': faceRecord['Face']['FaceId'],
                       'ImageId': faceRecord['Face']['ImageId'],
                       'ExternalImageId': faceRecord['Face']['ExternalImageId'],
                       'empleadoId': "n000000 ",
                       'nombre': nombre_capturado
                }
                )
                print("PutItem succeeded:")
    


def detect_labels(photo):
	client=boto3.client('rekognition', region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key) 
	
	response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},MaxLabels=10)
	print('Detected labels for ' + photo)
	print()
	descripcion = '\n' + "Detected labels" +'\n'
	for label in response['Labels']:
		print(label['Name'] + " Confidence: " + str(label['Confidence']))
		descripcion = descripcion + label['Name'] + " - " +'\n'
 
#                 print ("Confidence: " + str(label['Confidence']))
#                 print ("Instances:")
#                 for instance in label['Instances']:
#                         print (" Bounding box")
#                         print (" Top: " + str(instance['BoundingBox']['Top']))
#                         print (" Left: " + str(instance['BoundingBox']['Left']))
#                         print (" Width: " + str(instance['BoundingBox']['Width']))
#                         print (" Height: " + str(instance['BoundingBox']['Height']))
#                         print (" Confidence: " + str(instance['Confidence']))
#                         print()
#                 print ("Parents:")
#                 for parent in label['Parents']:
#                         print (" " + parent['Name'])
#                         print ("----------")
#                         print ()
	return descripcion, len(response['Labels'])


def detect_sentiment(text):
    comprehend = boto3.client(service_name='comprehend', 
		region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    response=comprehend.detect_sentiment(Text=text, LanguageCode='es')
    textDetections=response['Sentiment']
    return textDetections




def detect_text(photo):

    client=boto3.client('rekognition', 
		region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    textDetections=response['TextDetections']
    descripcion = '\n' + "Detected text" +'\n'
    print ('Detected text\n----------')
    for text in textDetections:
        print ('Detected text:' + text['DetectedText'])
#        descripcion = descripcion +  'Detected text:' + text['DetectedText'] +'\n'  
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
#        print ('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print ('Parent Id: {}'.format(text['ParentId']))
        else:
            #descripcion = descripcion +  'Detected text:' + text['DetectedText'] +'\n'
            descripcion = descripcion +  text['DetectedText'] # + '\n' 

    descripcion = descripcion + '\n' + "Sentimiento detectado: " +  detect_sentiment(descripcion)
    return descripcion, len(textDetections)    


def moderate_image(photo):
    client=boto3.client('rekognition',region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    descripcion = '\n' + "Detect Moderation Label" +'\n'
    print('Detected labels for ' + photo)
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
        descripcion = descripcion + label['Name'] + ' : ' + str(label['Confidence']) + " " + label['ParentName'] + '\n' 
    return descripcion, len(response['ModerationLabels'])


def recognize_celebrities(photo):
    client=boto3.client('rekognition', region_name=reg, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    descripcion = '\n' + "Detect Celebrities" +'\n'
    #with open(photo, 'rb') as image:
    response = client.recognize_celebrities(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    print('Detected faces for ' + photo)
    for celebrity in response['CelebrityFaces']:
        descripcion = descripcion + celebrity['Name']       
        print ('Name: ' + celebrity['Name'])
        print ('Id: ' + celebrity['Id'])
        print ('Position:')
    return descripcion
 

