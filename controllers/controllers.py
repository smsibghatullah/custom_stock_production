# -*- coding: utf-8 -*-
from odoo import http

# class CustomStockProduction(http.Controller):
#     @http.route('/custom_stock_production/custom_stock_production/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_stock_production/custom_stock_production/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_stock_production.listing', {
#             'root': '/custom_stock_production/custom_stock_production',
#             'objects': http.request.env['custom_stock_production.custom_stock_production'].search([]),
#         })

#     @http.route('/custom_stock_production/custom_stock_production/objects/<model("custom_stock_production.custom_stock_production"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_stock_production.object', {
#             'object': obj
#         })