# -*- coding: utf-8 -*-
{
 'name': 'Recipe Library Management',
 'summary': 'Restaurant recipe, theoretical food cost, consumption and closing stock control',
 'version': '14.0.1.0.3',
 'category': 'Operations/Restaurant',
 'author': 'CPA Books ERP', 'website': 'https://cpabookserp.com', 'support': 'info.cpabooks@gmail.com',
 'live_test_url': 'https://cpabookserp.com/contactus',
 'license': 'OPL-1', 'price': 0.00, 'currency': 'USD',
 'depends': ['base','product','sale_management','stock','purchase'],
 'data': [
   'security/recipe_security.xml','security/ir.model.access.csv',
   'views/recipe_views.xml','views/consumption_views.xml','views/dashboard_views.xml','views/menu.xml',
   'wizard/closing_stock_wizard_views.xml'
 ],
 'images': ['static/description/banner.png'],
 'application': True, 'installable': True,
}
