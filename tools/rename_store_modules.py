"""Apply the approved Odoo Store module identities once, preserving model names."""
import ast
import json
from pathlib import Path
import re

from lxml import html
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
IDENTITIES = json.loads((ROOT / 'tools/module_names.json').read_text())
TEXT_SUFFIXES = {'.py', '.xml', '.csv', '.js', '.css', '.scss', '.html', '.md', '.txt', '.rst', '.po', '.pot', '.json', '.yml', '.yaml'}


def replace_technical_names(text):
    for item in IDENTITIES:
        text = text.replace(item['old'], item['technical'])
    return text


def replace_display_names(text, item):
    names = sorted(set(item.get('aliases', []) + [item['display']]), key=len, reverse=True)
    pattern = r'(?<![\w])(?:' + '|'.join(re.escape(n) for n in names) + r')(?![\w])'
    return re.sub(pattern, lambda m: m[0] if m[0] == item['display'] else item['display'], text)


def rename_listing(doc, item):
    for node in doc.iter():
        if not isinstance(node.tag, str):
            continue
        if node.text:
            node.text = replace_display_names(node.text, item)
        if node.tail:
            node.tail = replace_display_names(node.tail, item)
        for attr in ('alt', 'title'):
            if node.get(attr):
                node.set(attr, replace_display_names(node.get(attr), item))
        href = node.get('href', '')
        if href.startswith(('mailto:', 'https://wa.me/')):
            for alias in item.get('aliases', []):
                href = href.replace(quote(alias), quote(item['display']))
            node.set('href', href)
    rename_heading(doc, item['display'])


def rename_heading(doc, display):
    heading = next(iter(doc.xpath('.//h1')), None)
    if heading is None:
        return
    tagline = ' '.join(heading.text_content().split())
    attributes = dict(heading.attrib)
    heading.clear()
    heading.attrib.update(attributes)
    heading.text = display
    # Keep the service desk's existing headline as feature copy.
    if 'Every complaint' in tagline:
        text = html.Element('p', style='font-size:20px;font-weight:700;line-height:1.5;margin:0 0 18px;')
        text.text = tagline
        heading.addnext(text)


def main():
    for item in IDENTITIES:
        old, new = ROOT / item['old'], ROOT / item['technical']
        if old.exists():
            if new.exists():
                raise RuntimeError('Both old and new module directories exist: ' + item['technical'])
            old.rename(new)
        if not new.exists():
            raise RuntimeError('Missing module directory: ' + str(new))
    changed = 0
    for item in IDENTITIES:
        module = ROOT / item['technical']
        for path in module.rglob('*'):
            if not path.is_file() or '__pycache__' in path.parts or path.suffix not in TEXT_SUFFIXES:
                continue
            raw = path.read_bytes()
            try:
                source = raw.decode('utf-8')
            except UnicodeDecodeError:
                continue
            result = replace_technical_names(source)
            if path.name == '__manifest__.py':
                result = re.sub(r"(['\"]name['\"]\s*:\s*)(['\"])(.*?)\2", lambda m: m[1] + repr(item['display']), result, count=1)
                result = replace_display_names(result, item)
            if result != source:
                path.write_bytes(result.encode('utf-8'))
                changed += 1
        description = module / 'static/description/index.html'
        doc = html.fragment_fromstring(description.read_text(), create_parent='div')
        rename_listing(doc, item)
        description.write_text('\n'.join(html.tostring(child, encoding='unicode', method='html') for child in doc).rstrip() + '\n')
        assert ast.literal_eval((module / '__manifest__.py').read_text())['name'] == item['display']
    # Review artifacts must point at the new directories as well.
    for path in (ROOT / 'preview').glob('*.json'):
        path.write_text(replace_technical_names(path.read_text()))
    print('Renamed 8 directories and manifests; updated {} source files.'.format(changed))


if __name__ == '__main__':
    main()
