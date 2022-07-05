/*
* Waycord server.
*
* Dev: Loona/MonEmperor
* date: 07/03/2022
* */

const express = require('express')
const bodyParser = require('body-parser')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, './.env')})

const app = express() // initializes express



// uses body parser
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))



// adds all the routes
users = require('./routes/users')
app.use('/users', users)

messages = require('./routes/messages')
app.use('/messages', messages)

servers = require('./routes/servers')
app.use('/servers', servers)

channels = require('./routes/channels')
app.use('/channels', channels)



// listens to the port
app.listen(process.env.PORT, () => {
    console.log(`server is up and running on port ${process.env.PORT}`)
})