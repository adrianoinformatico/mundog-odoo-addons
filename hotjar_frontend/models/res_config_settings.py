# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hotjar_analytics_key = fields.Char(string='Hotjar Tracking Code',
                                       related='website_id.hotjar_analytics_key', readonly=False)
    has_hotjar_analytics = fields.Boolean(string="Hotjar", compute='_compute_has_hotjar_analytics',
                                          inverse='_inverse_has_hotjar_analytics')

    @api.depends('website_id')
    def _compute_has_hotjar_analytics(self):
        for config in self:
            config.has_hotjar_analytics = bool(config.hotjar_analytics_key)

    def _inverse_has_hotjar_analytics(self):
        for config in self:
            if config.has_hotjar_analytics:
                continue
            config.hotjar_analytics_key = False
