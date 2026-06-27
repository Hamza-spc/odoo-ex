{
    'name': 'Restaurant Menu',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/menu_tag_data.xml',
        'views/menu_item_views.xml',
        'views/partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
