from odoo import fields, models
from odoo.exceptions import UserError


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
    supplier_id = fields.Many2one(
        comodel_name='res.partner',
        string='Supplier',
    )
    tag_ids = fields.Many2many(
        comodel_name='restaurant.menu.tag',
        string='Tags',
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Sales Product',
    )

    def action_create_product(self):
        self.ensure_one()
        if self.product_id:
            raise UserError('This dish already has a linked Sales product.')
        product = self.env['product.product'].create({
            'name': self.name,
            'list_price': self.price,
        })
        self.product_id = product

    def write(self, vals):
        res = super().write(vals)
        sync_fields = {'name', 'price'} & set(vals.keys())
        if sync_fields:
            for dish in self.filtered('product_id'):
                dish.product_id.write({
                    'name': dish.name,
                    'list_price': dish.price,
                })
        return res
