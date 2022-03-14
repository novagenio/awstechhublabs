from flask import Flask, request, Response
from flask_cors import CORS

import time

app = Flask(__name__)
CORS(app, support_credentials=True)



@app.route('/slider',methods=['POST'])

def test():
    servo = request.form["servo"]
    grados = request.form["grados"]
    print("servo: " + servo + " grados: " + grados)
    return servo


#if __name__=="__main__":
#        app.run(host="techhublabs.com", port=5000)

if __name__ == "__main__":
    context = ('/etc/ssl/certs/techhublabs.com.crt', '/etc/ssl/private/techhublabs.com.key')
    app.run(host='ec2-99-81-106-108.eu-west-1.compute.amazonaws.com', port=5000, ssl_context=context, threaded=True, debug=True)


