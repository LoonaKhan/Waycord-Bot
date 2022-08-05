/*
* Archive endpoints.
*
* Archives are the main data of an app.
*
* The archives are made up of:
*   id
*   title
*   creator(id)
*   message(id)
*   creation_date
* all the id's are references to another db object
* */

const { Router } = require('express')
const db = require('../db/connection')
const path = require('path')
require('dotenv').config({path: path.resolve(__dirname, '../.env')})

const router = Router()



// get an archive/s with matching titles.
// whenever the user wants to get a specifc archive/s
// requires title and creator id, user searches their own archives by name.
router.get('/:creator_id/filter', async (req, res) => {
    const {key} = req.headers
    const {creator_id} = req.params
    const {title} = req.body

    if (key === process.env.KEY) {

        try {
            db.execute(`SELECT * FROM ARCHIVES WHERE creator = ? AND title LIKE ? ORDER BY id ASC`,
                [creator_id, `%${title}%`],
                (err, result) => {
                if (err) {
                    res.status(400).send(err)
                }

                res.status(201).send(result)
            })
        } catch (err) {
            res.status(500).send(err)
        }
    }
})

// get all archives from a specific user
// when the user wants all their archives
// requires creator id
router.get('/:creator_id', async (req, res) => {
    const {key} = req.headers
    const {creator_id} = req.params

    if (key === process.env.KEY) {

        try {
            db.execute(`SELECT * FROM ARCHIVES WHERE creator = ?`,
                [creator_id],
                (err, result) => {
                if (err) {
                    res.status(400).send(err)
                }

                res.status(201).send(result)
            })
        } catch (err) {
            res.status(500).send(err)
        }
    }
})

// add an archive
//takes in a title, message id, owner id ad creation_date.
router.post('/', async (req, res) => {
    const {key} = req.headers
    const {creator_id, title, message_id, creation_date} = req.body

    if (key === process.env.KEY) {

        try {
            db.execute(`INSERT INTO ARCHIVES(title, creator, message_id, creation_date) VALUES(?, ?, ?, ?)`,
                [title, creator_id, message_id, creation_date],
                (err, result) => {
                if (err) {
                    res.status(400).send(err)
                }

                res.status(201).send(result)
            })
        } catch (err) {
            res.status(500).send(err)
        }
    }
})

// delete an archive
// user wants to get rid of one
// can delete by title, or id.
router.delete('/:id', async (req, res) => {

    const {key} = req.headers
    const {id} = req.params
    const { creator } = req.body

    if (key === process.env.KEY) {

        try {
            db.execute(`DELETE FROM ARCHIVES WHERE id = ? AND creator = ?`,
                [id, creator],
                (err, result) => {
                if (err) {
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