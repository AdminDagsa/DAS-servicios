# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Calendario_tipo(models.Model):
    _inherit = 'calendar.event.type'
    
    direccion = fields.Char('Direccion', store=True)