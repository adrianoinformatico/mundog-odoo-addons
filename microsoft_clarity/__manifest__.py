# -*- coding: utf-8 -*-
{
    'name': "Integración de Odoo con Microsoft Clarity",
    'summary': """Módulo para integrar odoo con Microsoft Clarity (Análisis de comportamiento de visitantes).""",
    'description': """
    Clarity is a user behavior analytics tool that helps you understand how users interact with your website. Supported features include:
Session Recordings
Heatmaps (or heat maps)
ML Insights
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
