# -*- coding: utf-8 -*-

from odoo.addons.sale.controllers.portal import CustomerPortal
from .sale_as_recipt import SaleAsReceiptController

class CustomerPortal(CustomerPortal):

    def portal_order_page(self, order_id, report_type=None, access_token=None, message=False, download=False, **kw):
        if report_type == 'receipt_json':
            new_sale_report_json = SaleAsReceiptController()
            return new_sale_report_json.print_sale_as_receipt(order_id, access_token)
        else:
            return super(CustomerPortal, self).portal_order_page(order_id, report_type, access_token, message, download, **kw)
