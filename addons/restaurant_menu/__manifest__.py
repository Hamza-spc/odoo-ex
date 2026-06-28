{
    'name': 'Restaurant Menu',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'data/menu_tag_data.xml',
        'data/cron.xml',
        'views/menu_item_views.xml',
        'views/partner_views.xml',
        'views/sale_order_views.xml',
        'views/product_wizard_views.xml',
        'report/menu_report.xml',
    ],
    'installable': True,
    'application': True,
}
