{
    'name': 'Restaurant Menu',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage restaurant menu items',
    'description': """
        Learning module: store menu items with name, category, and price.
    """,
    'author': 'Hamza',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_item_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
