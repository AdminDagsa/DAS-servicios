# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CalendarioCitas(models.Model):
    _inherit = 'calendar.event'
    
    contacto = fields.Many2one('crm.lead', string='Contacto', index=True)
    consultorio = fields.Char('Consultorio', store=True, related="categ_ids.name")