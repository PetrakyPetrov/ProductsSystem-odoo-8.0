from openerp import http
from openerp.http import request
import json

class Main(http.Controller):

    @http.route('/products_system/all_products', type='http', auth='none', website=True)
    def products_json(self):

        records = request.env['products.system']\
                         .sudo().search([])
        return json.dumps(records.read([]))
