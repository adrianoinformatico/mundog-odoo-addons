# -*- coding: utf-8 -*-
{
    'name': "Imprimir venta como recibo",
    'summary': """Módulo que permite imprimir la venta como un recibo de punto de venta""",
    'description': """
    Permite integrar la impresión de la venta como un recibo de punto de venta mediante impresoras térmicas.
    https://play.google.com/store/apps/details?id=mate.bluetoothprint
    """,
    'author': "Adriano Borrego",
    'website': "https://www.linkedin.com/in/adrian-borrego-dom%C3%ADnguez-399212a3/",
    'category': 'Hidden',
    'version': '16.0',
    'depends': ['website_sale',
                ],
    'data': ['views/sale_order_views.xml',
             'views/sale_portal_templates.xml',
             'views/website_sale_templates.xml',
             ],
    'application': True,
    'license': 'LGPL-3',
}
