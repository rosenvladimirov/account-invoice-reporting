# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Invoice sum of line quantity',
    'version': '11.0.1.0',
    'category': 'Accounting',
    'summary': 'Add total for quantity on lines',
    'description': """
    """,
    'depends': ['account'],
    'data': [
        'views/account_invoice_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
