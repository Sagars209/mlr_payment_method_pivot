# -*- coding: utf-8 -*-

from functools import partial

from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"
    payment_method_id = fields.Many2one(
                'pos.payment', string='payment_method_id', readonly=True)

    def _select(self):
        return super(PosOrderReport, self)._select() + ',s.payment_method_id AS payment_method_id'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ',s.payment_method_id'