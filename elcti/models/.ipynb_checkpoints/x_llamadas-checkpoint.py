# -*- coding: utf-8 -*-
from odoo import fields, models, api

class LlamadasMedix(models.Model):
    _inherit = 'x_llamadas'
    
    contacto = fields.Many2one('crm.lead', string='Contacto', index=True)