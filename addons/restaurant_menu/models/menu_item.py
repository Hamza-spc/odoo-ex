from odoo import fields, models


class RestaurantMenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Restaurant Menu Item'

    name = fields.Char(string='Dish Name', required=True)
    price = fields.Float(string='Price (DH)', digits=(10, 2))
    category = fields.Selection(
        selection=[
            ('starter', 'Starter'),
            ('main', 'Main Course'),
            ('dessert', 'Dessert'),
            ('drink', 'Drink'),
        ],
        string='Category',
        default='main',
    )
