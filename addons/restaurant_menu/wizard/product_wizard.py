from odoo import models


class RestaurantMenuProductWizard(models.TransientModel):
    _name = 'restaurant.menu.product.wizard'
    _description = 'Bulk Create Sales Products for Dishes'

    def action_create_products(self):
        dishes = self.env['restaurant.menu.item'].search([
            ('product_id', '=', False),
        ])
        for dish in dishes:
            product = self.env['product.product'].create({
                'name': dish.name,
                'list_price': dish.price,
            })
            dish.product_id = product
        return {'type': 'ir.actions.act_window_close'}
