# passport-privacy

A tiny, single-page browser tool for safely sharing a copy of your passport or ID card.

Live at **[passport-privacy.meertens.dev](https://passport-privacy.meertens.dev/)** in English, German (`/de/`), French (`/fr/`), Dutch (`/nl/`), Spanish (`/es/`), and Polish (`/pl/`).

## What it does

1. You upload or photograph a scan of your ID.
2. You drag black rectangles over fields you don't want to share — BSN, MRZ, document number, signature, etc.
3. The tool stamps a diagonal watermark across the image naming the recipient, the purpose, and the date.
4. You download the result as a JPEG and send only that.

## Privacy

The entire tool runs in your browser:

- No servers, no uploads, no API calls.
- No cookies, no localStorage, no tracking scripts.
- No third-party scripts at runtime — not even for HEIC decoding. That means there is no CDN that could be compromised to attack the page.
- You can save the page (Ctrl+S / ⌘+S) and use it fully offline.

## Why

Several EU data-protection authorities explicitly recommend redacting non-essential fields and watermarking ID copies with the recipient, purpose, and date. The page summarises each authority's concrete advice with direct links to the source:

- [Rijksoverheid](https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs) & [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs) (Netherlands)
- [CNIL](https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite) (France)
- [Verbraucherzentrale Niedersachsen](https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl) & [BfDI](https://www.bfdi.bund.de/) (Germany)
- [AEPD](https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni) (Spain)
- [Gegevensbeschermingsautoriteit (APD/GBA)](https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/elektronische-identiteitskaart-eid/praktische-toepassingen) (Belgium)
- [UODO](https://uodo.gov.pl/pl/138/2476) (Poland)

This project is not affiliated with any of the above bodies.

## Tech

Plain HTML + CSS + a single inline `<script>`. No dependencies, no bundler, and nothing to build at deploy time: GitHub Pages serves the committed files from `main`.

## Repository layout

```
index.html      English version (served at /)
de/index.html   German version  (served at /de/)
fr/index.html   French version  (served at /fr/)
nl/index.html   Dutch version   (served at /nl/)
es/index.html   Spanish version (served at /es/)
pl/index.html   Polish version  (served at /pl/)
i18n/build.py   Generates the translated pages from index.html
i18n/<code>.py  One file per translation (metadata, body text, script strings)
sitemap.xml     Lists all language variants with hreflang alternates
robots.txt      Points crawlers at the sitemap
CNAME           Custom domain for GitHub Pages
```

## Translations

`index.html` is the single source for the markup, styles and script. The translated pages are generated from it, so a change to how the tool works only has to be made once:

- **Changing the tool or the layout:** edit `index.html`, then run `python3 i18n/build.py` and commit the regenerated pages alongside it.
- **Changing translated text:** edit `i18n/<code>.py` (the page metadata, the body from `<h1>` to `</main>`, and the strings in the script), then run the build.
- **Changing English body text:** edit `index.html` and make the matching edit in each `i18n/<code>.py` — the body text is translated by hand, not copied.

`python3 i18n/build.py --check` exits non-zero if any generated page is out of date. The script needs only Python 3, no packages. Adding a language is described at the top of `i18n/build.py`.

## Contributing

Pull requests are welcome, especially translations into additional languages, or additions of genuinely concrete official guidance from other countries' data-protection authorities. The bar for a new regulator is: they must publish concrete, consumer-facing advice on which fields to redact and/or what to write on the copy — not just generic "protect your data" material.
