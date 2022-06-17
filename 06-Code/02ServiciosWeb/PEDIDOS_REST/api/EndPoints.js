const PedidosController = require('../controller/Pedido')
const express = require('express')
const router = express.Router()

//CRUD

router.post('/add',PedidosController.createPedidos)
router.get('/all',PedidosController.getPedidos)
router.put('/updatePedido',PedidosController.updatePedidos)
router.delete('/deletePedido', PedidosController.deletePedidos)
router.get('/DateOrder', PedidosController.DateOrder)

module.exports = router