# -*- coding: utf-8 -*-
{
    'name': "CRM En línea con tu imagen",
    'version': '14.01',
    'depends': [
        'base',
        'contacts',
        'crm',
        'calendar',
        'stock',
    ],
    'author': "Gustavo Torres",
    'category': 'Customizations',
    #'website':"https://veritatech.odoo.com/",
    'description': """
    Este módulo ayuda a las opraciones del programa En Línea Con Tu Imagen
    """,
    'summary':"""
    Este módulo ayuda a las opraciones del programa En Línea Con Tu Imagen
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/carga_inicial.xml',
        'views/elcti_pacientes_vista.xml',
        'views/elcti_citas_vista.xml',
        'views/elcti_llamadas_vista.xml',
        'views/elcti_recetas_vista.xml',
        'views/elcti_farmacovigilancia_vista.xml',
        'views/elcti_cuestionario_vista.xml',
        'views/elcti_consultorios_vista.xml',
        'views/menu.xml',
        'views/elcti_pacientes_vista_extend.xml',
        'data/mail_consulta.xml',
        'data/mail_cita.xml',
        'data/automatizaciones.xml',
    ],
    'application': True
}