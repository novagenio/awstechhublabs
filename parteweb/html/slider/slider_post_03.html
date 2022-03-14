<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.slidecontainer {
  width: 100%;
}

.slider {
  -webkit-appearance: none;
  width: 100%;
  height: 25px;
  background: #d3d3d3;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
}

.slider:hover {
  opacity: 1;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  background: #4CAF50;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 25px;
  height: 25px;
  background: #4CAF50;
  cursor: pointer;
}
</style>
</head>
<body>

<h1>Custom Range Slider</h1>
<p>Drag the slider to display the current value.</p>

<div class="slidecontainer">
  <input type="range" min="1" max="100" value="50" class="slider" id="id1">
  
  <input type="range" min="1" max="100" value="50" class="slider"  id="id2">
 
  <input type="range" min="1" max="100" value="50" class="slider" id="id3">
  
  <span>Value:</span> <span id="f" style="font-weight:bold;color:red"></span>
</div>

<script>
var slideCol = document.getElementById("id1");
var slideSq = document.getElementById("id2");
var slidePic = document.getElementById("id3");
var y = document.getElementById("f");
y.innerHTML = slideCol.value;

slideCol.oninput = function() {
	y.innerHTML = this.value;
	console.log("slide 1:" + this.value)
        postData(1,this.value)
	
}

slideSq.oninput = function() {
	y.innerHTML = this.value;
	console.log("slide 2:" + this.value)
        postData(2,this.value)
}

slidePic.oninput = function() {
	y.innerHTML = this.value;
	console.log("slide 3:" + this.value)
        postData(3,this.value)
}


    //Add file blob to a form and post
    function postData(servo, grados) {
        let formdata = new FormData();
        formdata.append("servo", servo);
        formdata.append("grados", grados);
        let xhr = new XMLHttpRequest();
        xhr.open('POST', 'https://techhublabs.com:5000/slider', true);
        xhr.onload = function () {
            if (this.status === 200) {
                console.log(this.response);
                respuesta = this.response;
//                alert(respuesta);
		}
	        else
                {
//                alert(this.response);
                console.error(xhr);
                }
        };
        xhr.send(formdata);
    }

</script>

</body>
</html>



