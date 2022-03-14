import time

# kafka
from kafka import KafkaConsumer
consumer = KafkaConsumer('topic-basic-test', bootstrap_servers=['techhublabs.com:9092'],group_id='topic-basic-test')


for msg in consumer:
        servo = msg.key.decode("utf-8")
        grados = msg.value.decode("utf-8")
        print ("Servo:" + msg.key.decode("utf-8") + " Grados: " + msg.value.decode("utf-8"))

