# -*- coding: utf-8 -*-
{
    'name': 'Side Menu Navigator',
    'summary': 'Vertical side menu for Odoo 14 Community: all apps, menu search and expandable sub-menus in one panel.',
    'description': """
Side Menu Navigator
===================
Replaces the top app switcher of Odoo 14 Community with a vertical side
menu. Every installed app is listed with its sub-menus, a search box filters
apps and menu items, and a Default menu toggle brings back the standard top
bar. Depends only on the web module.
    """,
    'author': 'CPA Books ERP',
    'website': 'https://cpabookserp.com',
    'live_test_url': 'https://cpabookserp.com/contactus',
    'support': 'info.cpabooks@gmail.com',
    'category': 'Productivity',
    'version': '14.0.1.0.0',
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'USD',
    'images': [
        'static/description/banner.png',
    ],
    'depends': ['web'],
    'data': [
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/sidebar.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
