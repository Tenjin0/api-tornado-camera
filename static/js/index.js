"use strict"

var self = this, video = document.getElementById("video");

socket = new WebSocket("ws://" + window.location.hostname + ":" + window.location.port + "/ws");


readCamera = function() {
    socket.send("read_camera");
}

socket.onopen = function() {
    console.log("Connected");
    readCamera()
}

socket.onmessage = function(messageEvent) {
    console.log(messageEvent)
    video.src = "data:image/jpeg;base64," + messageEvent.data;
}