# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class Calendario(models.Model):
    _inherit = 'calendar.event'
    
    estatus = fields.Selection([
        ('Atendida','Atendida'),
        ('No atendida','No atendida'),
        ('Cancelada','Cancelada'),
        ('Reagendada','Reagendada')],
        string="Estatus"
    )
    contacto = fields.Many2one('crm.lead', "Contacto")
    consultorio = fields.Char('Consultorio', store=True, related="categ_ids.name")
    llamada = fields.Many2one('llamadas', string='Llamada')
    temperatura = fields.Char('Temperatura corporal (°C)')
    frec_resp = fields.Char('Frecuencia respiratoria')
    frec_card = fields.Char('Frecuencia cardiaca')
    presion = fields.Char('Presión arterial')
    peso = fields.Float('Peso (Kg)')
    talla = fields.Float('Altura (m)')
    imc = fields.Float('IMC',compute="_imc")
    @api.depends()
    def _imc(self):
        for record in self:
            if record.peso > 0 and record.talla > 0:
                record.imc = record.peso / (record.talla**2)
            else:
                record.imc = 0
    clasificacion = fields.Selection([
        ('1','Normopeso'),
        ('2','Sobrepeso'),
        ('3','Obesidad grado I'),
        ('4','Obesidad grado II'),
        ('5','Obesidad grado III'),
        ('6','Obesidad grado IV')],
        string="Clasificación IMC",
        compute="_calcula_imc"
    )
    @api.depends()
    def _calcula_imc(self):
        for record in self:
            if record.imc > 0:
                if record.imc > 18.49 and record.imc < 24.99:
                    record.clasificacion = "1"
                elif record.imc < 29.99:
                    record.clasificacion = "2"
                elif record.imc < 34.99:
                    record.clasificacion = "3"
                elif record.imc < 39.99:
                    record.clasificacion = "4"
                elif record.imc < 49.99:
                    record.clasificacion = "5"
                elif record.imc > 50:
                    record.clasificacion = "6"
            else:
                record.clasificacion = None
    grasa = fields.Float('Porcentaje de grasa')
    pecho = fields.Float('Pecho/busto')
    cintura = fields.Float('Cintura')
    cadera = fields.Float('Cadera')
    nota_psicologia = fields.Text('Observaciones psicologo')
    nota_medicina = fields.Text('Observaciones médicas')
    nota_nutricion = fields.Text('Observaciones nutricionales')
    
    def nombre_cita(self,record):
        #raise UserError(record.contacto.name)
        if record.contacto.name != False:
            #raise UserError(record.contacto.name)
            record.name = record.contacto.name
            
    def enviar_correo_cita(self):
        plantilla = self.env.ref('calendar.model_calendar_event')
        plantilla.send_mail(self.id, force_send=True)
        
    def fecha_cita(self):
        dias = {"0":"domingo", "1":"lunes", "2":"martes", "3":"miércoles", "4":"jueves", "5":"viernes", "6":"sábado"}
        meses = {"1":"enero", "2":"febrero", "3":"marzo", "4":"abril", "5":"mayo", "6":"junio", "7":"julio", "8":"agosto", "9":"septiembre", "10":"octubre", "11":"noviembre", "12":"diciembre"}
        tiempo = self.start - timedelta(hours=5)
        return dias[tiempo.strftime("%w")] + ' ' + str(tiempo.strftime("%-d")) + ' de ' + meses[tiempo.strftime("%-m")] + ' de ' + str(tiempo.strftime("%Y")) + ' a las ' + str(tiempo.strftime("%X"))
    
    @api.onchange('categ_ids', 'start', 'duration')
    def _ubicacion(self):
        for record in self:
            if record.categ_ids:
                record.location = record.categ_ids.direccion
            else:
                record.location = None
            record.stop = record.start + timedelta(hours=record.duration)