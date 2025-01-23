{
    'name': 'Odoo AFIP CAE',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Genera QR y muestra el CAE en el footer de las facturas',
    'description': 'Este módulo genera un QR en el footer de la factura y muestra el número y fecha de vencimiento del CAE.',
    'author': 'Nahuel Dumo',
    'depends': ['account'],
    'data': [
        'views/invoice_template.xml',
    ],
    'installable': True,
    'application': False,
}
