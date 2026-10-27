# Polish (pl) translation of ../index.html. After editing, run: python3 i18n/build.py

CODE = 'pl'
NAV_LABEL = 'Język'
TITLE = 'Kopia dowodu osobistego – znak wodny i zasłanianie danych'
DESC = 'Dodaj znak wodny i zasłoń dane osobowe na kopii dowodu osobistego lub paszportu — w całości w przeglądarce. Nic nie jest wysyłane ani zapisywane.'
OG_TITLE = 'Bezpieczna kopia dowodu: znak wodny i zasłanianie danych'
OG_DESC = 'Zasłoń dane osobowe i dodaj znak wodny do kopii dowodu osobistego lub paszportu — w całości w przeglądarce. Bez wysyłania, bez śledzenia.'
TW_DESC = 'Zasłoń dane i dodaj znak wodny do kopii dowodu — w całości w przeglądarce. Bez wysyłania, bez śledzenia.'
OG_ALT = "Makieta paszportu z zasłoniętymi polami i ukośnym znakiem wodnym COPY, obok nagłówek 'Watermark your ID copy.'"
TW_ALT = 'Makieta paszportu z zasłoniętymi polami i ukośnym znakiem wodnym COPY.'
LD_NAME = 'Bezpieczna kopia dowodu osobistego lub paszportu – znak wodny i zasłanianie danych'
LD_DESC = 'Narzędzie działające wyłącznie w przeglądarce: zasłania dane osobowe i dodaje znak wodny z celem i datą do kopii dowodu osobistego lub paszportu. Bez wysyłania, bez śledzenia — dane nigdy nie opuszczają Twojego urządzenia.'

# (English source, translation) pairs for user-facing strings inside the <script>.
JS = [
    ("'HEIC files can\\'t be decoded safely in the browser without a third-party library. ' +\n            'Please convert the photo to JPEG or PNG first — see the instructions below.'",
     "'Plików HEIC nie da się bezpiecznie otworzyć w przeglądarce bez zewnętrznej biblioteki. ' +\n            'Najpierw przekonwertuj zdjęcie do JPEG lub PNG — instrukcja poniżej.'"),
    ("'That file is not an image. Try again.'",
     "'Ten plik nie jest obrazem. Spróbuj ponownie.'"),
    ("'loaded locally. Drop a new image to replace.'",
     "'wczytano lokalnie. Upuść nowy obraz, aby go zastąpić.'"),
    ("'Could not read that image. Try a different file.'",
     "'Nie udało się odczytać obrazu. Spróbuj innego pliku.'"),
    ('\'This browser does not support live camera access. Use "Choose an existing image" instead.\'',
     '\'Ta przeglądarka nie obsługuje dostępu do aparatu. Użyj opcji "Wybierz istniejący obraz".\''),
    ("'Camera access denied or unavailable: '",
     "'Brak dostępu do aparatu lub aparat niedostępny: '"),
    ("'(purpose not set)'",
     "'(nie podano celu)'"),
    ("'COPY  •  '",
     "'KOPIA  •  '"),
    ("'(date not set)'",
     "'(nie podano daty)'"),
]

