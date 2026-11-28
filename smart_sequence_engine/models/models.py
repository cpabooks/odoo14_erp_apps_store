# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class smart_sequence_engine(models.Model):
#     _name = 'smart_sequence_engine.smart_sequence_engine'
#     _description = 'smart_sequence_engine.smart_sequence_engine'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
