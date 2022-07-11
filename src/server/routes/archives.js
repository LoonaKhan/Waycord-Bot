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
// whenever the user wants to get one of their archives
// requires title and owner id, user searches their own archives by name. or creation date?

// add an archive
//takes in a title, message id, owner id.

// delete an archive
// user wants to get rid of one
// can delete by title, or id.



module.exports = router