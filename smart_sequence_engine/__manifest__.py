## -*- coding: utf-8 -*-
{
    'name': 'Advanced Sequence Manager',

    'summary': 'Manage and re-sequence document numbers across Odoo applications',

    'description': """
Advanced Sequence Manager
======================
Manage and re-sequence document numbers across Accounting, Sales,
Purchase, Inventory, Project and CRM in Odoo 14.
    """,

    'author': 'CPA Books ERP',
    'website': 'https://cpabookserp.com',
    'live_test_url': 'https://cpabookserp.com/contactus',
    'support': 'info.cpabooks@gmail.com',

    'category': 'Productivity',
    'version': '14.0.1.63',
    'license': 'OPL-1',

    'images': [
        'static/description/banner.png',
    ],

    'depends': [
        'base',
        'account',
        'sale',
        'purchase',
        'stock',
        'project',
        'crm',
    ],

    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/sequence_menu.xml',
        'views/account_move.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/stock_picking.xml',
        'views/set_company_prefix_vew.xml',
        'views/assets.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/create_sequences.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}

