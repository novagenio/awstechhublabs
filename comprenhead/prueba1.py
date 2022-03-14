import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
                

text = "Buenso días, he enviado una reclamación hace un par de semanas al no poder conectarme a internet con mi nuevo servicio contratado. Y aun  no tengo contestación.  Muchas gracias. "


print('Calling DetectDominantLanguage')
print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))
print("End of DetectDominantLanguage\n")

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectEntities\n')

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectKeyPhrases\n')

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')

#print('Calling DetectSyntax')
#print(json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
#print('End of DetectSyntax\n')


response=comprehend.detect_dominant_language(Text = text)
textDetections=response['LanguageCode']
print('Idioma:' +  textDetections) 


response=comprehend.detect_sentiment(Text=text, LanguageCode='en')
textDetections=response['Sentiment']
print('Sentimiento encontrado:' +  textDetections) 

for sent in textDetections:
    print ('Detected text:' + textDetections)

