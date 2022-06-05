# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CuestionarioLlave(models.Model):
    _inherit = 'calendar.event'
    
    contacto = fields.Many2one('crm.lead', string='Contacto', index=True)