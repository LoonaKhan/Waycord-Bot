/*
* Archive endpoints.
*
* Archives are the main data of an app.
*
* The archives are made up of:
*   title
*   owner(id)
*   message(id)
*   channel(id)
* all the id's are references to another db object
* */

const { Router } = require('express')
const db = require('../db/connection')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, '../.env')})

const router = Router()



// get an archive

// add an archive
/*
* takes in a title, message id, owner id and channel id.
* */

// update an archive

// delete an archive



module.exports = router