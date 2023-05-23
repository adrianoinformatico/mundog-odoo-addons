# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    microsoft_clarity_analytics_key = fields.Char(string='Microsoft Clarity Tracking Code',
                                                  related='website_id.microsoft_clarity_analytics_key', readonly=False)
    has_microsoft_clarity_analytics = fields.Boolean(string="Microsoft Clarity",
                                                     compute='_compute_has_microsoft_clarity_analytics',
                                                     inverse='_inverse_has_microsoft_clarity_analytics')

    @api.depends('website_id')
    def _compute_has_microsoft_clarity_analytics(self):
        for config in self:
            config.has_microsoft_clarity_analytics = bool(config.microsoft_clarity_analytics_key)

    def _inverse_has_microsoft_clarity_analytics(self):
        for config in self:
            if config.has_microsoft_clarity_analytics:
                continue
            config.microsoft_clarity_analytics_key = False
