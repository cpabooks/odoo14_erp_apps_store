"""Rebuild CPA Books ERP listing styles from the committed original descriptions.

Rebuilds the listing design using the approved module identities in module_names.json.
Run with the project's configured interpreter. Artwork is produced separately.
"""
import ast
import colorsys
import html
import json
from pathlib import Path
import re
import subprocess

from lxml import html as lh
from lxml.etree import SubElement
try:
    from .rename_store_modules import replace_technical_names, replace_display_names, rename_listing
except ImportError:
    from rename_store_modules import replace_technical_names, replace_display_names, rename_listing

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '97b21f151216c6d2840108071400a7b9ada312ac'
IDENTITIES = json.loads((ROOT / 'tools/module_names.json').read_text())
THEMES = {
    'audited_financials': (215, 'Sapphire / Financial reporting', 8),
    'chart_of_accounts': (273, 'Aubergine / Ledger architecture', 16),
    'facility_management': (150, 'Forest / Facility operations', 12),
    'field_service': (206, 'Marine / Service desk', 18),
    'fire_alarm': (350, 'Burgundy / Fire safety', 6),
    're_sequences': (25, 'Copper / Document control', 4),
    'recipe_book': (82, 'Olive / Restaurant operations', 20),
    'switchgear': (195, 'Electric blue / Manufacturing', 3),
}
MAIL = 'mailto:info.cpabooks@gmail.com'
WEBSITE = 'https://cpabookserp.com'
LIVE_DEMO = WEBSITE + '/contactus'


def original(path):
    relative = str(path.relative_to(ROOT))
    for item in IDENTITIES:
        if relative.startswith(item['technical'] + '/'):
            relative = item['old'] + relative[len(item['technical']):]
            break
    return subprocess.check_output(['git', 'show', BASELINE + ':' + relative], cwd=str(ROOT)).decode()


def brand(text):
    text = re.sub(r'https?://(?:www\.)?saaskul\.com[^\s\"\'<>]*', WEBSITE, text, flags=re.I)
    text = re.sub(r'\bsaaskul\.com\b', 'cpabookserp.com', text, flags=re.I)
    text = re.sub(r'\bsaaskul\b', 'CPA Books ERP', text, flags=re.I)
    # Links carry URL-encoded spaces, while display text remains readable.
    text = re.sub(r'(href=[\"\'])(.*?)([\"\'])', lambda m: m[1] + m[2].replace('CPA Books ERP', 'CPA%20Books%20ERP') + m[3], text)
    return text


def recolor(match, hue):
    value = match[0]
    rgb = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    _, light, sat = colorsys.rgb_to_hls(*rgb)
    if sat < .045:  # Preserve white, neutral grays and black.
        return value
    if hue == 82 and .24 < light < .66:
        light = min(light, .30)
        sat = min(sat, .40)
    rgb = colorsys.hls_to_rgb(hue / 360, light, min(sat, .72))
    return '#' + ''.join('{:02X}'.format(round(c * 255)) for c in rgb)


def setstyle(node, **values):
    styles = dict(part.split(':', 1) for part in node.get('style', '').split(';') if ':' in part)
    styles.update({key.replace('_', '-'): value for key, value in values.items()})
    node.set('style', ';'.join(key.strip() + ':' + value.strip() for key, value in styles.items()) + ';')


def readable_colors(node, background='#FFFFFF', foreground='#182B45'):
    styles = dict(part.split(':', 1) for part in node.get('style', '').split(';') if ':' in part)
    styles = {k.strip(): v.strip() for k, v in styles.items()}
    background = styles.get('background-color', background)
    foreground = styles.get('color', foreground)
    def luminance(value):
        channels = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        channels = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
        return sum(c * w for c, w in zip(channels, (.2126, .7152, .0722)))
    if re.fullmatch(r'#[A-Fa-f0-9]{6}', background) and re.fullmatch(r'#[A-Fa-f0-9]{6}', foreground):
        bg, fg = luminance(background), luminance(foreground)
        if (max(bg, fg) + .05) / (min(bg, fg) + .05) < 4.5:
            rgb = [int(foreground[i:i + 2], 16) / 255 for i in (1, 3, 5)]
            h, light, saturation = colorsys.rgb_to_hls(*rgb)
            direction = 1 if bg < .18 else -1
            for _ in range(100):
                light = max(0, min(1, light + direction * .01))
                rgb = colorsys.hls_to_rgb(h, light, saturation)
                foreground = '#' + ''.join('{:02X}'.format(round(c * 255)) for c in rgb)
                fg = luminance(foreground)
                if (max(bg, fg) + .05) / (min(bg, fg) + .05) >= 4.5:
                    break
            setstyle(node, color=foreground)
    for child in node:
        if isinstance(child.tag, str):
            readable_colors(child, background, foreground)


