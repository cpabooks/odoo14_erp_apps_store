# Approved Odoo Store module identities

| Previous module | New technical name / folder | Display name |
| --- | --- | --- |
| chart_of_accounts_saaskul | smart_coa_builder | Smart Chart of Accounts Manager |
| recipe_book_saaskul | recipe_library_pro | Recipe Library Management |
| switchgear_saaskul | switchgear_manager_pro | Switchgear Management System |
| re_sequences_saaskul | smart_sequence_engine | Advanced Sequence Manager |
| audited_financials_saaskul | financial_audit_suite | Financial Audit & Reporting |
| fire_alarm_saaskul | fire_alarm_manager | Fire Alarm Management System |
| facility_management_saaskul | facility_ops_manager | Facility Operations Management |
| field_service_saaskul | field_service_hub | Field Service Management |

The eight add-on directories and manifest names use these identities. XML IDs, Python imports/references, JavaScript module names, QWeb/report namespaces, security references, icon paths, asset paths, internal dependencies and primary menu labels have been updated. Publisher, support contacts, license and versions are retained. The facility and fire safety add-ons now depend on `smart_sequence_engine`.

Listing headings, descriptions, local preview, banners and the financial audit icon use the new display names. Bitmap text edits use built-in image_gen; prompts and final asset paths are recorded in `preview/rename-artwork-prompts.json`.

## Existing installations

The changes are prepared as newly named add-ons for distribution. Business model identifiers and database table names remain stable. An existing database with the previous add-ons installed requires a planned module/XML-ID ownership migration before switching its installed add-ons to the new technical names; simply renaming the folders is not an in-place database migration. No business-module database migration was run as part of this task.

The live cpabookserp.com website catalog is updated separately, using its existing app and shop-product IDs. Existing public app URLs are retained. Functional add-ons are not installed into the marketing website database by this catalog update.

## Checks and recovery

`tools/validate_store_modules.py` checks the eight identities, manifest paths, dependencies, Python/XML syntax, HTML image paths and anchors, absence of former technical references, and Python AST equivalence after namespace substitution. JavaScript files were syntax-checked with Node.

Local pre-rename snapshot: `/tmp/cpa-before-module-rename.tar`.

Server 8 pre-rename backup: `/opt/cpabooks/odoo14/backups/cpa-rename-20261101T165528Z/` (verified database dump, filestore and store assets).

See `preview/rename-validation.json` and `preview/rename-live-verification.json` for check results. Fresh functional module installation and apps.odoo.com ingestion were not exercised.
