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
        #'studio_customization',
        #'web_studio',
        #'x_llamadas',
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
        #'security/ir.model.access.csv',
        #'data/carga_inicial.xml',
        'views/views.xml',
        'views/elcti_pacientes_vista.xml',
        #'views/elcti_calendario.xml',
        #'views/elcti_recetas.xml',
        #'views/elcti_farmacovigilancia.xml',
        #'views/elcti_cuestionario.xml',
        #'views/elcti_oportunidades.xml',
        #'views/elcti_llamadas.xml',
        #'views/crm_elcti.xml',
        #'views/elcti_oportunidades_extend.xml',
    ],
    # data files containing optionally loaded demonstration data
    #'demo': [
        #'demo/demo_data.xml',
    #],
    'application': True
}