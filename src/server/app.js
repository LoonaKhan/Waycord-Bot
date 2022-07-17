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
const messages = require('./routes/messages')
app.use('/messages', messages)

const archives = require('./routes/archives')
app.use('/archives', archives)

const servers = require('./routes/servers')
app.use('/servers', servers)

const meta = require('./routes/meta')
app.use('/', meta)



// listens to the port
app.listen(process.env.PORT, () => {
    console.log(`server is up and running on port ${process.env.PORT}`)
})