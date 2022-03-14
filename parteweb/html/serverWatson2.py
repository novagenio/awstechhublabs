import  json

import time

#import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('hwjdUKM2X3EPLPaR8FqonQCIqfQzsWVnu_PM6iSIj6qm')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/6c600964-f638-4bfe-b560-deed58379a94')



def api(req, data):

    print("Json original:")
    print(json.loads(data))
    data=json.loads(data)
    texto=data['texto_traducir']
    print("campo extraido:" + texto)

    translation = language_translator.translate(texto, model_id='en-es').get_result()
    traduccion = json.dumps(translation, indent=2, ensure_ascii=False)
    decode=json.loads(traduccion)

    print("final 2:"  + str(decode['translations'][0]))

    #   return jsonify(json.dumps(translation, indent=2, ensure_ascii=False))
    #   return { 'message' : 'Hello World' } 

    a = decode['translations'][0]
    b = a['translation']

    #return { 'message' : str(decode['translations'][0])}
    return { 'message' : b }

