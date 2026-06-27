from odoo import fields, models


class RestaurantMenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Restaurant Menu Item'

    name = fields.Char(string='Dish Name', required=True)
