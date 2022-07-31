/*
* Meta endpoints.
*
* These endpoints exist basically to test certain functionality.
*
* Remove after done
* */

const { Router } = require('express')
const db = require('../db/connection')
const dbQuery = require('../db/query')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, '../.env')})

const router = Router()

router.get('/', async (req, res) => { // tests that key works.
    const {key} = req.headers

    if (key === process.env.KEY) { // if the key is invalid
        try {

            res.status(200).send('worked')

        } catch (err) {
            res.status(500).send(err)
        }
    }
})

module.exports = router