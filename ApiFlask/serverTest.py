

from flask import Flask, request, Response, jsonify, json
import time

app = Flask(__name__)

@app.route("/person", methods=['POST', 'GET']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET. 

def handle_person(): 
	if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
		msg_subj = request.args.get('msg_subj')
		print(msg_subj)
		salida = request.form.get('choices')
		return(jsonify(msg_subj=msg_subj),200)


if __name__ == "__main__":
	context = ('/etc/ssl/certs/techhublabs.com.crt', '/etc/ssl/private/techhublabs.com.key')
	app.run(host='ec2-52-209-149-64.eu-west-1.compute.amazonaws.com', port=8080, ssl_context=context, threaded=True, debug=True)

