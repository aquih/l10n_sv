# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import logging

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    retencion_iva = fields.Monetary(string="Retención IVA", compute='_valor_retencion_iva')

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding', 'currency_id', 'company_id', 'date_invoice', 'type')
    def _valor_retencion_iva(self):
        valor = 0
        for tax in self.tax_line_ids:
            if tax.name == 'Retención IVA':
                valor += tax.amount_total
        self.retencion_iva = valor
