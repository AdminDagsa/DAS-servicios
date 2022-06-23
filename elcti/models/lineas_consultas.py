# -*- coding: utf-8 -*-
from odoo import fields, models, api

class LineasConsulta(models.Model):
    _name = 'lineas.consultas'
    _description = "Lineas de consulta"
    
    consulta = fields.Many2one('consultas', string='Consulta')
    producto = fields.Many2one('product.product', string="Producto")
    cantidad = fields.Integer('Cantidad')