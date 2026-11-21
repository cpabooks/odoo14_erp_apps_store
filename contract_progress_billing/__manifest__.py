# -*- coding: utf-8 -*-
{
    'name': 'Contract Progress Billing - Construction & Labour Supply Invoice',
    'summary': 'Progress invoicing for contractors: Work Done % per line, Previous %, contract value, guarantee flag and a Construction Invoice print, plus a Labour Supply / Construction switch on customer invoices.',
    'description': """
Contract Progress Billing
=========================
Progress billing for construction, contracting, fit-out, MEP and labour supply
companies on Odoo 14 Community and Enterprise.

* Labour Supply Invoice / Construction Invoice switch on customer invoices
* Work Done % per invoice line: the line amount, taxes and journal entry are
  calculated on the work done, using Odoo's standard invoice logic
* Previous % (already billed), Contract Amount and Guarantee (Gtee) per line
* Contract Value total on the invoice
* Construction Invoice PDF with Contract Amount, Previous %, Work Done %, tax and totals
* Filters for Construction and Labour Supply invoices
* Depends only on Accounting (account)

Keywords: construction invoice, progress billing, progressive invoice, interim
invoice, percentage of completion, work done percentage, contracting invoice,
contractor billing, labour supply invoice, subcontractor invoice.
""",
    'version': '14.0.1.0.0',
    'category': 'Accounting/Accounting',
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
        'views/account_move_views.xml',
        'report/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
