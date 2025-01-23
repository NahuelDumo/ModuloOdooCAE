from odoo import models, fields
import qrcode
from io import BytesIO
import base64

class AfipCAE(models.Model):
    _name = 'afip.cae'
    
    @staticmethod
    def generate_qr(cae_number, cae_due_date):
        qr_data = f"CAE: {cae_number}\nFecha de Vencimiento CAE: {cae_due_date}"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer)
        qr_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return qr_b64

