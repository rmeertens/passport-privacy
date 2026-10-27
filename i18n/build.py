#!/usr/bin/env python3
"""Generate the translated pages (de/, fr/, nl/, es/, pl/) from the English index.html.

index.html is the single source for markup, styles and script. Each i18n/<code>.py
holds one language's head metadata, the translated body (from <h1> to </main>) and
translations of the user-facing strings inside the <script>. Everything else is
copied from the English page, so a fix to the tool only needs to be made once.

    python3 i18n/build.py          # rewrite <code>/index.html for every language
    python3 i18n/build.py --check  # exit 1 if any generated page is out of date

To add a language: create i18n/<code>.py (copy an existing one), add it to LANGS
below, add it to the language switcher, hreflang links and og:locale:alternate tags
in index.html, and add its URL to sitemap.xml.
"""
import importlib
import json
import os
import re
import sys

sys.dont_write_bytecode = True  # keep i18n/ free of __pycache__

BASE = 'https://passport-privacy.meertens.dev/'
# Language code -> og:locale, in the order the pages are generated.
LANGS = {'de': 'de_DE', 'fr': 'fr_FR', 'nl': 'nl_NL', 'es': 'es_ES', 'pl': 'pl_PL'}

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def sub_once(pattern, repl, s, flags=0):
    """Replace exactly one regex match; fail loudly if the English page changed shape."""
    out, n = re.subn(pattern, lambda m: repl, s, count=1, flags=flags)
    if n != 1 or len(re.findall(pattern, s, flags)) != 1:
        sys.exit(f'build.py: expected exactly one match for {pattern!r} in index.html')
    return out


def replace_once(s, old, new, lang):
    if s.count(old) != 1:
        sys.exit(f'build.py [{lang}]: expected exactly one occurrence of {old[:70]!r}')
    return s.replace(old, new)


def attr(text):
    return text.replace('"', '&quot;')


def meta(s, kind, name, value):
    return sub_once(rf'<meta {kind}="{re.escape(name)}" content="[^"]*" />',
                    f'<meta {kind}="{name}" content="{attr(value)}" />', s)


def build(en, code):
    L = importlib.import_module(code)
    url = BASE + code + '/'
    for needle in (f'hreflang="{code}" href="{url}"', f'href="/{code}/" hreflang="{code}"',
                   f'og:locale:alternate" content="{LANGS[code]}"'):
        if needle not in en:
            sys.exit(f'build.py [{code}]: index.html is missing {needle!r}')

    s = en
    s = replace_once(s, '<html lang="en">', f'<html lang="{code}">', code)
    s = sub_once(r'<title>.*?</title>', f'<title>{L.TITLE}</title>', s)
    s = meta(s, 'name', 'description', L.DESC)
    s = replace_once(s, f'<link rel="canonical" href="{BASE}" />', f'<link rel="canonical" href="{url}" />', code)
    s = replace_once(s, f'<meta property="og:url" content="{BASE}" />', f'<meta property="og:url" content="{url}" />', code)
    s = sub_once(r'<meta property="og:title" content="[^"]*" />', f'<meta property="og:title" content="{L.OG_TITLE}" />', s)
    s = meta(s, 'property', 'og:description', L.OG_DESC)
    s = meta(s, 'property', 'og:image:alt', L.OG_ALT)
    s = sub_once(r'<meta name="twitter:title" content="[^"]*" />', f'<meta name="twitter:title" content="{L.OG_TITLE}" />', s)
    s = meta(s, 'name', 'twitter:description', L.TW_DESC)
    s = meta(s, 'name', 'twitter:image:alt', L.TW_ALT)

    # og:locale: this page's locale first, every other language as an alternate.
    locales = {'en': 'en_GB', **LANGS}
    block = '\n'.join([f'  <meta property="og:locale" content="{locales[code]}" />'] +
                      [f'  <meta property="og:locale:alternate" content="{v}" />' for k, v in locales.items() if k != code])
    s = sub_once(r'  <meta property="og:locale" content="[^"]*" />\n(?:  <meta property="og:locale:alternate" content="[^"]*" />\n)*',
                 block + '\n', s)

    # JSON-LD
    s = sub_once(r'^    "name": .*,$', f'    "name": {json.dumps(L.LD_NAME, ensure_ascii=False)},', s, re.M)
    s = sub_once(r'^    "description": .*,$', f'    "description": {json.dumps(L.LD_DESC, ensure_ascii=False)},', s, re.M)
    s = replace_once(s, f'"url": "{BASE}",', f'"url": "{url}",', code)
    s = replace_once(s, '"inLanguage": "en",', f'"inLanguage": "{code}",', code)

    # Language switcher: label it in this language and mark this page as current.
    s = sub_once(r'<nav class="lang-switch" aria-label="[^"]*">', f'<nav class="lang-switch" aria-label="{L.NAV_LABEL}">', s)
    s = replace_once(s, ' lang="en" aria-current="page">', ' lang="en">', code)
    s = replace_once(s, f'href="/{code}/" hreflang="{code}" lang="{code}">',
                     f'href="/{code}/" hreflang="{code}" lang="{code}" aria-current="page">', code)

    # Body content, from <h1> up to </main>.
    start, end = s.index('      <h1>'), s.index('    </main>')
    s = s[:start] + L.BODY + s[end:]

    for old, new in L.JS:
        s = replace_once(s, old, new, code)
    return s


def main():
    check = '--check' in sys.argv[1:]
    sys.path.insert(0, HERE)
    with open(os.path.join(ROOT, 'index.html'), encoding='utf-8') as f:
        en = f.read()
    stale = []
    for code in LANGS:
        out = build(en, code)
        path = os.path.join(ROOT, code, 'index.html')
        if check:
            try:
                with open(path, encoding='utf-8') as f:
                    current = f.read()
            except FileNotFoundError:
                current = None
            if current != out:
                stale.append(f'{code}/index.html')
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(out)
        print(f'wrote {code}/index.html')
    if stale:
        sys.exit('out of date (run python3 i18n/build.py): ' + ', '.join(stale))
    if check:
        print('all translated pages are up to date')


if __name__ == '__main__':
    main()
