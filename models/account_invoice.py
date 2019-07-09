# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import logging

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    retencion_iva = fields.Monetary(string="Retención iva", compute='_valor_retencion_iva')

    def _valor_retencion_iva(self):
        valor = 0
        for tax in self.tax_line_ids:
            if tax.name == 'Retención IVA':
                valor = tax.amount_total
        return valor
