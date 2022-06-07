# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ContactosCrm(models.Model):
    _inherit = 'crm.lead'

    acepta_politica = fields.Boolean('Acepta politica de manejo de información personal', default=False, tracking=True)
    nombres = fields.Char('Nombre', index=True, tracking=True)
    primer_apellido = fields.Char('Primer apellido', index=True, tracking=True)
    segundo_apellido = fields.Char('Segundo apellido', index=True, tracking=True)
    fecha_de_nacimiento = fields.Date('Fecha de nacimiento')
    edad = fields.Integer('Edad', index=True, tracking=True, compute="_calcula_edad")
    @api.depends("fecha_de_nacimiento")
    def _calcula_edad(self):
        for record in self:
            if record.fecha_de_nacimiento:
                dias = int(str(datetime.date.today() - record.fecha_de_nacimiento).split(" ")[0])
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
    @api.depends("recordar_meses", "recordar_semanas", "recordar_dias", "recordar_horas", "recordar_minutos")
    def _calcula_recordatorio(self):
        for record in self:
            mes = int(str(datetime.datetime.now()).split("-")[1]) + record.recordar_meses
            record.recordatorio_llamada = datetime.datetime.strptime(str(datetime.datetime.now() + datetime.timedelta(weeks=record.recordar_semanas,days=record.recordar_dias,hours=record.recordar_horas,minutes=record.recordar_minutos)).split("-")[0]+"-"+str(mes)+"-"+str(datetime.datetime.now() + datetime.timedelta(weeks=record.recordar_semanas,days=record.recordar_dias,hours=record.recordar_horas,minutes=record.recordar_minutos)).split("-")[2].split(".")[0], '%Y-%m-%d %H:%M:%S')
            #record["description"] = str(datetime.datetime.now() + datetime.timedelta(weeks=record.x_studio_recordar_en_semanas,days=record.x_studio_recordar_en_dias,hours=record.x_studio_recordar_en_horas,minutes=record.x_studio_retraso)).split("-")[2].split(".")[0]
            """
            dias = int(str(datetime.date.today() - record.x_studio_fecha_de_nacimiento).split(" ")[0])
            edad = int(dias/365)
            record['x_studio_edad'] = str(int((dias - (edad/4) + 1)/365)) + " años"
            """
    sexo = fields.Selection([
        ('H', 'Hombre'),
        ('M', 'Mujer')],
        string='Sexo')
    cuestionario_llave = fields.One2many('cuestionario.llave', 'contacto', string="Cuestionario llave")
    clasificacion_imc = fields.Selection('Clasificacion IMC', related="cuestionario_llave.clasificacion")
    citas = fields.One2many('calendar.event', 'contacto', string="Citas programadas")
    ciudad = fields.Many2one('res.city', string="Ciudad")
    #contacto = fields.Many2one('llamada.contacto', string="Llamada de contacto")
    llamada_contacto = fields.Selection([
        ('1','1er contacto'),
        ('2','2do contacto'),
        ('3','3er contacto'),
        ('4''4to contacto'),
        ('5','5to contacto')],
        string="Llamada de contacto"
    )
    #motivo_cancelacion = fields.Many2one('motivos.cancelacion', string="Motivos de cancelación")
    #conteo_llamadas = fields.Integer('Conteo de llamadas', compute="_conteo_llamadas")
    #def _conteo_llamadas(self):
        #results = self.env['x_llamadas'].read_group([('x_studio_contacto_crm', 'in', self.ids)], ['x_studio_contacto_crm'], ['x_studio_contacto_crm'])
        #dic = {}
        #for x in results: dic[x['x_studio_contacto_crm'][0]] = x['x_studio_contacto_crm_count']
        #for record in self: record['conteo_llamadas'] = dic.get(record.id, 0)