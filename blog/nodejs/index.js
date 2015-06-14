var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var redis = require('redis');
var client = redis.createClient();
var user_client = redis.createClient();
client.subscribe('chat-channel');

var i = 0

io.on('connection', function(socket)
{
    var userL = ''
    user_client.get('user', function(err, reply) {
          userL = reply;
          io.emit('chat message', userL+', welcome to the test Chat Room!');
    });

    socket.on('disconnect', function () 
    {
         io.emit('chat message', userL+', left the chat.');
   });
});


client.on("message", function(channel, message) 
{
    io.emit('chat message', message);
});


http.listen(3000, function(){
  console.log('listening on *:3000');
});
