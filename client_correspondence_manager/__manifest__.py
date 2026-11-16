# -*- coding: utf-8 -*-
{
    "name": "Client Correspondence Manager",
    "summary": "Prepare, print, email and log client correspondence from CRM, quotations, estimations, invoices and projects.",
    "description": """
Client Correspondence Manager
=============================
Prepare client correspondence from the record it belongs to: CRM opportunity,
quotation, estimation, customer invoice or project. Client details,
reference numbers, amounts and scope are taken from the source document.
Each letter can be printed with signature and stamp, emailed from the source
record, shared as WhatsApp text, and kept in a numbered correspondence register.
Includes 11 editable letter templates.
    """,
    "version": "14.0.1.0.1",
    "category": "Sales/CRM",
    "author": "CPA Books ERP",
    "website": "https://cpabookserp.com",
    "live_test_url": "https://cpabookserp.com/contactus",
    "support": "info.cpabooks@gmail.com",
    "license": "OPL-1",
    "price": 0.0,
    "currency": "USD",
    "images": [
        "static/description/banner.png",
    ],
    "depends": [
        "crm",
        "sale_management",
        "account",
        "project",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/client_letter_sequence.xml",
        "data/client_letter_template_data.xml",
        "views/client_letter_document_views.xml",
        "views/client_letter_template_views.xml",
        "wizard/client_letter_wizard_views.xml",
        "views/action_buttons_views.xml",
        "report/client_letter_report.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
