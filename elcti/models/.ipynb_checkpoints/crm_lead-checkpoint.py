# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import datetime
from datetime import date
from datetime import timedelta

class Pacientes(models.Model):
    _inherit = 'crm.lead'
    
    nombres = fields.Char('Nombres', tracking=True)
    primer_apellido = fields.Char('Primer apellido', tracking=True)
    segundo_apellido = fields.Char('Segundo apellido', tracking=True)
    etapa = fields.Char('Etapa', related="stage_id.name", store=True, tracking=True)
    acepta_politica = fields.Boolean('Acepta politica de manejo de información personal', tracking=True)
    fecha_de_nacimiento = fields.Date('Fecha de nacimiento', tracking=True)
    edad = fields.Integer('Edad', index=True, tracking=True, compute="_calcula_edad")
    @api.depends()
    def _calcula_edad(self):
        for record in self:
            if record.fecha_de_nacimiento:
                dias = int(str(date.today() - record.fecha_de_nacimiento).split(" ")[0])
                edad = int(dias/365)
                record.edad = int((dias - (edad/4) + 1)/365)
            else:
                record.edad = None
    recordar_meses = fields.Integer()
    recordar_semanas = fields.Integer()
    recordar_dias = fields.Integer()
    recordar_horas = fields.Integer()
    recordar_minutos = fields.Integer()
    recordatorio_llamada = fields.Datetime('Recordar en', compute="_calcula_recordatorio")
    @api.depends()
    def _calcula_recordatorio(self):
        for record in self:
            mes = int(str(datetime.now()).split("-")[1]) + record.recordar_meses
            record.recordatorio_llamada = datetime.strptime(str(datetime.now() + timedelta(weeks=record.recordar_semanas,days=record.recordar_dias,hours=record.recordar_horas,minutes=record.recordar_minutos)).split("-")[0]+"-"+str(mes)+"-"+str(datetime.now() + timedelta(weeks=record.recordar_semanas,days=record.recordar_dias,hours=record.recordar_horas,minutes=record.recordar_minutos)).split("-")[2].split(".")[0], '%Y-%m-%d %H:%M:%S')
    sexo = fields.Selection([
        ('H', 'Hombre'),
        ('M', 'Mujer')],
        string='Sexo')
    cuestionario_llave = fields.One2many('cuestionario.llave', 'contacto', string="Cuestionario llave")
    clasificacion_imc = fields.Selection('Clasificacion IMC', related="cuestionario_llave.clasificacion")
    citas = fields.One2many('calendar.event', 'contacto', string="Citas programadas")
    llamadas = fields.One2many('llamadas', 'contacto', string="Llamadas")
    ciudad = fields.Many2one('res.city', string="Ciudad")
    llamada_contacto = fields.Selection([
        ('1', '1er contacto'),
        ('2', '2do contacto'),
        ('3', '3er contacto'),
        ('4', '4to contacto'),
        ('5', '5to contacto')],
        string='Llamada de contacto')
    #motivo_cancelacion = fields.Many2one('motivos.cancelacion', string="Motivos de cancelación")
    conteo_citas = fields.Integer('Citas agendadas', compute="_conteo_citas")
    def _conteo_citas(self):
        for record in self:
            record.conteo_citas = self.env['calendar.event'].search_count([('contacto', '=', self.id)])
    conteo_llamadas = fields.Integer('Conteo de llamadas', compute="_conteo_llamadas")
    def _conteo_llamadas(self):
        for record in self:
            record.conteo_llamadas = self.env['llamadas'].search_count([('contacto', '=', self.id)])
    def concatenar_nombre(self,record):
        if record.nombres and record.primer_apellido and record.segundo_apellido:
            record.name = record.nombres + ' ' + record.primer_apellido + ' ' + record.segundo_apellido
        elif record.nombres and record.primer_apellido:
            record.name = record.nombres + ' ' + record.primer_apellido
        elif record.nombres and record.segundo_apellido:
            record.name = record.nombres + ' ' + record.segundo_apellido
        elif record.primer_apellido and record.segundo_apellido:
            record.name = record.primer_apellido + ' ' + record.segundo_apellido
        elif record.nombres:
            record.name = record.nombres
        elif record.primer_apellido:
            record.name = record.primer_apellido
        elif record.segundo_apellido:
            record.name = record.segundo_apellido