# -*- coding: utf-8 -*-

import re
from odoo import fields, models, api


class Website(models.Model):
    _name = "website"
    _inherit = "website"

    @api.depends("matomo_analytics_host")
    def compute_matomo_analytics_host_normalized(self):
        for this in self:
            if this.matomo_analytics_host:
                host1 = re.sub(r'^https?:\/\/', '', this.matomo_analytics_host.strip())
                host1 = re.sub('\/$', '', host1)
                this.matomo_analytics_host_normalized = host1
            else:
                this.matomo_analytics_host_normalized = ''

    matomo_analytics_key = fields.Char(string='Matomo Analytics Site ID')
    matomo_analytics_host = fields.Char(string='Servidor Matomo (URL)')
    matomo_analytics_host_normalized = fields.Char(string="Servidor Matomo (solo URL)", readonly=True,
                                                   compute=compute_matomo_analytics_host_normalized)