def main():
    pages = []
    for key, (hue, label, radius) in THEMES.items():
        identity = next(i for i in IDENTITIES if i['old'] == key + '_saaskul')
        module = ROOT / identity['technical']
        path = module / 'static/description/index.html'
        source = replace_technical_names(brand(original(path))).replace('banner_screenshot.jpg', 'banner.png')
        source = re.sub(r'#[0-9A-Fa-f]{6}\b', lambda m: recolor(m, hue), source)
        source = re.sub(r'border-radius:(\d+)px', lambda m: 'border-radius:{}px'.format(radius if int(m[1]) >= 14 else min(int(m[1]), radius)), source)
        doc = lh.fragment_fromstring(source, create_parent='div')
        sections = doc.xpath('./section')
        # Add navigable section anchors without changing the feature descriptions.
        for i, section in enumerate(sections):
            if not section.get('id'):
                section.set('id', 'cpa-section-{}'.format(i + 1))
            setstyle(section, margin_bottom='24px')
            headings = section.xpath('.//h2')
            if i and headings:
                heading = headings[0]
                setstyle(heading, border_bottom_width='2px', border_bottom_style='solid', border_bottom_color=recolor(re.match(r'.*', '#DBEAFE'), hue), padding_bottom='14px')
        # Three former centered heroes become editorial split layouts.
        if key in ('chart_of_accounts', 're_sequences', 'recipe_book'):
            hero = sections[0][0]
            banner = hero.xpath('./img[contains(@src,"banner")]')[0]
            hero.remove(banner)
            row = lh.Element('div', {'class': 'row align-items-center'})
            left = lh.Element('div', {'class': 'col-lg-7', 'style': 'padding:18px;text-align:left;'})
            right = lh.Element('div', {'class': 'col-lg-5', 'style': 'padding:18px;'})
            # Keep statistics below the split introduction.
            stats = []
            for child in list(hero):
                if child.get('class') == 'row':
                    stats.append(child)
                    hero.remove(child)
                else:
                    left.append(child)
            setstyle(banner, width='100%', height='auto')
            right.append(banner)
            row.extend([left, right])
            hero.append(row)
            hero.extend(stats)
            setstyle(hero, padding='28px 18px', text_align='left')
        elif key == 'audited_financials':
            setstyle(sections[0][0], border_top='6px solid #245AA0', padding='34px 22px')
        elif key == 'fire_alarm':
            setstyle(sections[0][0], text_align='left', padding='36px 26px', border_top='6px solid #9E2944')
            for node in sections[0].xpath('.//img[@src="icon.png"]'):
                setstyle(node, margin='0 0 18px')
        elif key == 'facility_management':
            setstyle(sections[0][0], padding='36px 26px', border_top='6px solid #77AD8F')
        elif key == 'field_service':
            setstyle(sections[0][0], border='1px solid #B9D7EC', border_top='6px solid #2874A6')
        elif key == 'switchgear':
            setstyle(sections[0][0], border_top='6px solid #38BED9', padding='36px 22px 0')
        # Small screens must be allowed to shrink large headings and images.
        for image in doc.xpath('.//img'):
            setstyle(image, max_width='100%', height='auto')
        for heading in doc.xpath('.//h1'):
            setstyle(heading, font_size='38px', line_height='1.15', overflow_wrap='break-word')
        # Fixed table layout and wrapping keep dense workflow/month tables readable
        # inside the store's narrow mobile columns without hiding any values.
        for table in doc.xpath('.//table'):
            setstyle(table, width='100%', table_layout='fixed', overflow_wrap='break-word')
        nav = lh.Element('section', {'class': 'oe_container', 'style': 'padding:18px 8px;border-bottom:1px solid #E2E8F0;margin-bottom:24px;font-family:Arial,Helvetica,sans-serif;'})
        logo = SubElement(nav, 'strong', style='color:#182B45;font-size:18px;')
        logo.text = 'CPA Books ERP'
        demo = SubElement(nav, 'a', href=LIVE_DEMO, style='display:inline-block;margin:6px 0 6px 20px;color:#40536A;font-size:13px;text-decoration:none;')
        demo.text = 'Live Demo'
        for target, title in [(sections[0], 'Overview'), next(((s, 'Features') for s in sections if s.xpath('.//h2')), (sections[0], 'Features')), (sections[-1], 'Support')]:
            link = SubElement(nav, 'a', href='#' + target.get('id'), style='display:inline-block;margin:6px 0 6px 20px;color:#40536A;font-size:13px;text-decoration:none;')
            link.text = title
        doc.insert(0, nav)
        rename_listing(doc, identity)
        readable_colors(doc)
        result = '\n'.join(lh.tostring(child, encoding='unicode', method='html') for child in doc)
        path.write_text('<!-- CPA Books ERP | {} | Bootstrap grid and inline listing styles -->\n'.format(label) + result.rstrip() + '\n')
        manifest = module / '__manifest__.py'
        meta = original(manifest).replace('banner_screenshot.jpg', 'banner.png')
        meta = re.sub(r"(['\"]author['\"]\s*:\s*)['\"]Saaskul['\"]", r"\1'CPA Books ERP'", meta)
        meta = re.sub(r"(['\"]website['\"]\s*:\s*)['\"]https://saaskul.com['\"]", lambda m: m[1] + repr(WEBSITE), meta)
        meta = re.sub(r"(['\"]live_test_url['\"]\s*:\s*)['\"][^'\"]*['\"]", lambda m: m[1] + repr(LIVE_DEMO), meta)
        meta = replace_display_names(replace_technical_names(meta), identity)
        meta = re.sub(r"(['\"]name['\"]\s*:\s*)(['\"])(.*?)\2", lambda m: m[1] + repr(identity['display']), meta, count=1)
        assert ast.literal_eval(meta)['name'] == identity['display']
        manifest.write_text(meta)
        name = ast.literal_eval(meta)['name']
        pages.append({'name': name, 'theme': label, 'path': str(path.relative_to(ROOT)), 'html': result.replace('src="', 'src="../' + identity['technical'] + '/static/description/')})
    preview = ROOT / 'preview'
    preview.mkdir(exist_ok=True)
    css = '*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif}.oe_container{max-width:1140px;margin:auto;padding:0 12px}.row{display:flex;flex-wrap:wrap;margin:0 -12px}.row>[class*=col-]{padding:0 12px}[class*=col-]{width:100%}.align-items-center{align-items:center}.h-100{height:100%}.col-2{width:16.666%}.col-4{width:33.333%}.col-6{width:50%}@media(min-width:768px){.col-md-2{width:16.666%}.col-md-3{width:25%}.col-md-4{width:33.333%}.col-md-5{width:41.666%}.col-md-6{width:50%}.col-md-7{width:58.333%}.col-md-8{width:66.666%}}@media(min-width:992px){.col-lg-3{width:25%}.col-lg-4{width:33.333%}.col-lg-5{width:41.666%}.col-lg-6{width:50%}.col-lg-7{width:58.333%}.col-lg-8{width:66.666%}}img{max-width:100%;height:auto}a{color:inherit}'
    payload = json.dumps(pages).replace('</', '<\\/')
    shell = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CPA Books ERP · App collection</title><style>body{margin:0;background:#edf1f6;font-family:Arial,sans-serif;color:#182b45}header{padding:18px 24px;background:white;border-bottom:1px solid #d8e0eb}h1{font-size:22px;margin:0 0 12px}select,button,a{padding:10px;margin:4px;border:1px solid #ccd7e4;border-radius:6px;background:white;color:#182b45}#note{font-size:13px;color:#52677e;margin:12px 4px}iframe{display:block;width:100%;height:calc(100vh - 170px);border:0;background:white;margin:auto}iframe.mobile{width:390px;max-width:100%}</style><header><h1>CPA Books ERP / Odoo 14 Apps</h1><select id="app" aria-label="Select an app"></select><button id="desktop">Desktop</button><button id="mobile">Mobile</button><a id="source">Listing HTML</a><div id="note"></div></header><iframe id="page" title="App listing preview"></iframe><script>const pages=PAYLOAD;const css=CSS;const app=document.getElementById('app'),frame=document.getElementById('page');pages.forEach((p,i)=>app.add(new Option(p.name,i)));function show(){const p=pages[app.value];frame.srcdoc='<html><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style><body>'+p.html+'</body></html>';document.getElementById('source').href='../'+p.path;document.getElementById('note').textContent=p.theme+' · Local preview; final store rendering may differ.'}app.onchange=show;document.getElementById('mobile').onclick=()=>frame.className='mobile';document.getElementById('desktop').onclick=()=>frame.className='';show();</script></html>'''
    (preview / 'index.html').write_text(shell.replace('PAYLOAD', payload).replace('CSS', json.dumps(css)))
    print('Updated 8 listing pages and manifests; preview/index.html created.')


if __name__ == '__main__':
    main()
