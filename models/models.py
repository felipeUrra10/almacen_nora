# -*- coding: utf-8 -*-

from odoo import models, fields


class Cliente(models.Model):
    _name = 'almacen_nora.cliente'
    _description = 'almacen_nora.almacen_nora'
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre del cliente")
    apellido = fields.Char("Apellido del cliente")
    rut = fields.Char("Rut del cliente")
    venta_ids = fields.One2many('almacen_nora.venta', 'cliente_id')

class Venta(models.Model):
    _name = 'almacen_nora.venta'
    _description = 'Ventas del almacen'

    fecha_venta =fields.Date("fecha de venta")
    total_venta = fields.Integer("Total de venta")
    detalle_venta_ids = fields.One2many('almacen_nora.detalle_venta', 'venta_id')
    cliente_id =fields.Many2one('almacen_nora.cliente', 'Clientes')

class Detalle_Venta(models.Model):
    _name ='almacen_nora.detalle_venta'
    _description = 'detallle de ventas del almacen nora'

    cantidad = fields.Integer("cantidad")
    total_cantidad =fields.Integer("Total por cantidad")
    venta_id = fields.Many2one('almacen_nora.venta', 'Venta')
    producto_id = fields.Many2one('almacen_nora.producto', 'producto')

class Producto(models.Model):
    _name ='almacen_nora.producto'
    _description ='descripcion del producto'

    nombre_producto= fields.Char("nombre del producto")
    precio = fields.Integer("precio del producto")
    stock = fields.Integer("stock del producto")
    Detalle_Venta_ids = fields.One2many('almacen_nora.detalle_venta', 'producto_id')





