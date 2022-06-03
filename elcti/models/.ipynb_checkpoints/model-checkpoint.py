# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'crm.lead'

    acepta_politica = fields.Boolean('Acepta politica de manejo de información personal', default=False, tracking=True)
