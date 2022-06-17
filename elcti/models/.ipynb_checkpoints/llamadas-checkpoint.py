# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import datetime
from datetime import timedelta

class Llamadas(models.Model):
    _name = "llamadas"
    _description = "Llamadas"

    contacto = fields.Many2one('crm.lead', string='Contacto')
    fecha_de_nacimiento = fields.Date('Fecha de nacimiento', related="contacto.fecha_de_nacimiento", readonly=False)
    sexo = fields.Selection([
        ('H', 'Hombre'),
        ('M', 'Mujer')],
        string='Sexo',
        related="contacto.sexo",
        readonly=False)
    correo = fields.Char('Correo electrónico', related="contacto.email_from", readonly=False)
    telefono = fields.Char('Teléfono', related="contacto.phone", readonly=False)
    direccion = fields.Char('Dirección', related="contacto.street", readonly=False)
    pais = fields.Many2one('res.country', string="País", related="contacto.country_id", readonly=False)
    estado = fields.Many2one('res.country.state', string="Estado", related="contacto.state_id", readonly=False)
    ciudad = fields.Many2one('res.city', string="Ciudad", related="contacto.ciudad", readonly=False)
    colonia = fields.Char('Colonia', related="contacto.city", readonly=False)
    cp = fields.Char('C.P.', related="contacto.zip", readonly=False)
    acepta_politica = fields.Boolean('Acepta politica de manejo de información personal', related="contacto.acepta_politica", readonly=False)
    llamada_contacto = fields.Selection((
        ('1', '1er contacto'),
        ('2', '2do contacto'),
        ('3', '3er contacto'),
        ('4', '4to contacto'),
        ('5', '5to contacto')),
        string='Llamada de contacto',
        related="contacto.llamada_contacto",
        readonly=False)
    recordar_meses = fields.Integer(related="contacto.recordar_meses", readonly=False)
    recordar_semanas = fields.Integer(related="contacto.recordar_semanas", readonly=False)
    recordar_dias = fields.Integer(related="contacto.recordar_dias", readonly=False)
    recordar_horas = fields.Integer(related="contacto.recordar_horas", readonly=False)
    recordar_minutos = fields.Integer(related="contacto.recordar_minutos", readonly=False)
    inicio_llamada = fields.Datetime('Inicio de llamada')
    fin_llamada = fields.Datetime('Fin de llamada')
    direccion_llamada = fields.Selection([
        ('in','Entrante'),
        ('out','Saliente')],
        string="Direccion de llamada")
    def llamada_entrante(self):
        for record in self:
            record.direccion_llamada = 'in'
            record.inicio_llamada = datetime.now()
    def llamada_saliente(self):
        for record in self:
            record.direccion_llamada = 'out'
            record.inicio_llamada = datetime.now()
    codigo_cierre = fields.Selection([
        ('si','Resuelto'),
        ('no','Sin resolver'),
        ('otro','Otro, se abre incidencia')],
        string="Código de cierre")
    duracion_llamada = fields.Char('Duración de llamada')
    def finalizar_llamada(self):
        for record in self:
            record.fin_llamada = datetime.now()
            #if record.fin_llamada != None and record.inicio_llamada != None:
            record.duracion_llamada = str(record.fin_llamada - record.inicio_llamada)
    resumen = fields.Char('Resumen')
    descripcion = fields.Char('Descripción')
    #cuestionario_llave = fields.One2many('cuestionario.llave', 'contacto', string="Cuestionario llave", related="contacto.cuestionario_llave", readonly=False)
    #citas = fields.One2many('calendar.event', 'contacto', string="Citas programadas", related="contacto.citas", readonly=False)
    cuestionario_llave = fields.One2many('cuestionario.llave', 'llamada', string="Cuestionario llave")
    citas = fields.One2many('calendar.event', 'llamada', string="Citas programadas")