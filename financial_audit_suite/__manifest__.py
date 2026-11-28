# -*- coding: utf-8 -*-
{
    'name': 'Financial Audit & Reporting',
    'summary': 'IFRS-style financial statements, trial balance mapping and corporate tax filing',
    'description': """
Cpabooks Audited Financials
===========================
Self-contained financial statement pack for Odoo 19 Community:

* Statement of Profit or Loss
* Statement of Financial Position
* Changes in Equity, Cash Flow, PPE schedule and notes
* Chart of accounts mapping and corporate tax filing categories
* PDF, Excel and CSV export
* Country-aware print follows the company currency: NGN prints FGN / Nigerian Naira,
  AED keeps U.A.E. / Arab Emirates Dirhams, a currency used by one country prints
  that country. A shared or missing currency defaults to FGN / Nigeria.
  The company address is not used.
  Non-AED companies get L1 and L4 export only.
* Optional "Load ISO Chart of Accounts" wizard (ISOSYSTEMS, Nigeria): account groups,
  ledgers and AFG mapping.

Depends only on Accounting (account). No other custom module is required.
    """,
    'version': '19.0.1.0.267',
    'category': 'Accounting',
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
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/audited_financial_security.xml',
        'data/multico_client_actions.xml',
        'views/audited_financials_views.xml',
        'views/account_account_views.xml',
        'views/audited_financial_ledger_merge_views.xml',
        'views/audited_financial_l1_print_wizard_views.xml',
        'views/audited_financial_print_setup_wizard_views.xml',
        'views/afg_journal_items_views.xml',
        'views/audited_financial_iso_coa_wizard_views.xml',
        'views/res_company_views.xml',
        'report/afg_audit_report.xml',
        'data/menu_cleanup_legacy_statements.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'financial_audit_suite/static/lib/jquery.js',
            'financial_audit_suite/static/src/css/audited_financials_dashboard.css',
            'financial_audit_suite/static/src/css/audited_financial_app_shell.css',
            'financial_audit_suite/static/src/css/afg_map_list.css',
            'financial_audit_suite/static/src/xml/audited_financials_dashboard.xml',
            'financial_audit_suite/static/src/js/audited_financials_dashboard.js',
            'financial_audit_suite/static/src/js/afg_map_list.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
}
