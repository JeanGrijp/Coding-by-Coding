// index, show, store, update, destroy

const User = require('../models/UserModel')

module.exports = {
    async index(req, res) {
        return res.json({message: "Hello World"})
        // const {name} = req.query
        // const user = await User.find({name})
        // return res.json(user)
    },

    async store(req, res){
        const {name, cpf, data} = req.body
        let user = await User.findOne({name})
        if (!user){
            user = await User.create({name, cpf, data})
        }
        return res.json(user)
    }
}