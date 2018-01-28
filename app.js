var express = require('express');
var app = express();
var server = require('http').Server(app);

var io = require('socket.io')(server);

var sockets = [];

app.get('/trigger', function(req, res) {
    console.log('Trigger socket.');
    
    // Trigger all sockets.
    for (var i = 0; i < sockets.length; i++){
        sockets[i].emit('alert',);
    }

    res.sendStatus(200);
});

io.on('connection', function (socket) {
    sockets.push(socket);
    console.log('add socket');

    socket.on('disconnect', function (){
        var index = sockets.indexOf(socket);
        sockets.splice(index, 1);
        console.log('remove socket');
    });
});

server.listen(8080);