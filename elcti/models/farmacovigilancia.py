# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CuestionarioLlave(models.Model):
    _name = "farmacovigilancia"
    _description = "Farmacovigilancia"

    nombre = fields.Char('Nombre', index=True)
    celular_notificador = fields.Char('Celular')
    telefono_fijo = fields.Char('Teléfono fijo')
    lote = fields.Char('Lote')
    producto = fields.Char('Nombre del producto')
    laboratorio = fields.Char('Laboratorio')
    nombre_consumidor = fields.Char('Nombre')
    dolor_de_cabeza = fields.Boolean('Dolor de cabeza')
    nauseas = fields.Boolean('Nauseas')
    aumento_sueno = fields.Boolean('Aumento de sueño')
    alteraciones_piel = fields.Boolean('Alteraciones en la piel')
    mareos = fields.Boolean('Mareos')
    ardor_estomago = fields.Boolean('Ardor de estómago')
    vomito = fields.Boolean('Vómito')
    diarrea = fields.Boolean('Diarrea')
    sangrado = fields.Boolean('Sangrado')
    comezon = fields.Boolean('Comezón')
    inicio = fields.Date('Inicio')
    fin = fields.Date('Fin')
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    caducidad = fields.Date('Fecha de caducidad')
    peso = fields.Float('Peso (Kg)')
    talla = fields.Float('Talla (m)')
    sexo = fields.Selection([
        ('H', 'Hombre'),
        ('M', 'Mujer')],
        string='Sexo')