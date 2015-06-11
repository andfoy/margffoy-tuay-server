var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var redis = require('redis');
var client = redis.createClient();
client.subscribe('chat-channel');

var i = 0

io.on('connection', function(socket)
{
    //var user = ''
    //client.get('user', function(err, reply) {
    //      user = reply;
    //});
    io.emit('chat message', 'Welcome to the test Chat Room!');
});

client.on("message", function(channel, message) 
{
    io.emit('chat message', message);
});


http.listen(3000, function(){
  console.log('listening on *:3000');
});
