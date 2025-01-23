from io import BytesIO
import base64
import qrcode
from odoo import models, fields

class AfipCAE(models.Model):
    _name = 'afip.cae'
    
    @staticmethod
    def generate_qr(cae_number, cae_due_date):
        qr_data = f"CAE: {cae_number}\nFecha de Vencimiento CAE: {cae_due_date}"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")  # Especificamos el formato de la imagen
        qr_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return qr_b64
