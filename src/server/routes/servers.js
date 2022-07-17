/*
* Server endpoints.
*
* Servers dont need to be stored atm.
* So there is little point of keeping track of them.
* unless we think of a use-case.
* */

const { Router } = require('express')
const db = require('../db/connection')
const dbQuery = require('../db/query')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, '../.env')})

const router = Router()



// get a server
// whenever a server-related command is called. prob not needed.
router.get('/:id',  async (req, res) => {

    const { key } = req.headers
    if (key !== process.env.KEY) { // if the key is invalid
        res.status(400).send() // just dont respond?
    }

    try {

        dbQuery(``)

    } catch (err) {
        res.status(500).send(err)
    }

})

// add a server
// Used when the bot first joins a server.

// update a server
// attempts to be used whenever a bot command is used in a server

// delete a server
// todo: allow the admins to blacklist a server from being tracked?



module.exports = router