# Everything from <h1> up to (not including) </main>.
BODY = """\
      <h1>Bezpieczna kopia dowodu osobistego lub paszportu</h1>
      <p class="hero-copy">
        Wgraj lub sfotografuj swój dowód osobisty albo paszport, zasłoń dane, których nie chcesz udostępniać,
        i dodaj ukośny znak wodny z celem i datą — wszystko dzieje się w Twojej przeglądarce.
      </p>
      <a class="back" href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">⟨/⟩ Zobacz kod źródłowy na GitHubie — otwarty kod, nic ukrytego</a>
    </header>

    <main>
      <section class="card tool">
        <h2>1. Dodaj dowód osobisty lub paszport</h2>
        <noscript><p class="status error">To narzędzie wymaga JavaScriptu, który jest wyłączony w Twojej przeglądarce. Działa w całości na Twoim urządzeniu — nic nie jest wysyłane.</p></noscript>
        <p class="hint">Wybierz plik z urządzenia albo zrób zdjęcie aparatem. W obu przypadkach obraz pozostaje w tej przeglądarce.</p>

        <label class="file-drop" id="drop">
          <input type="file" id="file" accept="image/*,.heic,.heif,image/heic,image/heif" />
          <span id="drop-label">Upuść obraz tutaj lub kliknij, aby wybrać plik (JPEG lub PNG)</span>
        </label>

        <details id="heic-help" class="heic-help">
          <summary>Masz zdjęcie <code>.HEIC</code> z iPhone'a? Jak je najpierw przekonwertować</summary>
          <p>
            HEIC to domyślny format zdjęć Apple. To narzędzie celowo nie zawiera dekodera HEIC, bo każdy
            zewnętrzny dekoder ładowany w trakcie działania byłby ryzykiem w łańcuchu dostaw dla strony, która
            obsługuje Twój dokument tożsamości. Oto jak przekonwertować HEIC do JPEG lokalnie:
          </p>
          <ul>
            <li>
              <strong>iPhone / iPad</strong> — najprościej: Ustawienia → Aparat → Formaty → wybierz
              <em>Najbardziej zgodne</em> i zrób zdjęcie ponownie; nowe zdjęcia będą w formacie JPEG. Dla
              istniejącego pliku HEIC otwórz zdjęcie w aplikacji Pliki, przytrzymaj je, wybierz Udostępnij →
              <em>Zachowaj w Plikach</em> z opcją „JPEG” albo użyj wbudowanej czynności <em>Konwertuj obraz</em>
              w aplikacji Skróty.
            </li>
            <li>
              <strong>macOS</strong> — kliknij dwukrotnie plik HEIC, aby otworzyć go w Podglądzie, a następnie
              Plik → Eksportuj… → ustaw Format na JPEG.
            </li>
            <li>
              <strong>Windows 10/11</strong> — zainstaluj bezpłatne „Rozszerzenia obrazów HEIF” Microsoftu ze
              Sklepu Microsoft, otwórz plik w aplikacji Zdjęcia i wybierz „Zapisz jako” → JPEG.
            </li>
            <li>
              <strong>Android</strong> — większość telefonów z Androidem zapisuje zdjęcia jako JPEG. Jeśli
              otrzymałeś plik HEIC, otwórz go w Zdjęciach Google → menu → „Zapisz jako” / „Eksportuj”.
            </li>
          </ul>
          <p style="margin-bottom: 0;">
            <strong>Unikaj konwerterów HEIC online</strong> — wysyłanie dowodu do przypadkowego serwisu
            konwertującego przekreśla cały sens tego narzędzia.
          </p>
        </details>

        <div class="upload-row">
          <button type="button" id="start-camera">📷 Zrób zdjęcie aparatem</button>
          <button type="button" id="pick-file">🖼️ Wybierz istniejący obraz</button>
        </div>

        <div class="camera-panel" id="camera-panel" hidden>
          <video id="video" playsinline muted></video>
          <div class="actions">
            <button type="button" id="shutter" class="primary">Zrób zdjęcie</button>
            <button type="button" id="flip-camera">Przełącz aparat</button>
            <button type="button" id="cancel-camera">Anuluj</button>
          </div>
          <p class="status" id="camera-status"></p>
        </div>

        <h2>2. Uzupełnij znak wodny</h2>
        <div class="form-grid">
          <label>
            Dla kogo i w jakim celu? (wymagane — ten tekst pojawi się w znaku wodnym)
            <input type="text" id="purpose" placeholder="np. umowa najmu z Nieruchomości Sp. z o.o." maxlength="140" autocomplete="off" required value="zameldowanie w domku letniskowym" />
          </label>
          <label>
            Data przekazania
            <input type="date" id="date" />
          </label>
        </div>

        <div id="editor" hidden>
          <h2>3. Zasłoń to, czego nie chcesz udostępniać</h2>
          <p class="hint">
            Przeciągnij po obrazie, aby narysować czarny prostokąt na każdym polu, którego wolisz nie udostępniać.
            Na polskim dowodzie osobistym zwykle warto zasłonić <strong>serię i numer dowodu</strong>,
            <strong>numer CAN</strong>, <strong>podpis</strong>, <strong>PESEL</strong> (jeśli odbiorca go nie
            potrzebuje) oraz <strong>strefę MRZ</strong> (trzy wiersze tekstu z &lt;&lt;&lt; na odwrocie). Zasłoń też każdy <strong>kod QR</strong> — może
            zawierać te same dane w formie do odczytu maszynowego.
          </p>
          <div class="canvas-wrap">
            <canvas id="canvas"></canvas>
          </div>
          <label class="check">
            <input type="checkbox" id="limit-res" checked />
            <span>Zmniejsz rozdzielczość (maks. 1200 pikseli) — nadal czytelna, ale trudniejsza do ponownego użycia lub podrobienia</span>
          </label>
          <div class="actions">
            <button type="button" id="undo">Cofnij ostatnie zasłonięcie</button>
            <button type="button" id="clear-blackouts" class="danger">Usuń wszystkie zasłonięcia</button>
            <button type="button" id="download" class="primary">⬇ Pobierz kopię ze znakiem wodnym (JPEG)</button>
          </div>
          <p class="hint" style="margin-top: 12px;">
            Wskazówka: znak wodny aktualizuje się na bieżąco podczas pisania. Opisz cel konkretnie (dla kogo i po
            co), aby było jasne, że kopia jest jednorazowa.
          </p>
        </div>
      </section>

      <section class="card privacy-card">
        <h2>🔒 Twój obraz nigdy nie opuszcza tej karty przeglądarki</h2>
        <ul>
          <li>Bez serwerów do wysyłania. Bez wywołań API. Bez analityki. Bez śledzenia.</li>
          <li>Wszystko działa w czystym JavaScripcie na Twoim urządzeniu.</li>
          <li>Nic nie jest zapisywane — ani w ciasteczkach, ani w localStorage, ani nigdzie indziej.</li>
          <li>Odśwież stronę i wszystko znika. Zamknij kartę i wszystko znika.</li>
          <li>Możesz nawet zapisać tę stronę (Ctrl+S / ⌘+S) i używać jej całkowicie offline.</li>
          <li>Pobrany plik JPEG to nowo wygenerowany obraz: ukryte metadane zdjęcia, takie jak lokalizacja GPS czy dane aparatu, nie są przenoszone.</li>
          <li>
            Ta strona celowo nie ładuje <em>żadnych</em> zewnętrznych skryptów — nawet do dekodowania HEIC —
            więc nie ma CDN, którego przejęcie pozwoliłoby zaatakować Twoją kopię strony.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          To ważne, bo zdjęcie dokumentu tożsamości to dane wrażliwe: zawiera imię i nazwisko, datę urodzenia,
          numer dokumentu, podpis, zdjęcie, a na polskim dowodzie także numer PESEL. Rozsyłanie go bez
          zabezpieczenia to ulubiony składnik kradzieży tożsamości.
        </p>
      </section>

      <section class="card">
        <h2>Co zaleca UODO w Polsce</h2>
        <p>
          <a href="https://uodo.gov.pl/pl/138/2476" target="_blank" rel="noopener">Urząd Ochrony Danych Osobowych (UODO)</a>
          podkreśla, że kopiowanie dowodu osobistego powinno być wyjątkiem. W skrócie:
        </p>
        <ul>
          <li>Preferowaną praktyką jest <strong>okazanie dokumentu osobiście</strong> zamiast przekazywania kopii.</li>
          <li>Jeśli kopia jest naprawdę nieunikniona, <strong>zasłoń każde pole</strong>, którego cel umowy ściśle nie wymaga.</li>
          <li>Oznacz kopię <strong>celem</strong> i <strong>datą</strong>, aby nie dało się jej łatwo wykorzystać ponownie.</li>
        </ul>
        <p style="margin-bottom: 0;">
          Dodatkowa ochrona: od listopada 2023 r. możesz <strong>zastrzec swój numer PESEL</strong> (np. w aplikacji
          mObywatel lub w urzędzie gminy). Banki i inne instytucje muszą wtedy sprawdzić zastrzeżenie, zanim
          udzielą kredytu na Twoje dane.
        </p>
      </section>

      <section class="card">
        <h2>Co zaleca rząd Holandii</h2>
        <p>
          To narzędzie powstało na podstawie oficjalnych zaleceń z Holandii, gdzie dwa źródła mówią to samo:
          <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs" target="_blank" rel="noopener">Rijksoverheid</a>
          (portal rządu centralnego) oraz
          <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>
          (holenderski organ ochrony danych). W skrócie:
        </p>
        <ul>
          <li>Spraw, by numer <strong>BSN</strong> (holenderski odpowiednik numeru PESEL) był nieczytelny na kopii — <em>również</em> w strefie odczytu maszynowego na dole dokumentu.</li>
          <li>W dokumentach wydanych od <strong>2 sierpnia 2021 r.</strong> numer BSN jest zapisany w <strong>kodzie QR</strong> (na odwrocie dowodu osobistego i na stronie danych paszportu) — jego też trzeba zasłonić.</li>
          <li>Możesz też zasłonić <strong>zdjęcie</strong> i <strong>podpis</strong>.</li>
          <li>Napisz na kopii, że to <strong>kopia</strong>, oraz dla kogo / do jakiego produktu lub celu jest przeznaczona.</li>
          <li>Napisz na kopii <strong>datę</strong>, w której ją przekazujesz.</li>
        </ul>
        <p>
          Autoriteit Persoonsgegevens wyraźnie zaznacza, że niektóre organizacje — na przykład operatorzy
          telekomunikacyjni i wypożyczalnie samochodów — w ogóle nie mogą przetwarzać numeru BSN ani zdjęcia i
          same muszą je zasłonić, jeśli robią kopię.
        </p>
        <p style="margin-bottom: 0;">
          Wolisz aplikację? Rząd Holandii udostępnia do tego własną bezpłatną aplikację <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/veilige-kopie-identiteitsbewijs" target="_blank" rel="noopener">KopieID</a>
          (iPhone i Android): zasłaniasz dane, których odbiorca nie potrzebuje, i dodajesz znak wodny z celem.
        </p>
      </section>

      <section class="card">
        <h2>Podobne zalecenia innych europejskich organów</h2>
        <p>
          Inne organy ochrony danych w UE dają równoważne rady: zasłoń pola, których odbiorca ściśle nie
          potrzebuje, i oznacz kopię celem i datą. To narzędzie sprawdzi się w każdym przypadku — wpisz po prostu
          w polu celu sformułowanie zalecane przez dany organ.
        </p>
        <ul>
          <li>
            <strong>Francja — <a href="https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite" target="_blank" rel="noopener">CNIL</a>.</strong>
            Dodaj widoczny znak wodny z odbiorcą, celem i datą — przykład samej CNIL to
            <em>„Document transmis uniquement pour l'ouverture d'un compte chez [organisme] – [date]”</em>.
            CNIL zaleca też ograniczenie rozdzielczości kopii, aby trudniej było ją ponownie wykorzystać.
          </li>
          <li>
            <strong>Niemcy — <a href="https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl" target="_blank" rel="noopener">Verbraucherzentrale Niedersachsen</a>.</strong>
            Na Personalausweis zasłoń numer dokumentu, numer dostępu/seryjny, kolor oczu, wzrost,
            obywatelstwo, podpis oraz miejsce i datę urodzenia, a następnie dodaj znak wodny z odbiorcą i celem.
            Od zmiany ustawy PAuswG w 2017 r. do weryfikacji tożsamości zwykle wystarczą imię i nazwisko, adres,
            data urodzenia i data ważności.
          </li>
          <li>
            <strong>Hiszpania — <a href="https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni" target="_blank" rel="noopener">AEPD</a>.</strong>
            Na awersie DNI usuń lub rozmaż numer nośnika, płeć, obywatelstwo, datę urodzenia i podpis; na
            rewersie adres, miejsce urodzenia i imiona rodziców. Wystarczą imię, nazwiska, numer dokumentu i
            zdjęcie — plus widoczna adnotacja z celem i datą.
          </li>
          <li>
            <strong>Belgia — <a href="https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/elektronische-identiteitskaart-eid/praktische-toepassingen" target="_blank" rel="noopener">Urząd Ochrony Danych (APD/GBA)</a>.</strong>
            Przekazuj tylko przekreśloną kopię, zasłaniając każde pole, które nie jest ściśle potrzebne —
            zwłaszcza krajowy numer rejestrowy, numer karty eID, daty ważności, płeć, obywatelstwo oraz miejsce i
            datę urodzenia — i napisz na kopii nazwę odbiorcy oraz konkretny dozwolony cel.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Wspólny mianownik wszystkich tych zaleceń jest ten sam: udostępniaj minimum, dodaj znak wodny z celem
          i datą, i zapisz, kto otrzymał kopię.
        </p>
      </section>

      <section class="card">
        <h2>Zanim wyślesz kopię</h2>
        <ul>
          <li>Otwórz pobrany obraz i powiększ go: czy wszystkie dane do ukrycia są w pełni zasłonięte, łącznie z kodami QR? Czy znak wodny jest czytelny?</li>
          <li>Najlepiej wyślij kopię kanałem szyfrowanym end-to-end. Jeśli możesz, unikaj zwykłego e-maila.</li>
          <li>Zanotuj odbiorcę i datę. Jeśli kopia kiedyś wypłynie gdzie indziej, będziesz wiedzieć, kto ją miał.</li>
          <li>Jeśli ktoś żąda pełnej, niezasłoniętej kopii dowodu bez wyraźnego powodu, zapytaj o cel i podstawę prawną. Często to sygnał ostrzegawczy.</li>
          <li>Niektóre instytucje są prawnie zobowiązane do sprawdzenia określonych danych — na przykład banki muszą zweryfikować Twoją tożsamość zgodnie z przepisami o przeciwdziałaniu praniu pieniędzy. W razie wątpliwości zapytaj odbiorcę, których danych naprawdę potrzebuje.</li>
          <li>Po wysłaniu usuń kopię z folderu Pobrane i nie zostawiaj jej w czatach ani w wersjach roboczych e-maili.</li>
        </ul>
      </section>

      <footer>
        Mały eksperyment open source, oparty na zaleceniach
        <a href="https://uodo.gov.pl/pl/138/2476" target="_blank" rel="noopener">UODO</a>,
        <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs" target="_blank" rel="noopener">Rijksoverheid</a>
        i
        <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>.
        Nie zbieramy żadnych danych — nie musisz wierzyć nam na słowo:
        <a href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">przeczytaj kod źródłowy na GitHubie</a>.
      </footer>
"""
