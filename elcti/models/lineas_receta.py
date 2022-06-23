# -*- coding: utf-8 -*-
from odoo import fields, models, api

class LineasReceta(models.Model):
    _name = 'lineas.recetas'
    _description = "Lineas de receta"
    
    receta = fields.Many2one('receta', string='Receta')
    producto = fields.Many2one('product.product', string="Producto")
    cantidad = fields.Integer('Cantidad')