// index, show, store, update, destroy

const User = require('../models/UserModel')
const { update } = require('../models/UserModel')

module.exports = {
    async index(req, res) {
        // return res.json({message: "Hello World"})
        const {name} = req.query
        const user = await User.find({name})
        return res.json(user)
    },

    async store(req, res){
        
        const {name} = req.body
        const {cpf} = req.body
        const {data} = req.body
        let user = await User.findOne({name})
        if (!user){
            user = await User.create({name, cpf, data})
        }
        return res.json(user)
    },

    // async update(req, res) {
    //     const {name, cpf, data} = req.body
    //     let user = await User.findOne({name})
    //     // if (user){
    //     //     user = User.updateOne()
    //     // }
    // }
}