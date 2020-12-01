var results = [];

function makeRequest (method, url, data) {
  return new Promise(function (resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.onload = function () {
      if (this.status >= 200 && this.status < 300) {
        resolve(xhr.response);
      } else {
        reject({
          status: this.status,
          statusText: xhr.statusText
        });
      }
    };
    xhr.onerror = function () {
      reject({
        status: this.status,
        statusText: xhr.statusText
      });
    };
    if(method=="POST" && data){
        xhr.send(data);
    }else{
        xhr.send();
    }
  });
}

makeRequest('GET', "/spirograph/getCoords/45/90").then(function(data){
	results=JSON.parse(data);
});

const canvas = document.querySelector('#spirographCanvas');
const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;
const ctx = canvas.getContext('2d');

function drawSpirograph() {
	ctx.fillStyle = 'rgb(0, 0, 0)';
	ctx.fillRect(0, 0, width, height);
	
	for (var i = 0; i < results.length; i++) {
		ctx.fillStyle = 'rgb(255, 0, 0)';
		ctx.fillRect(results[i][0], results[i][1], 4, 4);
	}
}

