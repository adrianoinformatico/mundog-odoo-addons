# -*- coding: utf-8 -*-

from odoo import fields, models


class Website(models.Model):
    _name = "website"
    _inherit = "website"

    microsoft_clarity_analytics_key = fields.Char(string='Microsoft Clarity Tracking Code')
