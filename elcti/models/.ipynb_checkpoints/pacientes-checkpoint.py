# -*- coding: utf-8 -*-
from odoo import fields, models, api

class LineasReceta(models.Model):
    _inherit = 'crm.lead'
    
    nombres = fields.Char('Nombres')
    primer_apellido = fields.Char('Primer apellido')
    segundo_apellido = fields.Char('Segundo apellido')