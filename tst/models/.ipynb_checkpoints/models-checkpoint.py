# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from odoo import models, fields, api
import requests

class pedirEnlace(models.Model):
    _inherit = "x_receta"
    
    def getDatos(self):
        parametros={
            "idReceta": "",
            "fechaReceta": "",
            "nombres": "",
            "primerApellido": "",
            "segundoApellido": "",
            "email": "",
            "productos": [
              {
                "sku": 77898787778,
                "cantidad": 1
              }
            ],
            "medicoNombres": "",
            "medicoPrimerApellido": "",
            "medicoSegundoApellico": "",
            "medicoCodigoPostal": "",
            "medicoCedulaProfesional": ""
            }
        
        r = record['x_studio_enlace_de_pago'] = requests.post('https://vtech-elcti-api.herokuapp.com/api/generar_liga_pago',params=parametros)
        return r