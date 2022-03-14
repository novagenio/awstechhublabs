import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')

text = "Buenso días, he enviado una reclamación hace un par de semanas al no poder conectarme a internet con mi nuevo servicio contratado. Y aun  no tengo contestación.  Muchas gracias. "

response=comprehend.detect_sentiment(Text=text, LanguageCode='en')
textDetections=response['Sentiment']
print('Sentimiento encontrado:' +  textDetections) 

