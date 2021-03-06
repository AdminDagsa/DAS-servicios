# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import timedelta
import requests, json

class Receta(models.Model):
    _name = 'recetas'
    _description = "Receta"
    
    contacto = fields.Many2one('crm.lead', 'Contacto')
    edad = fields.Integer('Edad', related="contacto.edad")
    diagnostico = fields.Char('Diagnóstico')
    indicaciones = fields.Text('Indicaciones generales')
    lineas_receta = fields.One2many('lineas.recetas', 'receta', string="Productos", store=True)
    enlace_de_pago = fields.Char('Enlace de pago')
    enlace_dar = fields.Char('Enlace DAR')
    direccion = fields.Char('Dirección')
    pais = fields.Many2one('res.country', string="País")
    estado = fields.Many2one('res.country.state', string="Estado")
    ciudad = fields.Many2one('res.city', string="Ciudad")
    colonia = fields.Char('Colonia')
    cp = fields.Char('C.P.')
    
    @api.onchange('contacto')
    def _poner_direccion(self):
        for record in self:
            if record.contacto != False:
                record.direccion = record.contacto.street
                record.pais = record.contacto.country_id
                record.estado = record.contacto.state_id
                record.ciudad = record.contacto.ciudad
                record.colonia = record.contacto.city
                record.cp = record.contacto.zip
            else:
                record.direccion = None
                record.pais = None
                record.estado = None
                record.ciudad = None
                record.colonia = None
                record.cp = None
    
    payment_type = fields.Char('Tipo de Pago')
    payment_id = fields.Char('Id de Pago')
    payment_status = fields.Char('Estatus')
    payment_amount = fields.Char('Cantidad Pagada')
        
    surtido = fields.Selection([
        ('sfe', 'SFE'),
        ('fz', 'Farmazone'),
        ('no','No surtido')],
        string='Surtido por',
        default = 'no')
    
    def get_LigaFZ(self,record):
        lineItems = []
        productos = record.lineas_receta
        for producto in productos:
            lineItems.append({'SKU':str(producto.producto.barcode),'Cantidad':producto.cantidad})

        parametros={
            "consulta": record.id,
            "planId": "Odoo",
            "lineItems":lineItems,
            "address": [
                {
                    "address1": record.contacto.street,
                    "address2": "",
                    "city": record.contacto.country_id.name,
                    "province/State": record.contacto.state_id.name,
                    "Country": "Mexico",
                    "zip": record.contacto.zip,
                    "firstName": record.contacto.name,
                    "lastName": "",
                    "phone": record.contacto.phone
                }
            ]
        }

        r = requests.post('https://vtech-elcti-api.herokuapp.com/api/generar_liga_pago',json=parametros)
        decode = r.content.decode('utf-8')
        load = json.loads(decode)

        return load['msg']['url'] if load['code']==200 else load['msg']
    
    def get_LigaDAR(self,record):
        lineItems = []
        productos = record.lineas_receta
        for producto in productos:
            lineItems.append({'SKU':str(producto.producto.barcode),'Cantidad':producto.cantidad})
        parametros={
            "idReceta": record.id, 
            "fechaReceta": str(record.create_date), 
            "nombres": record.contacto.nombres,
            "primerApellido": record.contacto.primer_apellido,
            "segundoApellido": record.contacto.segundo_apellido, 
            "email": record.contacto.email_from, 
            "productos": lineItems,
            "medicoNombres": record.create_uid.name, 
            "medicoPrimerApellido": record.create_uid.name, 
            "medicoSegundoApellico": record.create_uid.name, 
            "medicoCodigoPostal":record.create_uid.zip if record.create_uid.zip != "" else "Test" ,
            "medicoCedulaProfesional": "4356789"
        }
        r = requests.post('https://vtech-elcti-api.herokuapp.com/api/generar_liga_pago_dar',json=parametros)
        decode = r.content.decode('utf-8')
        load = json.loads(decode)
        return load["message"]
    
    def obtener_enlaces(self,record):
        record.enlace_de_pago = self.env['recetas'].get_LigaFZ(record)
        record.enlace_dar = self.env['recetas'].get_LigaDAR(record)
        
    def enviar_correo_consulta(self):
        plantilla = self.env.ref('elcti.mail_consulta')
        plantilla.send_mail(self.id, force_send=True)
        
    def fecha_consulta(self):
        dias = {"0":"domingo", "1":"lunes", "2":"martes", "3":"miércoles", "4":"jueves", "5":"viernes", "6":"sábado"}
        meses = {"1":"enero", "2":"febrero", "3":"marzo", "4":"abril", "5":"mayo", "6":"junio", "7":"julio", "8":"agosto", "9":"septiembre", "10":"octubre", "11":"noviembre", "12":"diciembre"}
        tiempo = self.create_date - timedelta(hours=5)
        #return dias[tiempo.strftime("%w")] + ' ' + str(tiempo.strftime("%-d")) + ' de ' + meses[tiempo.strftime("%-m")] + ' de ' + str(tiempo.strftime("%Y")) + ' a las ' + str(tiempo.strftime("%X"))
        return str(tiempo.strftime("%-d")) + ' de ' + meses[tiempo.strftime("%-m")] + ' de ' + str(tiempo.strftime("%Y"))