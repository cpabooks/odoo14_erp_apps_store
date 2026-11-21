# -*- coding: utf-8 -*-
{
    'name': 'DB Manager Guard - Secure Login, Hide Database Selector',
    'summary': 'Protect your Odoo databases: removes Manage Databases and Select Database from the login page and returns 404 for the database manager, backup, restore, duplicate and drop URLs. One odoo.conf line to unlock.',
    'description': """
DB Manager Guard
================
Security for the Odoo login page and database manager.

* Removes the "Manage Databases" link from the login page
* Removes the "Select" database button from the login form
* Returns 404 for /web/database/manager, /web/database/selector and the
  create, duplicate, drop, backup, restore and change password URLs
* Unlock when you need the manager: add ``db_manager_unlock = True`` to the
  Odoo server configuration file and restart Odoo
* Depends only on the web module

Keywords: hide database manager, disable database manager, hide manage
databases, hide database selector, block database backup, secure login page,
database security, lock database manager.
""",
    'version': '14.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'CPA Books ERP',
    'website': 'https://cpabookserp.com',
    'live_test_url': 'https://cpabookserp.com/contactus',
    'support': 'info.cpabooks@gmail.com',
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'USD',
    'images': [
        'static/description/banner.png',
    ],
    'depends': [
        'web',
    ],
    'data': [
        'views/login_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
