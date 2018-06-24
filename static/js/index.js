var host = window.location.host;
var ws = new WebSocket("ws://" + host + "/ws");

let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');
// let image = new Image();
let image = document.getElementById('camera')

function drawCanvas() {
    context.drawImage(image, 0, 0, 600, 450);
}

ws.onopen = function() {
    ws.send("message", "user connected");
};

ws.onmessage = function(e) {
    // image.onload = function () {
    //     draw_context.drawImage(image, 0, 0, 600, 450);
    // };
    image.src = e.data;
    drawCanvas();
}
