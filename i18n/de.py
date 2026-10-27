# German (de) translation of ../index.html. After editing, run: python3 i18n/build.py

CODE = 'de'
NAV_LABEL = 'Sprache'
TITLE = 'Ausweiskopie: Wasserzeichen &amp; Schwärzen-Tool'
DESC = 'Fügen Sie Wasserzeichen hinzu und schwärzen Sie persönliche Angaben auf einer Kopie Ihres Personalausweises oder Reisepasses — vollständig im Browser. Nichts wird hochgeladen, nichts gespeichert.'
OG_TITLE = 'Ausweiskopie: Wasserzeichen &amp; Schwärzen'
OG_DESC = 'Ausweiskopien lokal im Browser schwärzen und mit Wasserzeichen versehen — ohne Uploads, ohne Tracker.'
TW_DESC = 'Ausweiskopien lokal schwärzen und mit Wasserzeichen versehen — ohne Uploads, ohne Tracker.'
OG_ALT = 'Nachgebildeter Ausweis mit geschwärzten Feldern und diagonalem COPY-Wasserzeichen, daneben die Überschrift „Watermark your ID copy.“.'
TW_ALT = 'Nachgebildeter Ausweis mit geschwärzten Feldern und diagonalem COPY-Wasserzeichen.'
LD_NAME = 'Ausweiskopie: Wasserzeichen & Schwärzen'
LD_DESC = 'Ein Browser-Tool, das persönliche Angaben auf einer Ausweiskopie schwärzt und ein Wasserzeichen mit Zweck und Datum aufbringt. Keine Uploads, keine Tracker — die Daten verlassen Ihr Gerät nicht.'

# (English source, translation) pairs for user-facing strings inside the <script>.
JS = [
    ("'HEIC files can\\'t be decoded safely in the browser without a third-party library. ' +",
     "'HEIC-Dateien können ohne externe Bibliothek nicht sicher im Browser dekodiert werden. ' +"),
    ("'Please convert the photo to JPEG or PNG first — see the instructions below.';",
     "'Bitte konvertieren Sie das Foto zuerst in JPEG oder PNG — siehe Anleitung unten.';"),
    ("dropLabel.textContent = 'That file is not an image. Try again.';",
     "dropLabel.textContent = 'Diese Datei ist kein Bild. Bitte erneut versuchen.';"),
    ("dropLabel.textContent = (name ? name + ' — ' : '') + 'loaded locally. Drop a new image to replace.';",
     "dropLabel.textContent = (name ? name + ' — ' : '') + 'lokal geladen. Ein neues Bild einfach drüberziehen.';"),
    ("dropLabel.textContent = 'Could not read that image. Try a different file.';",
     "dropLabel.textContent = 'Dieses Bild konnte nicht gelesen werden. Bitte eine andere Datei versuchen.';"),
    ('camStatus.textContent = \'This browser does not support live camera access. Use "Choose an existing image" instead.\';',
     "camStatus.textContent = 'Dieser Browser unterstützt keinen direkten Kamerazugriff. Verwenden Sie stattdessen „Vorhandenes Bild auswählen“.';"),
    ("camStatus.textContent = 'Camera access denied or unavailable: ' + err.message;",
     "camStatus.textContent = 'Kamerazugriff verweigert oder nicht verfügbar: ' + err.message;"),
    ("const purpose = (purposeEl.value || '').trim() || '(purpose not set)';",
     "const purpose = (purposeEl.value || '').trim() || '(Zweck nicht angegeben)';"),
    ("const text = 'COPY  •  ' + purpose + '  •  ' + dateStr;",
     "const text = 'KOPIE  •  ' + purpose + '  •  ' + dateStr;"),
    ("if (!iso) return '(date not set)';",
     "if (!iso) return '(Datum nicht angegeben)';"),
    ("return parts[2] + '-' + parts[1] + '-' + parts[0]; // DD-MM-YYYY, Dutch style",
     "return parts[2] + '.' + parts[1] + '.' + parts[0]; // DD.MM.YYYY, deutsche Schreibweise"),
]

