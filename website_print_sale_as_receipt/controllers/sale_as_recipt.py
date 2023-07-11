# -*- coding: utf-8 -*-

import json
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.tools import consteq
from odoo import http, SUPERUSER_ID


class SaleAsReceiptController(http.Controller):

    @http.route(['/print_sale_as_receipt/<int:sale_order_id>'], type='http', auth="public", website=True)
    def print_sale_as_receipt(self, sale_order_id, access_token=None):
        try:
            order_sudo = self._document_check_access('sale.order', sale_order_id, access_token=access_token)
        except AccessError as e_a:
            return e_a
        except MissingError as e_m:
            return e_m
        except Exception as e:
            return e
        else:
            sale_order = order_sudo
            sale_order_name = sale_order.name if sale_order else 'ERROR: ORDEN NO ENCONTRADA'
            receipt_json = {
                0: {
                    "type": 0,
                    "content": "ABARROPLUS",
                    "bold": 1,
                    "align": 1,
                    "format": 3
                },
                1: {
                    "type": 0,
                    "content": "Abarrotes en la puerta de tu negocio",
                    "bold": 0,
                    "align": 1,
                    "format": 4
                },
                2: {
                    "type": 4,
                    "content": " <br/> ",
                },
                3: {
                    "type": 0,
                    "content": "ORDEN: %s" % sale_order_name,
                    "bold": 1,
                    "align": 1,
                    "format": 1
                },
                4: {
                    "type": 0,
                    "content": str(sale_order.date_order),
                    "bold": 0,
                    "align": 1,
                    "format": 4
                },
                5: {
                    "type": 0,
                    "content": " ",
                    "bold": 0,
                    "align": 0,
                    "format": 0
                },
                6: {
                    "type": 0,
                    "content": "CANT. DESCRIPCION         PRECIO",
                    "bold": 0,
                    "align": 0,
                    "format": 0
                },
                7: {
                    "type": 0,
                    "content": "--------------------------------",
                    "bold": 0,
                    "align": 0,
                    "format": 0
                },
            }
            for sale_line in sale_order.order_line:
                available_chars = 31
                full_qty = sale_line.product_uom_qty
                int_qty = int(full_qty)
                diff_qty = full_qty - int_qty
                if diff_qty > 0:
                    print_qty = "%.2f" % full_qty
                else:
                    print_qty = "%d" % int_qty
                print_qty = print_qty.rjust(4)
                available_chars -= 4
                print_price = "%.2f" % sale_line.price_total
                available_chars -= len(print_price)
                name_short = sale_line.product_id.name[:available_chars - 2]
                print_name = name_short.ljust(available_chars - 2)
                receipt_json[len(receipt_json)] = {
                    "type": 0,
                    "content": "%s %s %s" % (print_qty, print_name, print_price),
                    "bold": 0,
                    "align": 0,
                    "format": 0
                }
                if sale_line.product_id.default_code:
                    receipt_json[len(receipt_json)] = {
                        "type": 0,
                        "content": "      %s" % sale_line.product_id.default_code[:26],
                        "bold": 0,
                        "align": 0,
                        "format": 4,
                    }
            receipt_json[len(receipt_json)] = {
                "type": 0,
                "content": "--------------------------------",
                "bold": 0,
                "align": 0,
                "format": 0
            }
            receipt_json[len(receipt_json)] = {
                "type": 0,
                "content": "TOTAL: %.2f" % sale_order.amount_total,
                "bold": 1,
                "align": 2,
                "format": 0
            }
            receipt_json[len(receipt_json)] = {
                "type": 4,
                "content": " <br/> ",
                "bold": 0,
                "align": 0,
                "format": 0
            }
            receipt_json[len(receipt_json)] = {
                "type": 0,
                "content": "Cliente: %s" % sale_order.partner_id.name,
                "bold": 0,
                "align": 1,
                "format": 0
            }
            receipt_json[len(receipt_json)] = {
                "type": 4,
                "content": " <br/> <br/> ",
                "bold": 0,
                "align": 0,
                "format": 0
            }
            receipt_json[len(receipt_json)] = {
                "type": 0,
                "content": "CRECE TU NEGOCIO CON NOSOTROS",
                "bold": 1,
                "align": 1,
                "format": 4
            }
            receipt_json[len(receipt_json)] = {
                "type": 0,
                "content": "PRELE: Vende tiempo aire electrónico, recargas y pagos de servicios.",
                "bold": 0,
                "align": 1,
                "format": 4
            }
            receipt_json[len(receipt_json)] = {
                "type": 4,
                "content": " <br/> ",
                "bold": 0,
                "align": 1,
                "format": 0,
            }
            receipt_json[len(receipt_json)] = {
                "type": 0,
                "content": "https://www.prele.com.mx",
                "bold": 0,
                "align": 1,
                "format": 4,
            }
            receipt_json[len(receipt_json)] = {
                "type": 4,
                "content": " <br/> <br/> <br/> <br/> <br/> ",
                "bold": 0,
                "align": 1,
                "format": 0
            }

            json_as_string = json.dumps(receipt_json)
            headers = {'Content-Type': 'application/json'}
            return request.make_response(json_as_string, headers=headers)

    def _document_check_access(self, model_name, document_id, access_token=None):
        document = request.env[model_name].browse([document_id])
        document_sudo = document.with_user(SUPERUSER_ID).exists()
        if not document_sudo:
            raise MissingError("El documento solicitado no existe.")
        try:
            document.check_access_rights('read')
            document.check_access_rule('read')
        except AccessError:
            if not access_token or not document_sudo.access_token or not consteq(document_sudo.access_token, access_token):
                raise
        return document_sudo
