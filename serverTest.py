
from flask import Flask, request, Response, jsonify, json
from flask_cors import CORS
import time

app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route("/person", methods=['POST', 'GET']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET. 

def handle_person(): 
	if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
		average_time = request.form.get('average_time')
		choices = request.form.get('choices')
		return(jsonify(average_time = 100),200)











if __name__ == "__main__":
	context = ('/etc/ssl/certs/techhublabs.com.crt', '/etc/ssl/private/techhublabs.com.key')
	app.run(host='ec2-52-209-149-64.eu-west-1.compute.amazonaws.com', port=8080, ssl_context=context, threaded=True, debug=True)

