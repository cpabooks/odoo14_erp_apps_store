# -*- coding: utf-8 -*-
# from odoo import http


# class CpabooksChartOfAccountV1(http.Controller):
#     @http.route('/smart_coa_builder/smart_coa_builder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_coa_builder/smart_coa_builder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_coa_builder.listing', {
#             'root': '/smart_coa_builder/smart_coa_builder',
#             'objects': http.request.env['smart_coa_builder.smart_coa_builder'].search([]),
#         })

#     @http.route('/smart_coa_builder/smart_coa_builder/objects/<model("smart_coa_builder.smart_coa_builder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_coa_builder.object', {
#             'object': obj
#         })
