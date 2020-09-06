const mongoose = require('mongoose')

const UserSchema = new mongoose.Schema({
    name: {type: String, required: true},
    cpf: String,
    data: String
})

module.exports = mongoose.model('User', UserSchema)