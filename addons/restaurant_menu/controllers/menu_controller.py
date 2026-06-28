import json

from odoo import http
from odoo.http import request


class RestaurantMenuController(http.Controller):

    @http.route('/restaurant/menu', auth='public', methods=['GET'], csrf=False)
    def menu_list(self):
        dishes = request.env['restaurant.menu.item'].sudo().search([])
        data = []
        for dish in dishes:
            data.append({
                'name': dish.name,
                'category': dish.category,
                'price': dish.price,
            })
        body = json.dumps(data)
        return request.make_response(
            body,
            headers=[('Content-Type', 'application/json')],
        )
