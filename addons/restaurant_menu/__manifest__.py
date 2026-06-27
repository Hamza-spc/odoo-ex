{
    'name': 'Restaurant Menu',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/menu_tag_data.xml',
        'views/menu_item_views.xml',
        'views/partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
