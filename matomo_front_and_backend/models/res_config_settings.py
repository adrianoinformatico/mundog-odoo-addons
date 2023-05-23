# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    matomo_analytics_key = fields.Char(string='Matomo Analytics Site ID', related='website_id.matomo_analytics_key',
                                       readonly=False)
    matomo_analytics_host = fields.Char(string='Servidor Matomo (URL)', related='website_id.matomo_analytics_host',
                                        readonly=False)
    has_matomo_analytics = fields.Boolean(string="Matomo", compute='_compute_has_matomo_analytics',
                                          inverse='_inverse_has_matomo_analytics')
    matomo_analytics_host_normalized = fields.Char(string="Servidor Matomo (solo URL)", readonly=True,
                                                   related='website_id.matomo_analytics_host_normalized')

    @api.depends('website_id')
    def _compute_has_matomo_analytics(self):
        for config in self:
            config.has_matomo_analytics = bool(config.matomo_analytics_key)

    def _inverse_has_matomo_analytics(self):
        for config in self:
            if config.has_matomo_analytics:
                continue
            config.matomo_analytics_key = False
