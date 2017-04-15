from openerp import http
from openerp.http import request
import json

class Main(http.Controller):

    @http.route('/products_system/products/json', type='http', auth='none')
    def products_json(self):

        records = request.env['products.system']\
                         .sudo().search([])
        return json.dumps(records.read([]))
