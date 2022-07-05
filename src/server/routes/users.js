const { Router } = require('express')
const db = require('../db/connection')

const router = Router()

router.get('/',  async (req, res) => { // test response

    try {

        res.status(201).send("hi")

    } catch (err) {
        res.status(500).send(err)
    }

})



module.exports = router