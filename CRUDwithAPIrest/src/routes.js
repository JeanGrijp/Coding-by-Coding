const express = require('express')
const routes = express.Router()
const homeController = require('./controllers/HomeController')



routes.get('/user', homeController.index)
routes.post('/user', homeController.store)

module.exports = routes