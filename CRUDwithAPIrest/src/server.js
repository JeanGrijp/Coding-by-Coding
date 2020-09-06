require('dotenv').config()
const express = require('express')
const server = express()
const mongoose = require('mongoose')
const routes = require('./routes')

server.use(express.json())

mongoose.connect(process.env.DB_STRING, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then( () => {
    console.log('Connected to DB')
    server.emit('ok')
}).catch(e => {
    console.log(e)
})

server.use(routes)
server.use(express.urlencoded({extended : true}))


server.on('ok', () => {
    server.listen(3000, () => {
        console.log('http://localhost:3000')
        console.log('servidor executando na porta 3000')
    })
})