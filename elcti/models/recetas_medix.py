# -*- coding: utf-8 -*-
from odoo import fields, models, api

class RecetasMedix(models.Model):
    _name = "recetas.medix"
    _description = "Recetas"

    active = fields.Boolean('Activo', default=True)
    nombre = fields.Char('Nombre', index=True)
    contacto = fields.Many2one('crm.lead', string='Contacto', index=True)
    edad = fields.Integer('Edad', related="contacto.edad")
    diagnostico = fields.Char('Diagnóstico')
    indicaciones = fields.Text('Indicaciones generales')
    lineas_receta = fields.One2many('lineas.recetas.medix', 'receta', string="Productos")
    enlace_de_pago = fields.Char('Enlace de pago')
    enlace_dar = fields.Char('Enlace DAR')
    direccion = fields.Char('Dirección', related="contacto.street")
    pais = fields.Many2one('res.country', string="País", related="contacto.country_id")
    estado = fields.Many2one('res.country.state', string="Estado", related="contacto.state_id")
    ciudad = fields.Many2one('res.city', string="Ciudad", related="contacto.ciudad")
    colonia = fields.Char('Colonia', related="contacto.city")
    cp = fields.Char('C.P.', related="contacto.zip")
    surtido = fields.Selection([
        ('sfe', 'SFE'),
        ('fz', 'Farmazone'),
        ('no','No surtido')],
        string='Surtido por')