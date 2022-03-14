from flask import Flask, request, Response, jsonify, json
from flask_cors import CORS
import time
import functions_rekognitionv2


PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)

############## esto es para evitar el  "No 'Access-Control-Allow-Origin'"
CORS(app, support_credentials=True)

@app.route('/')
def index():
    return Response(open('./static/getImage.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/imageR', methods=['POST'])

def imageR():

    i = request.files['image']  # get the image
    f = ('img_' + '%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    origen = ('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
    i.save(origen)
    functions_rekognitionv2.upload_file_s3(origen,f)
    print("s3 ")
    face_id, porcentaje=functions_rekognitionv2.SearchFacesByImage(f)
    print("face ")
    nombre=functions_rekognitionv2.BuscaEnBd(face_id)
    print("v1.0 El nombre encintrado es: " + nombre)
    saludo = "Hola, el sistema de Reconocimiento Bio Metrico, te ha identificado como: " + nombre + ", con una exactitud del: " + str(porcentaje) + "%, gracias "
    functions_rekognitionv2.delete_file_s3(f)   
    return Response(saludo)

@app.route('/imageC', methods=['POST'])

def imageC():

    i = request.files['image']  # get the image
    f = ('add_' + '%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    origen = ('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
    i.save(origen)
    functions_rekognitionv2.upload_file_s3(origen,f)
    print("s3 ")
    print("resuktado del request:   " + request.form['nombre'])
    print(" ============================== Detect Labels =====================================")
    descripcion, label_count=functions_rekognitionv2.detect_labels(f)
    print("Labels detected: " + str(label_count))

    print(" ============================== Detect Text   =====================================")
    text_count=functions_rekognitionv2.detect_text(f)
    print("Text detected: " + str(text_count))

    print(" ============================== Detect Face    =====================================")

    descripcion = functions_rekognitionv2.DetectFaces(f)

    print(" ============================== Index face     =====================================")

    functions_rekognitionv2.add_faceid(f, request.form['nombre'])

    #return Response("fichero grabado en S3 , " + origen)
    return Response(descripcion)

@app.route('/imageDF', methods=['POST'])

def imageDF():

    i = request.files['image']  # get the image
    f = ('add_' + '%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    origen = ('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
    i.save(origen)
    functions_rekognitionv2.upload_file_s3(origen,f)

    print(" ============================== Detect Face    =====================================")

    descripcion = functions_rekognitionv2.DetectFaces(f)

    print("=============================== Celebrities ==========================================")

    descripcion4 = functions_rekognitionv2.recognize_celebrities(f)

    return Response(descripcion + descripcion4)

@app.route('/imageDP', methods=['POST'])


def imageDP():

    i = request.files['image']  # get the image
    f = ('add_' + '%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    origen = ('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
    i.save(origen)
    functions_rekognitionv2.upload_file_s3(origen,f)
    print(" ============================== Detect Labels =====================================")
    descripcion, label_count = functions_rekognitionv2.detect_labels(f)
    print("Labels detected: " + str(label_count))
    print(" ============================== moderate image     =====================================")
    descripcion3, mod = functions_rekognitionv2.moderate_image(f)
    return Response(descripcion + descripcion3) 


@app.route('/imageDT', methods=['POST'])

def imageDT():

    i = request.files['image']  # get the image
    f = ('add_' + '%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    origen = ('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
    i.save(origen)
    functions_rekognitionv2.upload_file_s3(origen,f)
    print(" ============================== Detect Text   =====================================")
    descripcion2, text_count=functions_rekognitionv2.detect_text(f)
    print("Text detected: " + str(text_count))
    return Response(descripcion2)


@app.route('/datos',methods=['POST'])

def datos():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    return 'Hola ' + nombre + ' ' + apellido



@app.route('/api', methods=['POST'])

def hello():
    nombre = request.args.get('nombre')
    
    print(json.loads(request.data))
   # return jsonify(hello=nombre) # Returns HTTP Response with {"hello": "world"}
    return jsonify(json.loads(request.data))






if __name__ == "__main__": context = ('/etc/ssl/certs/techhublabs.com.crt', '/etc/ssl/private/techhublabs.com.key')
	app.run(host='ec2-52-209-149-64.eu-west-1.compute.amazonaws.com', port=8080 , ssl_context=context, threaded=True, debug=True)



