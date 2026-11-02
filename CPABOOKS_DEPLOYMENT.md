# CPA Books ERP website catalog deployment

Deployed on 2026-11-01 to https://cpabookserp.com/apps on Server 8 (`169.58.222.92`).

The subsequent approved module/display-name rename is documented in [MODULE_RENAMES.md](MODULE_RENAMES.md). Website catalog and product IDs, as well as public URLs, are retained. The new backup for that change is `/opt/cpabooks/odoo14/backups/cpa-rename-20261101T165528Z/`.

- Odoo container: `saas_contabo-odoo`; database: `saas_contabo`; PostgreSQL container: `saas_contabo-db`.
- Removed the nine previous website catalog records (seven published and two unpublished duplicates). Created eight published CPA Books ERP listings, including IFRS Chart of Accounts.
- Reused the seven corresponding shop products to retain sales/order references. The two obsolete duplicate products are unpublished and archived. The new chart of accounts listing has its own shop product.
- Deployed listing artwork under `cpabooks_saas_website/static/cpa_books_erp_apps/`. Full descriptions, icons, banners, manifests, license information and existing email/WhatsApp contacts are present.
- New listing URLs use `/apps/cpa-books-erp-*`. Homepage and catalog links resolve to the new records.
- Fixed the website's hardcoded publisher badge to use the app author, in both its source template and database view. Set website version labels to `Odoo 14` so the existing version parser displays only `14.0`.
- Refreshed Odoo worker template caches through the existing cache signaling sequence; no container restart was needed.

## Backup and recovery materials

Server-side directory: `/opt/cpabooks/odoo14/backups/cpa-apps-20261101T150210Z/`.

Contains a verified PostgreSQL custom-format dump, the pre-deployment filestore archive, the website module archive, the original app-store branding template, import/finalization scripts and the listing payload. Restore database and filestore together if a full rollback is required; the original branding template is also preserved separately.

## Verification

- Public homepage, catalog and all eight detail pages returned HTTP 200.
- All eight entries appear in the catalog and homepage, with CPA Books ERP authorship, version 14.0 and the requested Live Demo URL.
- All 78 referenced listing image URLs returned images successfully.
- No old `/apps/saaskul-*` links remain on the homepage or catalog.
- Browser checks covered financial reports, chart of accounts and recipe costing at 1440px and 390px widths, with no horizontal overflow or broken images.
- Odoo remained running; no ERROR/CRITICAL/Traceback lines appeared in the inspected post-deployment container logs.

SSH authentication is stored in the gitignored local credential file referenced by `cpabooks-custom/.cursor/rules/live-docker-server8-contabo.mdc`, with permissions 0600. No password is stored in this report or the tracked rule file.
