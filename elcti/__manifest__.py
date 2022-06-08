# -*- coding: utf-8 -*-
{
    'name': "CRM En línea con tu imagen",
    'version': '1.0',
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
    'description': """
    Este módulo ayuda a las opraciones del programa En Línea Con Tu Imagen, del laboratorio Medix
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/etapas.xml',
        'data/consultorios.xml',
        'views/elcti_calendario.xml',
        'views/elcti_recetas.xml',
        'views/elcti_farmacovigilancia.xml',
        'views/elcti_cuestionario.xml',
        'views/elcti_llamadas.xml',
        'views/elcti_oportunidades.xml',
        'views/crm_elcti.xml',
    ],
    # data files containing optionally loaded demonstration data
    #'demo': [
        #'demo/demo_data.xml',
    #],
    'application': True
}