const sql = require('mysql2')
const path = require('path')
require('dotenv').config({path:path.resolve(__dirname, './../.env')})

// TODO:
//  develop this in a vm and use dev user n stuff
module.exports = sql.createConnection({
    host: process.env.HOST,
    user: process.env.USER,
    password: process.env.PASSWORD,
    database: 'Waycord'
})