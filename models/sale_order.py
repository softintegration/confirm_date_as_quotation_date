# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_confirmation_values(self):
        res = super(SaleOrder, self)._prepare_confirmation_values()
        res.update({'date_order':self.mapped("date_order")[0]})
        return res
