# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Receta(models.Model):
    _name = 'recetas'
    _description = "Receta"
    
    contacto = fields.Many2one('crm.lead', 'Contacto')