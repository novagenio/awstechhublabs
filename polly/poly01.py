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

texto = "hola como esta hoy dia"
session = Session(profile_name="adminuser")
polly = session.client("polly")
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

