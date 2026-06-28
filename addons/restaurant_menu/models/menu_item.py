from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class RestaurantMenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Restaurant Menu Item'

    name = fields.Char(string='Dish Name', required=True)
    price = fields.Float(string='Price (DH)', digits=(10, 2))
    cost = fields.Float(string='Cost (DH)', digits=(10, 2))
    margin = fields.Float(
        string='Margin (DH)',
        compute='_compute_margin',
        store=True,
    )
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

    @api.onchange('category')
    def _onchange_category(self):
        default_prices = {
            'starter': 25.0,
            'main': 85.0,
            'dessert': 35.0,
            'drink': 15.0,
        }
        if self.category:
            self.price = default_prices.get(self.category, 0.0)

    @api.depends('price', 'cost')
    def _compute_margin(self):
        for dish in self:
            dish.margin = dish.price - dish.cost

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

    @api.constrains('price')
    def _check_price_positive(self):
        for dish in self:
            if dish.price <= 0:
                raise ValidationError('Price must be greater than 0.')

    @api.model
    def cron_check_missing_products(self):
        dishes = self.search([('product_id', '=', False)])
        if dishes:
            names = ', '.join(dishes.mapped('name'))
            _logger.warning(
                'Restaurant Menu: dishes without Sales product: %s', names
            )

    @api.model
    def action_check_missing_products(self):
        dishes = self.search([('product_id', '=', False)])
        if dishes:
            names = ', '.join(dishes.mapped('name'))
            raise UserError(
                'Dishes missing Sales product: %s' % names
            )
        raise UserError('All dishes have a Sales product.')
