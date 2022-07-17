/*
* Querying the database function/s.
*
* Used so we dont unecessarily repeat code.
* */

const { db } = require('./connection')

module.exports = (sql, res) => {
    db.query(sql, (err, result) => {
        if (err){
            res.status(400).send(err)
        }

        res.status(201).send(result)

    })
}