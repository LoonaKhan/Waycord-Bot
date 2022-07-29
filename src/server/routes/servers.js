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
    const {id} = req.params

    if (key === process.env.KEY) { // if the key is invalid

        try {
            db.execute(`SELECT * FROM SERVERS WHERE id = ?`,
                [id],
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

// add a server
// Used when the bot first joins a server.
router.post('/', async (req, res) => {

    const {key} = req.headers
    const { member_count, creation_date, boost_level } = req.body

    if (key === process.env.KEY){
        try {

        db.execute(`INSERT INTO SERVERS (member_count, creation_date, boost_level) VALUES(?, ?, ?)`,
            [member_count, creation_date, boost_level],
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

// update a server
// attempts to be used whenever a bot command is used in a server
router.put('/:id', async (req, res) => {

    const {key} = req.headers
    const { id } = req.params
    const { member_count, boost_level } = req.body

    if (key === process.env.KEY){
        try {

        db.execute(`UPDATE SERVERS SET member_count = ?, boost_level = ? WHERE id = ?`,
            [member_count, boost_level, id],
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

// delete a server
// todo: allow the admins to blacklist a server from being tracked?
router.delete('/:id', async  (req, res) => {

    const { key } = req.headers
    const { id } = req.params

    if (key === process.env.KEY) {

        try {

            db.execute(`DELETE FROM SERVERS WHERE id = ?`,
                [id],
                (err, result) =>{

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