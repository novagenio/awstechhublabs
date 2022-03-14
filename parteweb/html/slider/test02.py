from kafka import KafkaProducer
from time import sleep


import json


producer = KafkaProducer(bootstrap_servers='techhublabs.com:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('topic-basic-test', {'foo': 'bar'})
sleep(0.1)

