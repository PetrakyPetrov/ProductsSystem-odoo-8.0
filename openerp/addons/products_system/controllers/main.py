from openerp import http
from openerp.http import request
import json

class Main(http.Controller):
    @http.route('/products_system/products', type='http', auth='none')
    def products(self):

        records = request.env['products.system'].sudo().search([])
        result = '<html><body><table><tr><td>'
        result += '</td></tr><tr><td>'.join(records.mapped('name'))
        result += '</td></tr></table></body></html>'
        return result

    @http.route('/products_system/products/json', type='http', auth='none')
    def products_json(self):

        records = request.env['products.system']\
                         .sudo().search([])
        return json.dumps(records.read([]))
