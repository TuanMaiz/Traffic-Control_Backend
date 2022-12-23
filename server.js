if(process.env.NODE_ENV !== 'production') //load .env file only in develop process
{
    require('dotenv').config()
}
const express = require('express')
const http = require('http')
const app = express()
var cors = require('cors')
const server  = http.createServer(app)
const { Server } = require('socket.io')

app.use(cors())
const io = new Server(server, {
    cors: {
        origin: "http://localhost:3000",
      }
})
const port = process.env.PORT || 3001

// app.get('/', (req, res) => {
//     res.sendFile( __dirname + '/index.html')
// })

//websocket part
io.on('connection', (socket) => {
    console.log(`User ${socket.id} connected`);
    socket.on('send-frame', async (data) => {
        console.log(data);
        socket.broadcast.emit('on-frame-react', data)
    })
})
// io.on('connection', (socket) => { // when there is event 'on-chat' then do sth
//     socket.on('on-chat', (data) => {
//       console.log(data); // 
//       io.sockets.emit('on-chat-react', data)
//     });
// });


//mongodb part
// const mongoose = require('mongoose')
// console.log('url la ' + process.env.MONGODB_URI);
// mongoose.set('strictQuery', true)
// mongoose.connect(process.env.MONGODB_URI, {useNewUrlParser: true})
// const db = mongoose.connection
// db.on('error', err => console.error(error))
// db.once('open', () => {console.log('Connected to Mongo');})

server.listen(port, () => {
    console.log(`App is listening on port ${port}`);
})