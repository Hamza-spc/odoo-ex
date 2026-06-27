from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    menu_item_ids = fields.One2many(
        comodel_name='restaurant.menu.item',
        inverse_name='supplier_id',
        string='Menu Items',
    )
