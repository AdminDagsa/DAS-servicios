# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CuestionarioLlave(models.Model):
    _name = "recetas.medix"
    _description = "Recetas"

    active = fields.Boolean('Activo', default=True)
    nombre = fields.Char('Nombre', index=True)
    contacto = fields.Many2one('crm.lead', string='Contacto', index=True)
    diagnostico = fields.Char('Diagnóstico')
    indicaciones = fields.Text('Indicaciones generales')
    lineas_receta = fields.One2many('lineas.recetas.medix', 'receta', string="Productos")
    enlace_de_pago = fields.Char('Enlace de pago')
    enlace_dar = fields.Char('Enlace DAR')
    direccion = fields.Char('Dirección')
    pais = fields.Many2one('res.country', string="País")
    estado = fields.Many2one('res.country.state', string="Estado")
    ciudad = fields.Many2one('res.city', string="Ciudad")
    colonia = fields.Char('Colonia')
    cp = fields.Char('C.P.')