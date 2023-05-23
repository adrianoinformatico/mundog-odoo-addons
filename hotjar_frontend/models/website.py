# -*- coding: utf-8 -*-

from odoo import fields, models


class Website(models.Model):
    _name = "website"
    _inherit = "website"

    hotjar_analytics_key = fields.Char(string='Hotjar Tracking Code')
