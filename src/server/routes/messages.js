/*
* Message endpoints.
*
* Messages will be stored in the database along with their attributes (contents, author, attachments etc)
* we store messages when we want to archive a message.
* */

const { Router } = require('express')
const db = require('../db/connection')
const Query = require('.././db/query')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, '../.env')})


const router = Router()



// get a message
// whenever we get an archive?
router.get('/:id', async (req, res) =>{

    const { key } = req.headers
    const {id} = req.params

    if (key === process.env.KEY){
        try {

            db.query(`SELECT * FROM MESSAGES WHERE id = '${id}'`, (err, result) => {
            if (err){
                res.status(400).send(err)
            }

            res.status(201).send(result)

            })

        } catch (err) {
            res.status(500).send(err)
        }
    }
})

// add a message
// whenever we archive a message
router.post('/', async (req, res) =>{

    const { key } = req.headers
    const { id, author, contents, channel, creation_date } = req.body

    if (key === process.env.KEY){
        try {

            db.query(`INSERT INTO MESSAGES(id, author, contents, channel, creation_date) VALUES('${id}', '${author}', '${contents}', '${channel}', '${creation_date}')`,
                (err, result) => {
            if (err){
                res.status(400).send(err)
            }

            res.status(201).send(result)

            })

        } catch (err) {
            res.status(500).send(err)
        }
    }
})

// delete a message
// whenever we un-archive something, delete the corresponding message
router.delete('/:id', async (req, res) => {
    const { key } = req.headers
    const { id } = req.params

    if (key === process.env.KEY) {
        try {

            db.query(`DELETE FROM MESSAGES WHERE id = '${id}'`, (err, result) => {
            if (err){
                res.status(400).send(err)
            }

            res.status(201).send(result)

            })

        } catch (err) {
            res.status(500).send(err)
        }
    }
})



module.exports = router