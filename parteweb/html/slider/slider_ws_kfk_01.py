from time import sleep
from kafka import KafkaProducer

from flask import Flask, request, Response
from flask_cors import CORS

import time

producer = KafkaProducer(bootstrap_servers='techhublabs.com:9092')

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/slider',methods=['POST'])

def test():
    servo = request.form["servo"]
    grados = request.form["grados"]
    print("servo: " + servo + " grados: " + grados)
    producer.send('topic-basic-test', key=servo.encode(), value=grados.encode())
    sleep(0.1)
    return servo


#if __name__=="__main__":
#        app.run(host="techhublabs.com", port=5000)

if __name__ == "__main__":
    context = ('/etc/ssl/certs/techhublabs.com.crt', '/etc/ssl/private/techhublabs.com.key')
    app.run(host='ec2-34-250-190-216.eu-west-1.compute.amazonaws.com', port=5000, ssl_context=context, threaded=True, debug=True)


