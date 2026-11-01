# -*- coding: utf-8 -*-
# from odoo import http


# class SaaskulSequences(http.Controller):
#     @http.route('/smart_sequence_engine/smart_sequence_engine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_sequence_engine/smart_sequence_engine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_sequence_engine.listing', {
#             'root': '/smart_sequence_engine/smart_sequence_engine',
#             'objects': http.request.env['smart_sequence_engine.smart_sequence_engine'].search([]),
#         })

#     @http.route('/smart_sequence_engine/smart_sequence_engine/objects/<model("smart_sequence_engine.smart_sequence_engine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_sequence_engine.object', {
#             'object': obj
#         })
