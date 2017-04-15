# -*- coding: utf-8 -*-
{
    'name': "products_system",
    'author': "Petraky Petrov",
    'website': "none",
    'icon': "/products_system/static/desciption/icon.png",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Products',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/products_system.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}