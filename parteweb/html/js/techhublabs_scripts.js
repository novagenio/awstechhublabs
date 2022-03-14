 // Initialize the Amazon Cognito credentials provider
        AWS.config.region = 'eu-west-1';
        AWS.config.credentials = new AWS.CognitoIdentityCredentials({IdentityPoolId: "eu-west-1:1ec82e00-df42-406f-8ca8-cb9b5d337e92"});


//    var captureButton = document.getElementById('capture');
    var nombre_capturado = ""
    let v = document.getElementById("myVideo");
    var tipo;
    var respuesta;

    //create a canvas to grab an image for upload
    let imageCanvas = document.createElement('canvas');
    let imageCtx = imageCanvas.getContext("2d");

    //Add file blob to a form and post
    function postFile(file) {
        let formdata = new FormData();
        formdata.append("image", file);
        formdata.append("nombre", nombre_capturado);
        let xhr = new XMLHttpRequest();
        if (tipo == "C") {
                xhr.open('POST', 'https://techhublabs.com:8080/imageC', true);
                }
        else
                {
                xhr.open('POST', 'https://techhublabs.com:8080/imageR', true);
                }	
        if (tipo == "F") {
                xhr.open('POST', 'https://techhublabs.com:8080/imageDF', true);
                }
        if (tipo == "P") {
                xhr.open('POST', 'https://techhublabs.com:8080/imageDP', true);
                }
        if (tipo == "T") {
                xhr.open('POST', 'https://techhublabs.com:8080/imageDT', true);
                }


        xhr.onload = function () {
            if (this.status === 200) {
                console.log(this.response);
                respuesta = this.response;

//              alert(respuesta);
                if (tipo == "C") {
//                      document.getElementById("demo").innerHTML = nombre_capturado;
                        alert("Se ha guardado exitosamente el perfil biometrico de: " + nombre_capturado + " " + respuesta);
                        }
                else
                        {
//                      document.getElementById("rekognition").innerHTML = respuesta;
                        alert(respuesta);
			speakText(respuesta);
                        }
                }
            else
                {
                alert(this.response);
                console.error(xhr);
                }
        };
        xhr.send(formdata);
    }

    //Get the image from the canvas
    function sendImagefromCanvas() {
        //Make sure the canvas is set to the current video size
        imageCanvas.width = 400;
        v.videoWidth;
        imageCanvas.height = 400;
        v.videoHeight;
        imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight);
        //Convert the canvas to blob and post the file
        imageCanvas.toBlob(postFile, 'image/jpeg');
    }


 function buttom_capture_nombre(f) {
        event.preventDefault();
        tipo = "C";
        respuesta = "";
        var ok = true;
        var msg = "Debes escribir algo en los campos:\n";
          if(f.elements[0].value == "")
                {
                    msg = "Hola, es necesario que escribas un nombre en el campo. Intentalo nuevamente ..";
                    speakText(msg);
                    ok = false;
                }
          if(ok == false)
              alert(msg);
          else
                {
                console.log('buttom tipo C, capture' + 'nombre capturado:' + f.elements[0].value);
                nombre_capturado = f.elements[0].value;
                sendImagefromCanvas();
                document.frm_nombre.nombre.value=""
                }
//        return ok;
    };

    function buttom_capture_face(f) {
        event.preventDefault();
        tipo = "F";
        respuesta = "";
        var ok = true;
        console.log("buttom tipo DF, describe face")
        sendImagefromCanvas();
    };

    function buttom_capture_picture(f) {
        event.preventDefault();
        tipo = "P";
        respuesta = "";
        var ok = true;
        console.log("buttom tipo DP, describe picture")
        sendImagefromCanvas();
    };


    function buttom_capture_text(f) {
        event.preventDefault();
        tipo = "T";
        respuesta = "";
        var ok = true;
        console.log("buttom tipo DT, describe text")
        sendImagefromCanvas();
    };


    function buttom_capture() {
        tipo = "C";
        respuesta = "";
        console.log('buttom tipo C, capture');
        sendImagefromCanvas();
    };

    function buttom_rekognition() {
        tipo = "R";
        console.log('buttom tipo R, rekognition');
        sendImagefromCanvas();
    };








    window.onload = function () {
        //Get camera video
        navigator.mediaDevices.getUserMedia({video: {width: 400, height: 400}, audio: false})
            .then(stream => {
                v.srcObject = stream;
            })
            .catch(err => {
                console.log('navigator.getUserMedia error: ', err)
            });
    };



// Function invoked by button click --- Polly
        function speakText(text_to) {
            // Create the JSON parameters for getSynthesizeSpeechUrl
            var speechParams = {
                OutputFormat: "mp3",
                SampleRate: "16000",
                Text: "",
                TextType: "text",
//               VoiceId: "Matthew"
                VoiceId:  "Conchita"
            };
            //            speechParams.Text = document.getElementById("textEntry").value;
            speechParams.Text = text_to;


            // Create the Polly service object and presigner object
            var polly = new AWS.Polly({apiVersion: '2016-06-10'});
            var signer = new AWS.Polly.Presigner(speechParams, polly)

            // Create presigned URL of synthesized speech file
            signer.getSynthesizeSpeechUrl(speechParams, function(error, url) {
            if (error) {
                document.getElementById('result').innerHTML = error;
            } else {
                document.getElementById('audioSource').src = url;
                document.getElementById('audioPlayback').load();
//                document.getElementById('result').innerHTML = "Speech ready to play.";
            }
          });
        }

