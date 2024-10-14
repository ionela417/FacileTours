{
    'name': 'My Custom Module',
    'version': '1.0',
    'summary': 'Custom Module for Odoo',
    'description': """Module description""",
    'category': 'Custom',
    'author': 'Your Name',
    'depends': ['website', 'base', 'sale'],
    'data': [
        'views/sale_order_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
