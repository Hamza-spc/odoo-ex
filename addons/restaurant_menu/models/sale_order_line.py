from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    menu_item_id = fields.Many2one(
        comodel_name='restaurant.menu.item',
        string='Menu Dish',
        compute='_compute_menu_item_id',
    )
    menu_category = fields.Selection(
        related='menu_item_id.category',
        string='Dish Category',
        readonly=True,
    )

    @api.depends('product_id')
    def _compute_menu_item_id(self):
        for line in self:
            if line.product_id:
                line.menu_item_id = self.env['restaurant.menu.item'].search(
                    [('product_id', '=', line.product_id.id)],
                    limit=1,
                )
            else:
                line.menu_item_id = False
