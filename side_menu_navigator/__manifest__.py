# -*- coding: utf-8 -*-
{
    'name': 'Side Menu Navigator',
    'summary': 'Permanent left sidebar with every installed app, searchable menus and nested sub-menus for Odoo 19 Community. No web_enterprise needed.',
    'description': """
App Sidebar Navigation
======================
A fixed left sidebar for Odoo 19 Community that lists every installed app.
Search apps and menu items, open sub-menus in place, and switch back to the
standard top menu with one click. Depends only on the web module and does
not use or copy web_enterprise.
    """,
    'author': 'CPA Books ERP',
    'website': 'https://cpabookserp.com',
    'live_test_url': 'https://cpabookserp.com/contactus?name=Live%20Preview%20-%20App%20Sidebar%20Navigation',
    'support': 'info.cpabooks@gmail.com',
    'category': 'Productivity',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'USD',
    'images': [
        'static/description/banner.png',
    ],
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'side_menu_navigator/static/src/scss/sidebar.scss',
            'side_menu_navigator/static/src/xml/sidebar.xml',
            'side_menu_navigator/static/src/js/sidebar.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
