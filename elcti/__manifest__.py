# -*- coding: utf-8 -*-
{
    'name': "CRM En línea con tu imagen",
    'version': '1.0',
    'depends': [
        'base',
        'contacts',
        'crm',
        'calendar',
        'stock'
    ],
    'author': "Gustavo Torres",
    'category': 'Customizations',
    'description': """
    Este módulo ayuda a las opraciones del programa En Línea Con Tu Imagen, del laboratorio Medix
    """,
    # data files always loaded at installation
    'data': [
        'views/view.xml',
    ],
    # data files containing optionally loaded demonstration data
    #'demo': [
        #'demo/demo_data.xml',
    #],
    'application': True
}