/*
* Querying the database function/s.
*
* Used so we dont unecessarily repeat code.
* */

const { db } = require('connection')

module.exports = (queryString, res) => {
    db.query(queryString, (err, result) => {
        if (err){
            res.status(400).send(err)
        }

        res.status(201).send(result)

    })
}