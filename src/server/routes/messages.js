/*
* Message endpoints.
*
* Messages will be stored in the database along with their attributes (contents, author, attachments etc)
* we store messages when we want to archive a message.
* */

const { Router } = require('express')
const db = require('../db/connection')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, '../.env')})


const router = Router()



// get a message

// add a message

// delete a message



module.exports = router