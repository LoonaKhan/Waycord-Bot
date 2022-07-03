/*
* Waycord server.
*
* Dev: Loona/MonEmperor
* date: 07/03/2022
* */

const express = require('express')
const bodyParser = require('body-parser')

const app = express()
const port = 4000

// uses body parser
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))

// adds all the routes
users = require('routes/Users')
app.use('/users', users)

messages = require('routes/Messages')
app.use('/messages', messages)

servers = require('routes/Servers')
app.use('/servers', servers)

channels = require('routes/Channels')
app.use('/channels', channels)

// listens to the port
app.listen(port, () => {
    console.log(`server is up and running on port ${port}`)
})