# Dutch (nl) translation of ../index.html. After editing, run: python3 i18n/build.py

CODE = 'nl'
NAV_LABEL = 'Taal'
TITLE = 'Veilige kopie paspoort of ID-kaart – watermerk &amp; afschermen'
DESC = 'Zet een watermerk op een kopie van je paspoort of ID-kaart en scherm je BSN en andere gegevens af — volledig in je browser. Niets wordt geüpload, niets wordt opgeslagen.'
OG_TITLE = 'Veilige kopie ID-bewijs: watermerk &amp; afschermen'
OG_DESC = 'Scherm persoonsgegevens af en zet een watermerk op een kopie van je paspoort of ID-kaart — volledig in je browser. Geen uploads, geen trackers.'
TW_DESC = 'Scherm af en zet een watermerk op een kopie van je ID — volledig in je browser. Geen uploads, geen trackers.'
OG_ALT = "Een nagemaakt paspoort met afgeschermde velden en een diagonaal COPY-watermerk, naast de kop 'Watermark your ID copy.'"
TW_ALT = 'Een nagemaakt paspoort met afgeschermde velden en een diagonaal COPY-watermerk.'
LD_NAME = 'Veilige kopie paspoort of ID-kaart – watermerk & afschermen'
LD_DESC = 'Een browsertool die persoonsgegevens afschermt en een watermerk met doel en datum op een kopie van je paspoort of ID-kaart zet. Geen uploads, geen trackers — je gegevens verlaten je apparaat nooit.'

# (English source, translation) pairs for user-facing strings inside the <script>.
JS = [
    ("'HEIC files can\\'t be decoded safely in the browser without a third-party library. ' +\n            'Please convert the photo to JPEG or PNG first — see the instructions below.'",
     "'HEIC-bestanden kunnen niet veilig in de browser worden geopend zonder externe bibliotheek. ' +\n            'Zet de foto eerst om naar JPEG of PNG — zie de uitleg hieronder.'"),
    ("'That file is not an image. Try again.'",
     "'Dat bestand is geen afbeelding. Probeer het opnieuw.'"),
    ("'loaded locally. Drop a new image to replace.'",
     "'lokaal geladen. Sleep een nieuwe afbeelding hierheen om te vervangen.'"),
    ("'Could not read that image. Try a different file.'",
     "'Kan deze afbeelding niet lezen. Probeer een ander bestand.'"),
    ('\'This browser does not support live camera access. Use "Choose an existing image" instead.\'',
     '\'Deze browser ondersteunt geen cameratoegang. Gebruik in plaats daarvan "Kies een bestaande afbeelding".\''),
    ("'Camera access denied or unavailable: '",
     "'Cameratoegang geweigerd of niet beschikbaar: '"),
    ("'(purpose not set)'",
     "'(doel niet ingevuld)'"),
    ("'COPY  •  '",
     "'KOPIE  •  '"),
    ("'(date not set)'",
     "'(datum niet ingevuld)'"),
]

