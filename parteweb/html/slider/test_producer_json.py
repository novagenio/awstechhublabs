from kafka import KafkaProducer
from time import sleep
import time as time_

import json


producer = KafkaProducer(bootstrap_servers='techhublabs.com:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('topic-basic-test', {'Servo':1,'Grados':30, 'Time':int(round(time_.time()))})
sleep(0.1)

