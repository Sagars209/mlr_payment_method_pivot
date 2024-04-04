# -*- coding: utf-8 -*-

from functools import partial

from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"
    payment_method_id = fields.Many2one(
                'pos.payment', string='Payment', readonly=True)
    payment_id = fields.Many2one('pos.payment.method', string='payment_method_id')

    def _select(self):
        return super(PosOrderReport, self)._select() + """
                ,pp.payment_method_id AS payment_id, pp.payment_method_id
        """

    def _from(self):
        return super(PosOrderReport, self)._from() + """
                LEFT JOIN pos_payment pp ON (s.id=pp.pos_order_id)
        """

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ',pp.payment_method_id'
