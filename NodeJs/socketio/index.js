const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// middleware auth
io.use((socket, next) => {
  const token = socket.handshake.query.token;
  if (token === '123') {
    return next();
  }
  return next(new Error('authentication error'));
});

io.on('connection', (socket) => {
  console.log('server side: ' + socket.id);
  socket.on('chat message', msg => {
    io.emit('chat message', msg);
  });
});

http.listen(port, () => {
  console.log(`Socket.IO server running at http://localhost:${port}/`);
});