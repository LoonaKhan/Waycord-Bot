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



// listens to the port
app.listen(process.env.PORT, () => {
    console.log(`server is up and running on port ${process.env.PORT}`)
})