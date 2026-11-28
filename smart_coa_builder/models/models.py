# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class smart_coa_builder(models.Model):
#     _name = 'smart_coa_builder.smart_coa_builder'
#     _description = 'smart_coa_builder.smart_coa_builder'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
