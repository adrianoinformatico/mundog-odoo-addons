# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _compute_print_receipt_url(self):
        for order in self:
            order.print_receipt_url = 'my.bluetoothprint.scheme://%s%s' % (order.get_base_url(), order.get_portal_url(report_type='receipt_json'))

    print_receipt_url = fields.Char(string="Link al recibo", compute='_compute_print_receipt_url',
                                    help="Link para imprimir el ticket de la venta.")
