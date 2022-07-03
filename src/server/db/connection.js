const sql = require('mysql2')
const Process = require('process')
const { dotenv } = require('dotenv')

// TODO:
//  develop this in a vm and use dev user n stuff
module.exports = sql.createConnection({
    host: 'localhost',
    user: `${process.env.USERNAME}`,
    password: `${process.env.PASSWORD}`,
    database: 'Waycord'
})