# Everything from <h1> up to (not including) </main>.
BODY = """\
      <h1>Ausweiskopie: Wasserzeichen &amp; Schwärzen</h1>
      <p class="hero-copy">
        Laden Sie einen Scan Ihres Personalausweises oder Reisepasses hoch oder fotografieren Sie ihn, schwärzen
        Sie die persönlichen Angaben, die Sie nicht weitergeben möchten, und versehen Sie die Kopie mit einem
        diagonalen Wasserzeichen aus Zweck und Datum — alles geschieht ausschließlich in Ihrem Browser.
      </p>
      <a class="back" href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">⟨/⟩ Quellcode auf GitHub ansehen — Open Source, kein versteckter Code</a>
    </header>

    <main>
      <section class="card tool">
        <h2>1. Ausweis oder Reisepass hinzufügen</h2>
        <noscript><p class="status error">Dieses Tool benötigt JavaScript, das in Ihrem Browser deaktiviert ist. Es läuft vollständig auf Ihrem Gerät — nichts wird hochgeladen.</p></noscript>
        <p class="hint">Wählen Sie eine Datei von Ihrem Gerät aus oder machen Sie ein Foto mit Ihrer Kamera. Beides bleibt vollständig in diesem Browser.</p>

        <label class="file-drop" id="drop">
          <input type="file" id="file" accept="image/*,.heic,.heif,image/heic,image/heif" />
          <span id="drop-label">Bild hierher ziehen oder klicken, um eine Datei auszuwählen (JPEG oder PNG)</span>
        </label>

        <details id="heic-help" class="heic-help">
          <summary>Sie haben ein <code>.HEIC</code>-Foto vom iPhone? So konvertieren Sie es</summary>
          <p>
            HEIC ist das Standard-Fotoformat von Apple. Dieses Tool bindet bewusst keinen HEIC-Decoder ein,
            denn jeder zur Laufzeit geladene Decoder eines Drittanbieters wäre ein Supply-Chain-Risiko für
            eine Seite, die mit Ihrem Ausweis umgeht. So konvertieren Sie HEIC lokal zu JPEG:
          </p>
          <ul>
            <li>
              <strong>iPhone / iPad</strong> — am einfachsten: Einstellungen → Kamera → Formate →
              <em>Maximale Kompatibilität</em> wählen und das Foto neu aufnehmen; neue Fotos werden dann
              als JPEG gespeichert. Für ein bestehendes HEIC öffnen Sie es in der Dateien-App,
              halten Sie es gedrückt, wählen Sie Teilen → <em>In „Dateien“ sichern</em> mit der
              JPEG-Option, oder nutzen Sie die Aktion <em>Bild konvertieren</em> in der Kurzbefehle-App.
            </li>
            <li>
              <strong>macOS</strong> — HEIC doppelklicken, um es in der Vorschau zu öffnen, dann Ablage →
              Exportieren… → Format auf JPEG setzen.
            </li>
            <li>
              <strong>Windows 10/11</strong> — die kostenlose Microsoft-Erweiterung „HEIF-Bilderweiterungen“
              aus dem Microsoft Store installieren, die Datei in Fotos öffnen und über „Speichern unter“ →
              JPEG exportieren.
            </li>
            <li>
              <strong>Android</strong> — die meisten Android-Geräte speichern Fotos ohnehin als JPEG.
              Wenn Sie ein HEIC erhalten haben, öffnen Sie es in Google Fotos → Menü → „Speichern
              unter“ / „Exportieren“.
            </li>
          </ul>
          <p style="margin-bottom: 0;">
            Bitte <strong>verwenden Sie keine Online-HEIC-Konverter</strong> — das Hochladen Ihres Ausweises
            zu einem zufälligen Dienst widerspricht dem Sinn dieses Tools.
          </p>
        </details>

        <div class="upload-row">
          <button type="button" id="start-camera">📷 Foto mit der Kamera aufnehmen</button>
          <button type="button" id="pick-file">🖼️ Vorhandenes Bild auswählen</button>
        </div>

        <div class="camera-panel" id="camera-panel" hidden>
          <video id="video" playsinline muted></video>
          <div class="actions">
            <button type="button" id="shutter" class="primary">Aufnehmen</button>
            <button type="button" id="flip-camera">Kamera wechseln</button>
            <button type="button" id="cancel-camera">Abbrechen</button>
          </div>
          <p class="status" id="camera-status"></p>
        </div>

        <h2>2. Wasserzeichen ausfüllen</h2>
        <div class="form-grid">
          <label>
            Für wen und wofür? (Pflichtfeld — dieser Text erscheint im Wasserzeichen)
            <input type="text" id="purpose" placeholder="z. B. Mietvertrag mit Beispiel GmbH" maxlength="140" autocomplete="off" required value="Check-in Ferienwohnung" />
          </label>
          <label>
            Datum der Weitergabe
            <input type="date" id="date" />
          </label>
        </div>

        <div id="editor" hidden>
          <h2>3. Alles schwärzen, was Sie nicht teilen möchten</h2>
          <p class="hint">
            Ziehen Sie mit der Maus über das Bild, um ein schwarzes Rechteck über Felder zu legen, die Sie
            nicht teilen möchten. Beim deutschen Personalausweis sollten Sie typischerweise die
            <strong>Ausweisnummer</strong>, die <strong>Zugangs-/Seriennummer</strong>, die
            <strong>Unterschrift</strong> und die <strong>MRZ</strong> (die Zeilen mit
            &lt;&lt;&lt;) schwärzen. Decken Sie auch jeden <strong>QR-Code</strong> ab — er kann dieselben
            Daten maschinenlesbar enthalten.
          </p>
          <div class="canvas-wrap">
            <canvas id="canvas"></canvas>
          </div>
          <label class="check">
            <input type="checkbox" id="limit-res" checked />
            <span>Auflösung verringern (max. 1200 Pixel) — weiterhin lesbar, aber schwerer weiterzuverwenden oder zu fälschen</span>
          </label>
          <div class="actions">
            <button type="button" id="undo">Letzte Schwärzung rückgängig</button>
            <button type="button" id="clear-blackouts" class="danger">Alle Schwärzungen entfernen</button>
            <button type="button" id="download" class="primary">⬇ Kopie mit Wasserzeichen herunterladen (JPEG)</button>
          </div>
          <p class="hint" style="margin-top: 12px;">
            Tipp: Das Wasserzeichen aktualisiert sich live beim Tippen. Formulieren Sie den Zweck konkret
            (für wen, wofür), damit die Kopie eindeutig als einmalig nutzbar erkennbar ist.
          </p>
        </div>
      </section>

      <section class="card privacy-card">
        <h2>🔒 Ihr Bild verlässt diesen Browser-Tab nicht</h2>
        <ul>
          <li>Keine Upload-Server. Keine API-Aufrufe. Keine Analytics. Keine Tracker.</li>
          <li>Alles läuft in reinem JavaScript auf Ihrem Gerät.</li>
          <li>Nichts wird gespeichert — nicht in Cookies, nicht im localStorage, nirgendwo.</li>
          <li>Seite aktualisieren und es ist weg. Tab schließen und es ist weg.</li>
          <li>Sie können diese Seite sogar speichern (Strg+S / ⌘+S) und vollständig offline nutzen.</li>
          <li>Das heruntergeladene JPEG wird neu erzeugt: versteckte Foto-Metadaten wie GPS-Standort oder Kameradaten werden nicht übernommen.</li>
          <li>
            Diese Seite lädt zur Laufzeit bewusst <em>keine</em> Drittanbieter-Skripte nach — nicht einmal
            für HEIC-Dekodierung — es gibt also kein CDN, das kompromittiert werden könnte, um Ihre Kopie
            der Seite anzugreifen.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Das ist wichtig, denn ein Foto Ihres Ausweises ist sensibel: Es enthält Ihren vollständigen Namen,
          Geburtsdatum, Dokumentennummer, Unterschrift und Lichtbild — alles zusammen eine beliebte Zutat
          für Identitätsdiebstahl.
        </p>
      </section>

      <section class="card">
        <h2>Empfehlungen deutscher Stellen</h2>
        <p>
          Zwei Quellen geben in Deutschland die konkretesten Empfehlungen für die Weitergabe einer
          Ausweiskopie: die
          <a href="https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl" target="_blank" rel="noopener">Verbraucherzentrale Niedersachsen</a>
          und die
          <a href="https://www.bfdi.bund.de/" target="_blank" rel="noopener">Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)</a>.
          Kurz zusammengefasst:
        </p>
        <ul>
          <li>Schwärzen Sie Felder, die der Empfänger nicht zwingend braucht — typischerweise die
            <strong>Ausweisnummer</strong>, die <strong>Zugangs-/Seriennummer</strong>,
            <strong>Augenfarbe</strong>, <strong>Körpergröße</strong>, <strong>Staatsangehörigkeit</strong>,
            <strong>Geburtsort und -datum</strong> und die <strong>Unterschrift</strong>.</li>
          <li>Sie dürfen auch das <strong>Lichtbild</strong> schwärzen, wenn der Zweck das nicht erfordert.</li>
          <li>Schreiben Sie auf die Kopie, dass es sich um eine <strong>Kopie</strong> handelt, für wen sie
            bestimmt ist und zu welchem Zweck.</li>
          <li>Notieren Sie das <strong>Datum</strong>, an dem Sie die Kopie weitergeben.</li>
        </ul>
        <p>
          Seit der Änderung des Personalausweisgesetzes 2017 genügt für eine Identitätsprüfung in der
          Regel, wenn Name, Anschrift, Geburtsdatum und Gültigkeitsdauer lesbar bleiben — alle übrigen Felder
          dürfen geschwärzt werden.
        </p>
        <p style="margin-bottom: 0;">
          Gut zu wissen: Auf deutschen Ausweisen ist kein BSN-Äquivalent aufgedruckt, jedoch steht die
          <em>Zugangs-/Seriennummer</em> (auch CAN genannt) auf der Vorderseite und sollte wie die
          Ausweisnummer geschwärzt werden, sofern der Empfänger sie nicht ausdrücklich benötigt.
        </p>
      </section>

      <section class="card">
        <h2>Ähnliche Empfehlungen anderer europäischer Behörden</h2>
        <p>
          Mehrere europäische Datenschutzbehörden geben vergleichbar konkrete Empfehlungen: nicht benötigte
          Felder schwärzen und die Kopie mit Zweck und Datum versehen. Dieses Tool funktioniert für alle
          davon — tragen Sie einfach in das Zweck-Feld ein, was die jeweilige Behörde empfiehlt.
        </p>
        <ul>
          <li>
            <strong>Niederlande — <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>.</strong>
            Den BSN (Bürgerservicenummer, einschließlich in der MRZ), das Lichtbild und die Unterschrift
            schwärzen. Auf der Kopie notieren, dass es eine Kopie ist, für wen und wofür sie bestimmt ist,
            sowie das Datum. Bei Dokumenten ab dem 2. August 2021 steckt der BSN in einem QR-Code (Rückseite der ID-Karte,
            Datenseite des Reisepasses) — diesen QR-Code ebenfalls schwärzen.
            Die niederländische Regierung bietet dafür auch eine eigene kostenlose App an: <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/veilige-kopie-identiteitsbewijs" target="_blank" rel="noopener">KopieID</a>
            (iPhone und Android).
          </li>
          <li>
            <strong>Frankreich — <a href="https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite" target="_blank" rel="noopener">CNIL</a>.</strong>
            Ein sichtbares Wasserzeichen mit Empfänger, Zweck und Datum anbringen — das Beispiel der CNIL
            lautet <em>„Document transmis uniquement pour l'ouverture d'un compte chez [organisme] – [date]“</em>.
            Die CNIL empfiehlt zudem, die Auflösung der Kopie zu reduzieren, damit sie schwerer weiterverwendbar ist.
          </li>
          <li>
            <strong>Spanien — <a href="https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni" target="_blank" rel="noopener">AEPD</a>.</strong>
            Auf der Vorderseite des DNI die Support-Nummer, das Geschlecht, die Staatsangehörigkeit, das
            Geburtsdatum und die Unterschrift schwärzen; auf der Rückseite die Anschrift, den Geburtsort und
            die Namen der Eltern. Nur Name, Nachnamen, Dokumentennummer und Lichtbild müssen sichtbar bleiben
            — zuzüglich eines sichtbaren Vermerks mit Zweck und Datum.
          </li>
          <li>
            <strong>Belgien — <a href="https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/elektronische-identiteitskaart-eid/praktische-toepassingen" target="_blank" rel="noopener">Gegevensbeschermingsautoriteit (APD/GBA)</a>.</strong>
            Nur eine durchgestrichene (<em>doorstreept</em>) Kopie weitergeben und jedes Feld überdecken, das
            nicht zwingend erforderlich ist — besonders die Rijksregisternummer, die eID-Kartennummer,
            Gültigkeitsdaten, Geschlecht, Staatsangehörigkeit sowie Geburtsort und -datum. Auf der Kopie
            Empfänger und autorisierten Zweck vermerken.
          </li>
          <li>
            <strong>Polen — <a href="https://uodo.gov.pl/pl/138/2476" target="_blank" rel="noopener">UODO</a>.</strong>
            Wo eine Kopie des <em>dowód osobisty</em> unvermeidbar ist, jedes Feld überdecken, das der
            Vertragszweck nicht zwingend verlangt. Die UODO bevorzugt, dass das Dokument persönlich gezeigt
            statt kopiert wird.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Der rote Faden ist überall derselbe: nur das Nötigste weitergeben, mit Zweck und Datum
          wasserzeichnen und festhalten, wer die Kopie erhalten hat.
        </p>
      </section>

      <section class="card">
        <h2>Und im Vereinigten Königreich?</h2>
        <p>
          Die Verbraucherinformationen zu Ausweis-Sicherheit verteilen sich im Vereinigten Königreich auf
          drei Stellen, und anders als in den Niederlanden oder Deutschland veröffentlicht keine davon eine
          Schritt-für-Schritt-Anleitung zum Schwärzen einer Passkopie. Der Schwerpunkt liegt auf Prävention,
          Meldung und schützender Registrierung:
        </p>
        <ul>
          <li>
            <a href="https://ico.org.uk/for-the-public/identity-theft/" target="_blank" rel="noopener">Information Commissioner's Office (ICO) — Identity theft</a>:
            die Verbraucherseite der britischen Aufsichtsbehörde. Erklärt Warnzeichen, was bei einem
            Datenleck zu tun ist, und empfiehlt verlorene oder gestohlene Ausweise bei der ausstellenden
            Stelle zu melden.
          </li>
          <li>
            <a href="https://www.actionfraud.police.uk/a-z-of-fraud/identity-fraud-and-identity-theft" target="_blank" rel="noopener">Action Fraud — Identity fraud and identity theft</a>:
            die nationale Meldestelle für Betrug. Empfiehlt, persönliche Dokumente sicher aufzubewahren, vor
            dem Wegwerfen zu vernichten und verlorene Pässe bei HM Passport Office zu melden.
          </li>
          <li>
            <a href="https://www.cifas.org.uk/services/identity-protection" target="_blank" rel="noopener">Cifas — Identity protection</a>:
            der britische Betrugspräventionsdienst. Gegen eine geringe Gebühr lässt sich eine
            <em>Protective Registration</em> eintragen, sodass Kredit- oder Kontoanträge in Ihrem Namen
            zusätzlich geprüft werden.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Das Grundprinzip ist überall gleich: so wenig wie möglich teilen, mit so wenigen Personen wie
          möglich, so kurz wie möglich, und festhalten, wer eine Kopie erhalten hat. Schwärzen und
          Wasserzeichnen sind universelle Werkzeuge — selbst wenn nur wenige Länder sie so ausführlich
          beschreiben.
        </p>
      </section>

      <section class="card">
        <h2>Bevor Sie die Kopie verschicken</h2>
        <ul>
          <li>Öffnen Sie das heruntergeladene Bild und zoomen Sie hinein: Ist alles, was verborgen sein soll, vollständig abgedeckt – auch QR-Codes? Ist das Wasserzeichen lesbar?</li>
          <li>Versenden Sie nach Möglichkeit über einen Ende-zu-Ende-verschlüsselten Kanal. Vermeiden Sie normale E-Mails.</li>
          <li>Notieren Sie Empfänger und Datum. Taucht die Kopie später irgendwo auf, wissen Sie, wer sie hatte.</li>
          <li>In Deutschland dürfen Sie nach der PAuswG-Reform von 2017 eine teilgeschwärzte Kopie weitergeben — Forderungen nach einer ungeschwärzten Kopie sind oft unnötig und ein Warnsignal.</li>
          <li>Manche Stellen müssen bestimmte Angaben von Gesetzes wegen sehen — Banken etwa müssen Ihre Identität nach dem Geldwäschegesetz prüfen. Fragen Sie im Zweifel nach, welche Felder wirklich benötigt werden.</li>
          <li>Löschen Sie die Kopie nach dem Versand aus Ihrem Download-Ordner und lassen Sie sie nicht in Chats oder E-Mail-Entwürfen liegen.</li>
        </ul>
      </section>

      <footer>
        Ein kleines Open-Source-Experiment, das den Empfehlungen der
        <a href="https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl" target="_blank" rel="noopener">Verbraucherzentrale</a>
        und der niederländischen
        <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a> folgt.
        Es werden keine Daten gesammelt — aber glauben Sie uns nicht blind:
        <a href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">den Quellcode auf GitHub ansehen</a>.
      </footer>
"""
