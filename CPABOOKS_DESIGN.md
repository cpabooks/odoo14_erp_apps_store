# CPA Books ERP — Odoo 14 listing design

Open [preview/index.html](preview/index.html) in a browser. Choose an app, then Desktop or Mobile. This local review page is separate from the app descriptions; it supplies a small Bootstrap-like grid for offline viewing.

The approved technical and display names are listed in [MODULE_RENAMES.md](MODULE_RENAMES.md). Functional descriptions, versions and licenses are retained; references and internal dependencies use the new namespaces. Publisher metadata and marketing branding use **CPA Books ERP**. The existing support email and WhatsApp number are retained. Each manifest uses `https://cpabookserp.com` as its website and `https://cpabookserp.com/contactus` as its live demo URL. All listing navigation bars include a Live Demo link to that contact page.

| App | Theme | Listing treatment |
| --- | --- | --- |
| Financial Audit & Reporting | Sapphire / navy | Editorial statement cards and ruled financial tables |
| Smart Chart of Accounts Manager | Aubergine / lavender | Split introduction, hierarchy and feature cards |
| Facility Operations Management | Forest / sage | Operations panels, module cards and calendar sections |
| Field Service Management | Marine / sky blue | Service ticket introduction and workflow sections |
| Fire Alarm Management System | Burgundy / coral | Left-aligned introduction, process tables and handover cards |
| Advanced Sequence Manager | Copper / charcoal | Split introduction and document control sections |
| Recipe Library Management | Olive / cream | Split introduction and recipe/variance sections |
| Switchgear Management System | Electric cyan / midnight blue | Industrial cycle, production cards and engineering tables |

## Artwork

Eight banners and 45 feature images were generated/edited with the built-in image_gen tool and saved in each module's `static/description/` directory. Every module now uses `static/description/banner.png` in its manifest. The financial report's original JPG remains available as an unused original.

The [artwork prompt set](preview/artwork-prompts.json) records the destination paths, prompts and original banner correction prompts. The subsequent [rename prompt set](preview/rename-artwork-prompts.json) records the new title artwork. Existing feature illustrations and the original menu sample photo were retained. Primary app menu labels and code namespaces now follow the approved identities.

## Validation

- Parsed all eight manifests; app names and dependencies match the original.
- Compared original and revised HTML text; original descriptive text is retained after branding/contact substitutions.
- Checked all local image paths and internal section links; image files decode successfully.
- Checked eight pages in Chrome at desktop and 390px preview widths (16 layouts): no missing images or horizontal overflow.
- Checked the Git diff for whitespace errors.

Initial design validation covered the local listings and preview. The listings were subsequently deployed to cpabookserp.com; see [CPABOOKS_DEPLOYMENT.md](CPABOOKS_DEPLOYMENT.md) for live verification and backup details. Rendering on apps.odoo.com and installation of the functional modules were not exercised.

`tools/rebrand_store.py` rebuilds listing HTML, metadata and the local preview from the pinned original Git revision. Artwork is maintained separately. The script requires the project's configured Python environment with lxml.
