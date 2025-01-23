from odoo import models, fields
from .afip_cae import AfipCAE  # Importa la clase que genera el QR

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    
    afip_cae_qr = fields.Binary(string="QR CAE", compute="_compute_afip_cae_qr")

    def _compute_afip_cae_qr(self):
        for record in self:
            cae_number = record.x_cae_number
            cae_due_date = record.x_cae_due_date
            record.afip_cae_qr = AfipCAE.generate_qr(cae_number, cae_due_date)