# Everything from <h1> up to (not including) </main>.
BODY = """\
      <h1>Veilige kopie van je paspoort of ID-kaart</h1>
      <p class="hero-copy">
        Upload of fotografeer je paspoort of ID-kaart, scherm de gegevens af die je niet wilt delen en zet er een
        diagonaal watermerk op met het doel en de datum — helemaal in je browser.
      </p>
      <a class="back" href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">⟨/⟩ Bekijk de broncode op GitHub — open source, geen verborgen code</a>
    </header>

    <main>
      <section class="card tool">
        <h2>1. Voeg je paspoort of ID-kaart toe</h2>
        <noscript><p class="status error">Deze tool heeft JavaScript nodig, maar dat staat uit in je browser. Alles draait op je eigen apparaat — er wordt niets geüpload.</p></noscript>
        <p class="hint">Kies een bestand op je apparaat of maak een foto met je camera. In beide gevallen blijft de afbeelding in deze browser.</p>

        <label class="file-drop" id="drop">
          <input type="file" id="file" accept="image/*,.heic,.heif,image/heic,image/heif" />
          <span id="drop-label">Sleep een afbeelding hierheen of klik om een bestand te kiezen (JPEG of PNG)</span>
        </label>

        <details id="heic-help" class="heic-help">
          <summary>Een <code>.HEIC</code>-foto van een iPhone? Zo zet je die eerst om</summary>
          <p>
            HEIC is het standaard fotoformaat van Apple. Deze tool bevat bewust geen HEIC-decoder, omdat elke
            externe decoder die tijdens het gebruik wordt geladen een supply-chain-risico is voor een pagina die
            met je paspoort werkt. Zo zet je HEIC lokaal om naar JPEG:
          </p>
          <ul>
            <li>
              <strong>iPhone / iPad</strong> — het eenvoudigst: open Instellingen → Camera → Formaten → kies
              <em>Meest compatibel</em> en maak de foto opnieuw; nieuwe foto's worden dan JPEG. Voor een bestaande
              HEIC: open de foto in de app Bestanden, houd hem ingedrukt, kies Deel → <em>Bewaar in Bestanden</em>
              met de optie "JPEG", of gebruik de ingebouwde actie <em>Converteer afbeelding</em> in de app
              Opdrachten.
            </li>
            <li>
              <strong>macOS</strong> — dubbelklik op de HEIC om hem in Voorvertoning te openen en kies Archief →
              Exporteer… → stel Structuur in op JPEG.
            </li>
            <li>
              <strong>Windows 10/11</strong> — installeer de gratis "HEIF-afbeeldingsextensies" van Microsoft uit
              de Microsoft Store, open het bestand in Foto's en kies "Opslaan als" → JPEG.
            </li>
            <li>
              <strong>Android</strong> — de meeste Android-telefoons slaan foto's al op als JPEG. Heb je een HEIC
              ontvangen, open hem dan in Google Foto's → menu → "Opslaan als" / "Exporteren".
            </li>
          </ul>
          <p style="margin-bottom: 0;">
            <strong>Gebruik hiervoor liever geen online HEIC-converters</strong> — je paspoort uploaden naar een
            willekeurige conversiedienst gaat volledig voorbij aan het doel van deze tool.
          </p>
        </details>

        <div class="upload-row">
          <button type="button" id="start-camera">📷 Maak een foto met mijn camera</button>
          <button type="button" id="pick-file">🖼️ Kies een bestaande afbeelding</button>
        </div>

        <div class="camera-panel" id="camera-panel" hidden>
          <video id="video" playsinline muted></video>
          <div class="actions">
            <button type="button" id="shutter" class="primary">Foto maken</button>
            <button type="button" id="flip-camera">Wissel camera</button>
            <button type="button" id="cancel-camera">Annuleren</button>
          </div>
          <p class="status" id="camera-status"></p>
        </div>

        <h2>2. Vul het watermerk in</h2>
        <div class="form-grid">
          <label>
            Voor wie en waarvoor? (verplicht — deze tekst komt in het watermerk)
            <input type="text" id="purpose" placeholder="bijv. huurcontract met Woonbedrijf BV" maxlength="140" autocomplete="off" required value="inchecken vakantiewoning" />
          </label>
          <label>
            Datum van afgeven
            <input type="date" id="date" />
          </label>
        </div>

        <div id="editor" hidden>
          <h2>3. Scherm af wat je niet wilt delen</h2>
          <p class="hint">
            Sleep over de afbeelding om een zwart vlak te tekenen over elk veld dat je liever niet deelt.
            Op Nederlandse paspoorten en ID-kaarten scherm je meestal het <strong>BSN</strong> af, ook de
            <strong>QR-code</strong> waarin het BSN staat, plus het <strong>documentnummer</strong>, je
            <strong>handtekening</strong> en de <strong>MRZ</strong> (de regels met &lt;&lt;&lt;-tekst).
          </p>
          <div class="canvas-wrap">
            <canvas id="canvas"></canvas>
          </div>
          <label class="check">
            <input type="checkbox" id="limit-res" checked />
            <span>Verlaag de resolutie (max. 1200 pixels) — nog steeds leesbaar, maar lastiger te hergebruiken of te vervalsen</span>
          </label>
          <div class="actions">
            <button type="button" id="undo">Laatste vlak ongedaan maken</button>
            <button type="button" id="clear-blackouts" class="danger">Alle vlakken wissen</button>
            <button type="button" id="download" class="primary">⬇ Download kopie met watermerk (JPEG)</button>
          </div>
          <p class="hint" style="margin-top: 12px;">
            Tip: het watermerk past zich direct aan terwijl je typt. Maak het doel specifiek (voor wie, waarvoor)
            zodat duidelijk is dat de kopie maar voor één keer bedoeld is.
          </p>
        </div>
      </section>

      <section class="card privacy-card">
        <h2>🔒 Je afbeelding verlaat dit browsertabblad nooit</h2>
        <ul>
          <li>Geen uploadservers. Geen API-aanroepen. Geen analytics. Geen trackers.</li>
          <li>Alles draait in pure JavaScript op je eigen apparaat.</li>
          <li>Er wordt niets bewaard — niet in cookies, niet in localStorage, nergens.</li>
          <li>Ververs de pagina en het is weg. Sluit het tabblad en het is weg.</li>
          <li>Je kunt deze pagina zelfs opslaan (Ctrl+S / ⌘+S) en volledig offline gebruiken.</li>
          <li>De gedownloade JPEG is een opnieuw getekende afbeelding: verborgen fotogegevens zoals je GPS-locatie of cameragegevens gaan niet mee.</li>
          <li>
            Deze pagina laadt bewust <em>geen enkel</em> extern script — zelfs niet voor zaken als
            HEIC-decodering — dus er is geen CDN dat gehackt kan worden om jouw kopie van de pagina aan te vallen.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Dit is belangrijk, want een foto van je ID-bewijs is gevoelige informatie: je volledige naam,
          geboortedatum, documentnummer, handtekening, pasfoto en — op Nederlandse documenten — je BSN.
          Zo'n kopie onbeschermd rondsturen is een geliefd ingrediënt voor identiteitsfraude.
        </p>
      </section>

      <section class="card">
        <h2>Wat de Nederlandse overheid adviseert</h2>
        <p>
          Twee officiële bronnen geven hetzelfde advies over het delen van een kopie van een Nederlands
          identiteitsbewijs:
          <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs" target="_blank" rel="noopener">Rijksoverheid</a>
          en de
          <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>
          (de Nederlandse privacytoezichthouder). Kort samengevat:
        </p>
        <ul>
          <li>Maak je <strong>BSN</strong> (burgerservicenummer) onleesbaar op de kopie — <em>ook</em> in de machineleesbare cijfers onderaan het document.</li>
          <li>Je mag ook je <strong>pasfoto</strong> en <strong>handtekening</strong> afschermen.</li>
          <li>Zet op de kopie dat het een <strong>kopie</strong> is, en voor wie / voor welk product of doel de kopie bedoeld is.</li>
          <li>Zet op de kopie de <strong>datum</strong> waarop je de kopie afgeeft.</li>
        </ul>
        <p>
          De Autoriteit Persoonsgegevens zegt er duidelijk bij dat sommige organisaties — bijvoorbeeld
          telecomaanbieders en autoverhuurbedrijven — je BSN en pasfoto niet eens mogen verwerken, en die zelf
          moeten afschermen als ze een kopie maken.
        </p>
        <p>
          Let op de QR-code: op Nederlandse paspoorten en ID-kaarten die vanaf <strong>2 augustus 2021</strong> zijn
          uitgegeven, is het BSN uit de machineleesbare regels gehaald en verplaatst naar een <strong>QR-code</strong>
          — op de achterkant van de ID-kaart en op de fotopagina van het paspoort. Scherm die QR-code dus ook af.
          Op oudere documenten kan het BSN ook als getal op de voor- of achterkant staan: scherm elke plek af
          waar het staat.
        </p>
        <p style="margin-bottom: 0;">
          Liever een app? De Rijksoverheid heeft hiervoor een eigen gratis app, <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/veilige-kopie-identiteitsbewijs" target="_blank" rel="noopener">KopieID</a>
          (iPhone en Android): je schermt de gegevens af die de ontvanger niet nodig heeft en zet er een
          watermerk met het doel op.
        </p>
      </section>

      <section class="card">
        <h2>Vergelijkbaar advies van andere Europese toezichthouders</h2>
        <p>
          Verschillende andere privacytoezichthouders in de EU geven vergelijkbaar advies: scherm de velden af
          die de ontvanger niet strikt nodig heeft, en zet het doel en de datum op de kopie. Deze tool werkt
          voor al die gevallen — vul bij het doel gewoon de formulering in die de toezichthouder aanraadt.
        </p>
        <ul>
          <li>
            <strong>Frankrijk — <a href="https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite" target="_blank" rel="noopener">CNIL</a>.</strong>
            Zet een zichtbaar watermerk met de ontvanger, het doel en de datum — het voorbeeld van de CNIL zelf is
            <em>"Document transmis uniquement pour l'ouverture d'un compte chez [organisme] – [date]"</em>.
            De CNIL raadt ook aan de resolutie van de kopie te beperken, zodat die lastiger te hergebruiken is.
          </li>
          <li>
            <strong>Duitsland — <a href="https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl" target="_blank" rel="noopener">Verbraucherzentrale Niedersachsen</a>.</strong>
            Scherm op een Personalausweis het documentnummer, het toegangs-/serienummer, de oogkleur, lengte,
            nationaliteit, handtekening en geboorteplaats/-datum af, en zet er een watermerk op met de ontvanger
            en het doel. Sinds de wijziging van de PAuswG in 2017 hoeven normaal alleen naam, adres, geboortedatum
            en geldigheid zichtbaar te blijven voor een identiteitscontrole.
          </li>
          <li>
            <strong>Spanje — <a href="https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni" target="_blank" rel="noopener">AEPD</a>.</strong>
            Wis of vervaag op de voorkant van een DNI het supportnummer, geslacht, nationaliteit, geboortedatum en
            handtekening; op de achterkant het adres, de geboorteplaats en de namen van de ouders. Alleen naam,
            achternamen, documentnummer en foto hoeven te blijven — plus een zichtbare notitie met doel en datum.
          </li>
          <li>
            <strong>België — <a href="https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/elektronische-identiteitskaart-eid/praktische-toepassingen" target="_blank" rel="noopener">Gegevensbeschermingsautoriteit (GBA)</a>.</strong>
            Geef alleen een doorstreepte kopie af en scherm elk veld af dat niet strikt nodig is — vooral het
            rijksregisternummer, het kaartnummer van de eID, de geldigheidsdata, het geslacht, de nationaliteit
            en de geboorteplaats/-datum — en schrijf op de kopie de naam van de ontvanger en het specifieke
            toegestane gebruik.
          </li>
          <li>
            <strong>Polen — <a href="https://uodo.gov.pl/pl/138/2476" target="_blank" rel="noopener">UODO</a>.</strong>
            Als een kopie van een <em>dowód osobisty</em> echt onvermijdelijk is, scherm dan elk veld af dat het
            doel van het contract niet strikt vereist. UODO geeft er de voorkeur aan dat het document persoonlijk
            wordt getoond in plaats van gekopieerd.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          De rode draad in al deze adviezen — en in de Nederlandse richtlijnen hierboven — is steeds dezelfde:
          deel zo min mogelijk, zet doel en datum in het watermerk, en houd bij wie de kopie heeft gekregen.
        </p>
      </section>

      <section class="card">
        <h2>En in het Verenigd Koninkrijk?</h2>
        <p>
          Britse consumentenadviezen over de veiligheid van identiteitsdocumenten zijn verspreid over drie
          instanties, en — anders dan de Nederlandse bronnen — publiceert geen van hen een stappenplan voor het
          afschermen van een paspoortkopie. Hun advies draait vooral om voorkomen, melden en preventieve
          registratie:
        </p>
        <ul>
          <li>
            <a href="https://ico.org.uk/for-the-public/identity-theft/" target="_blank" rel="noopener">Information Commissioner's Office (ICO) — Identity theft</a>:
            de consumentenpagina van de Britse toezichthouder. Legt de waarschuwingssignalen uit, wat je moet doen
            als je denkt dat je gegevens zijn uitgelekt, en raadt aan verloren of gestolen ID-bewijzen te melden
            bij de uitgevende instantie.
          </li>
          <li>
            <a href="https://www.actionfraud.police.uk/a-z-of-fraud/identity-fraud-and-identity-theft" target="_blank" rel="noopener">Action Fraud — Identity fraud and identity theft</a>:
            het nationale meldpunt voor fraude in het VK. Raadt aan persoonlijke documenten achter slot en grendel
            te bewaren, alles met je naam erop te vernietigen voordat je het weggooit, en verloren of gestolen
            paspoorten te melden bij HM Passport Office.
          </li>
          <li>
            <a href="https://www.cifas.org.uk/services/identity-protection" target="_blank" rel="noopener">Cifas — Identity protection</a>:
            de Britse fraudepreventiedienst. Tegen een kleine vergoeding kun je <em>Protective Registration</em>
            aanvragen, zodat aanvragen voor krediet of rekeningen op jouw naam extra worden gecontroleerd.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Het onderliggende principe is in elk land hetzelfde: deel zo min mogelijk, met zo min mogelijk mensen,
          zo kort mogelijk, en houd bij naar wie je het hebt gestuurd. Afschermen wat een ontvanger niet strikt
          nodig heeft en het doel op de kopie zetten werkt in elk land — ook al is het alleen de Nederlandse
          overheid die het zo gedetailleerd uitlegt.
        </p>
      </section>

      <section class="card">
        <h2>Voordat je je kopie verstuurt</h2>
        <ul>
          <li>Open de gedownloade afbeelding en zoom in: is alles wat je wilde afschermen echt bedekt, ook de QR-code? Is het watermerk leesbaar?</li>
          <li>Verstuur bij voorkeur via een end-to-end versleuteld kanaal. Vermijd gewone e-mail als dat kan.</li>
          <li>Noteer de ontvanger en de datum. Duikt de kopie ooit ergens anders op, dan weet je wie hem had.</li>
          <li>In Nederland mag een winkel, hotel, sportschool of verhuurder meestal geen kopie van je ID zonder afscherming eisen. Vraagt iemand daar toch om, dan is dat vaak een waarschuwingssignaal.</li>
          <li>Sommige organisaties moeten wettelijk bepaalde gegevens zien — je werkgever heeft bijvoorbeeld je BSN nodig voor de loonadministratie, en banken moeten je identiteit controleren vanwege de witwasregels. Twijfel je? Vraag de ontvanger welke gegevens echt nodig zijn.</li>
          <li>Verwijder de kopie na het versturen uit je map Downloads, en laat hem niet rondslingeren in chats of conceptmails.</li>
        </ul>
      </section>

      <footer>
        Een klein open-source experiment dat het advies volgt van de
        <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs" target="_blank" rel="noopener">Rijksoverheid</a>
        en de
        <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>.
        Er worden geen gegevens verzameld — geloof ons niet op ons woord:
        <a href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">lees de broncode op GitHub</a>.
      </footer>
"""
