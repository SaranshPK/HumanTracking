var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var updateID = setInterval(updateClient, 100);
var i = 0;
app.get('/', function(req, res) {
    res.sendFile(__dirname + "/ImageP.html");
});

io.on('connect', function(socket) {
    socket.emit('connected');
});

http.listen(3141, function() {
    console.log("Connecting to port 3141...");
});
function updateClient(){
    i++
    io.emit('Update',i)
}