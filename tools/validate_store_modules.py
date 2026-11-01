"""Static checks for the approved Odoo module namespace rename."""
import ast
import json
from pathlib import Path
import re
import tarfile

from lxml import etree, html

ROOT = Path(__file__).resolve().parents[1]
IDENTITIES = json.loads((ROOT / 'tools/module_names.json').read_text())
NAMES = {item['technical'] for item in IDENTITIES}
OLD_NAMES = {item['old'] for item in IDENTITIES}


def main():
    failures, existing = [], []
    python_files = xml_files = checked_assets = 0
    snapshot = Path('/tmp/cpa-before-module-rename.tar')
    archive = tarfile.open(str(snapshot)) if snapshot.exists() else None

    def before(item, relative):
        if not archive:
            return None
        name = 'odoo14_erp_apps_store/' + item['old'] + '/' + str(relative)
        try:
            return archive.extractfile(name).read()
        except KeyError:
            return None

    for item in IDENTITIES:
        module = ROOT / item['technical']
        assert module.is_dir(), module
        assert not (ROOT / item['old']).exists(), item['old']
        meta = ast.literal_eval((module / '__manifest__.py').read_text())
        assert meta['name'] == item['display']
        assert meta['author'] == 'CPA Books ERP'
        assert meta['website'] == 'https://cpabookserp.com'
        assert meta['live_test_url'] == 'https://cpabookserp.com/contactus'
        assert meta['support'] == 'info.cpabooks@gmail.com'
        assert not OLD_NAMES.intersection(meta.get('depends', []))
        old_manifest = before(item, Path('__manifest__.py'))
        if old_manifest:
            original_meta = ast.literal_eval(old_manifest.decode())
            mapping = {i['old']: i['technical'] for i in IDENTITIES}
            assert meta['depends'] == [mapping.get(d, d) for d in original_meta['depends']]
            assert meta['license'] == original_meta['license']
            assert meta['version'] == original_meta['version']
        for field in ('data', 'demo', 'qweb', 'images'):
            for value in meta.get(field, []):
                if not (module / value).is_file():
                    issue = '{}: missing {} file {}'.format(item['technical'], field, value)
                    if archive:
                        try:
                            archive.getmember('odoo14_erp_apps_store/' + item['old'] + '/' + value)
                            failures.append(issue)
                        except KeyError:
                            existing.append(issue)
                    else:
                        failures.append(issue)
        doc = html.fragment_fromstring((module / 'static/description/index.html').read_text(), create_parent='div')
        assert doc.xpath('.//h1')[0].text_content() == item['display']
        for src in doc.xpath('.//img/@src'):
            assert (module / 'static/description' / src).is_file(), src
            checked_assets += 1
        ids = set(doc.xpath('.//*[@id]/@id'))
        for link in doc.xpath('.//a[starts-with(@href,"#")]/@href'):
            assert link[1:] in ids, (module, link)
        for path in module.rglob('*'):
            if not path.is_file() or '__pycache__' in path.parts:
                continue
            relative = path.relative_to(module)
            if path.suffix in ('.py', '.xml', '.js', '.css', '.scss', '.csv', '.html', '.json'):
                text = path.read_text()
                for old in OLD_NAMES:
                    if old in text:
                        failures.append('{} still contains {}'.format(path.relative_to(ROOT), old))
            if path.suffix not in ('.py', '.xml'):
                continue
            raw = path.read_bytes()
            try:
                if path.suffix == '.py':
                    current_ast = ast.parse(raw, filename=str(path))
                    python_files += 1
                    prior = before(item, relative)
                    if prior is not None and path.name != '__manifest__.py':
                        expected = prior.decode()
                        for identity in IDENTITIES:
                            expected = expected.replace(identity['old'], identity['technical'])
                        assert ast.dump(ast.parse(expected)) == ast.dump(current_ast), 'Unexpected Python logic change: ' + str(path)
                else:
                    etree.fromstring(raw)
                    xml_files += 1
            except (SyntaxError, etree.XMLSyntaxError) as error:
                prior = before(item, relative)
                same = False
                if prior is not None:
                    try:
                        ast.parse(prior) if path.suffix == '.py' else etree.fromstring(prior)
                    except (SyntaxError, etree.XMLSyntaxError):
                        same = True
                (existing if same else failures).append('{}: {}'.format(path.relative_to(ROOT), error))
        print('PASS: {} -> {}'.format(item['technical'], item['display']))
    if archive:
        archive.close()
    report = {'modules': len(IDENTITIES), 'python_files': python_files, 'xml_files': xml_files, 'listing_images': checked_assets, 'preexisting_findings': existing, 'failures': failures}
    (ROOT / 'preview/rename-validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
