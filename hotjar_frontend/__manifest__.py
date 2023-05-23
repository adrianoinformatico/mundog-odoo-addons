# -*- coding: utf-8 -*-
{
    'name': "Integración de Odoo con Hotjar",
    'summary': """Módulo para integrar Odoo con Hotjar.com""",
    'description': """
    Numbers tell you what’s happening. Hotjar’s visual insights tell you why. So you can make the changes that matter.
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
