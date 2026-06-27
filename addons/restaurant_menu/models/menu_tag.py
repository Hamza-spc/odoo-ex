from odoo import fields, models


class RestaurantMenuTag(models.Model):
    _name = 'restaurant.menu.tag'
    _description = 'Menu Item Tag'

    name = fields.Char(string='Tag Name', required=True)
