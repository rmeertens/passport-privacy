# passport-privacy

A tiny, single-page browser tool for safely sharing a copy of your passport or ID card.

Live at **[passport-privacy.meertens.dev](https://passport-privacy.meertens.dev/)** in English, German (`/de/`), and French (`/fr/`).

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

Plain HTML + CSS + a single inline `<script>`. No build step, no dependencies, no bundler. Deployed via GitHub Pages from `main`.

## Repository layout

```
index.html      English version (served at /)
de/index.html   German version  (served at /de/)
fr/index.html   French version  (served at /fr/)
sitemap.xml     Lists all three language variants with hreflang alternates
robots.txt      Points crawlers at the sitemap
CNAME           Custom domain for GitHub Pages
```

## Contributing

Pull requests are welcome, especially translations into additional languages, or additions of genuinely concrete official guidance from other countries' data-protection authorities. The bar for a new regulator is: they must publish concrete, consumer-facing advice on which fields to redact and/or what to write on the copy — not just generic "protect your data" material.
