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
// whenever we get an archive?

// add a message
// whenever we archive a message

// delete a message
// whenever we un-archive something, delete the corresponding message



module.exports = router