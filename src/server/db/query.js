/*
* Querying the database function/s.
*
* Used so we dont unecessarily repeat code.
*
* TODO: 
*   DOES NOT WORK. 
*   works without using a seperate function
*   something about a function call
*   maybe because of res?
*   maybe return the err or result as well as a status instead of trying to respond.
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
