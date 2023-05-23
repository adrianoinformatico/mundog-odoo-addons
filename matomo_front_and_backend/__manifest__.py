# -*- coding: utf-8 -*-
{
    'name': "Integración de Odoo con Matomo Frontend y Backend",
    'summary': """Módulo para integrar odoo con Matomo.""",
    'description': """
    Funciona en el backend y en el frontend
    """,

    'author': "Adriano Borrego",
    'website': "https://www.linkedin.com/in/adrian-borrego-dom%C3%ADnguez-399212a3/",

    'category': 'Hidden',
    'version': '16.0',

    'depends': ['website',
                ],

    'data': ['views/res_config_settings_views.xml',
             'views/website_templates.xml',
             ],
    'application': True,
    'license': 'LGPL-3',
}
