# -*- coding: utf-8 -*-
from openerp import models, fields

class ProductsSystem(models.Model):
    _name = 'products.system'
    name = fields.Char('Title', required=True)
    description = fields.Char('Description', required=False)
    quantity = fields.Integer(string='Quantity')
