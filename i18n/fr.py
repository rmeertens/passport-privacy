# French (fr) translation of ../index.html. After editing, run: python3 i18n/build.py

CODE = 'fr'
NAV_LABEL = 'Langue'
TITLE = "Filigrane &amp; masquage pour copie de passeport ou carte d'identité"
DESC = "Ajoutez un filigrane et masquez les informations personnelles sur la copie de votre passeport ou de votre pièce d'identité — entièrement dans votre navigateur. Rien n'est envoyé, rien n'est stocké."
OG_TITLE = "Filigrane &amp; masquage pour copie de pièce d'identité"
OG_DESC = "Masquez les informations personnelles et apposez un filigrane sur une copie de votre pièce d'identité — entièrement dans votre navigateur. Sans envoi, sans traqueur."
TW_DESC = "Masquer et filigraner une copie de votre pièce d'identité — entièrement dans le navigateur. Sans envoi, sans traqueur."
OG_ALT = 'Maquette de passeport avec des champs masqués et un filigrane diagonal COPY, à côté du titre « Watermark your ID copy. ».'
TW_ALT = 'Maquette de passeport avec des champs masqués et un filigrane diagonal COPY.'
LD_NAME = "Filigrane & masquage pour copie de pièce d'identité"
LD_DESC = "Un outil qui tourne entièrement dans votre navigateur pour masquer les informations personnelles et apposer un filigrane (finalité + date) sur une copie de votre pièce d'identité. Aucun envoi, aucun traqueur — rien ne quitte votre appareil."

# (English source, translation) pairs for user-facing strings inside the <script>.
JS = [
    ("'HEIC files can\\'t be decoded safely in the browser without a third-party library. ' +",
     "'Les fichiers HEIC ne peuvent pas être décodés en toute sécurité dans le navigateur sans bibliothèque tierce. ' +"),
    ("'Please convert the photo to JPEG or PNG first — see the instructions below.';",
     "'Merci de convertir la photo en JPEG ou PNG d\\'abord — voir les instructions ci-dessous.';"),
    ("dropLabel.textContent = 'That file is not an image. Try again.';",
     "dropLabel.textContent = 'Ce fichier n\\'est pas une image. Veuillez réessayer.';"),
    ("dropLabel.textContent = (name ? name + ' — ' : '') + 'loaded locally. Drop a new image to replace.';",
     "dropLabel.textContent = (name ? name + ' — ' : '') + 'chargé localement. Déposez une autre image pour la remplacer.';"),
    ("dropLabel.textContent = 'Could not read that image. Try a different file.';",
     "dropLabel.textContent = 'Impossible de lire cette image. Essayez un autre fichier.';"),
    ('camStatus.textContent = \'This browser does not support live camera access. Use "Choose an existing image" instead.\';',
     "camStatus.textContent = 'Ce navigateur ne prend pas en charge l\\'accès direct à la caméra. Utilisez plutôt « Choisir une image existante ».';"),
    ("camStatus.textContent = 'Camera access denied or unavailable: ' + err.message;",
     "camStatus.textContent = 'Accès à la caméra refusé ou indisponible : ' + err.message;"),
    ("const purpose = (purposeEl.value || '').trim() || '(purpose not set)';",
     "const purpose = (purposeEl.value || '').trim() || '(finalité non renseignée)';"),
    ("const text = 'COPY  •  ' + purpose + '  •  ' + dateStr;",
     "const text = 'COPIE  •  ' + purpose + '  •  ' + dateStr;"),
    ("if (!iso) return '(date not set)';",
     "if (!iso) return '(date non renseignée)';"),
    ("return parts[2] + '-' + parts[1] + '-' + parts[0]; // DD-MM-YYYY, Dutch style",
     "return parts[2] + '/' + parts[1] + '/' + parts[0]; // JJ/MM/AAAA"),
]

# Everything from <h1> up to (not including) </main>.
BODY = """\
      <h1>Filigraner &amp; masquer une copie de pièce d'identité</h1>
      <p class="hero-copy">
        Importez ou photographiez le scan de votre passeport ou de votre carte d'identité, masquez les
        informations que vous ne souhaitez pas transmettre, puis apposez un filigrane en diagonale
        indiquant la finalité et la date — tout se passe dans votre navigateur.
      </p>
      <a class="back" href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">⟨/⟩ Voir le code source sur GitHub — open source, aucun code caché</a>
    </header>

    <main>
      <section class="card tool">
        <h2>1. Ajoutez votre passeport ou pièce d'identité</h2>
        <noscript><p class="status error">Cet outil a besoin de JavaScript, qui est désactivé dans votre navigateur. Il fonctionne entièrement sur votre appareil : rien n'est envoyé.</p></noscript>
        <p class="hint">Choisissez un fichier sur votre appareil ou prenez une photo avec votre caméra. Dans les deux cas, l'image reste entièrement dans ce navigateur.</p>

        <label class="file-drop" id="drop">
          <input type="file" id="file" accept="image/*,.heic,.heif,image/heic,image/heif" />
          <span id="drop-label">Déposez une image ici ou cliquez pour choisir un fichier (JPEG ou PNG)</span>
        </label>

        <details id="heic-help" class="heic-help">
          <summary>Une photo <code>.HEIC</code> prise avec un iPhone ? Voici comment la convertir</summary>
          <p>
            HEIC est le format photo par défaut d'Apple. Ce site n'embarque volontairement aucun décodeur
            HEIC, car tout décodeur tiers chargé à l'exécution constituerait un risque pour une page qui
            traite votre pièce d'identité. Voici comment convertir un HEIC en JPEG localement :
          </p>
          <ul>
            <li>
              <strong>iPhone / iPad</strong> — le plus simple : Réglages → Appareil photo → Formats →
              <em>Le plus compatible</em>, puis reprenez la photo ; les nouvelles photos seront en JPEG.
              Pour un HEIC existant, ouvrez la photo dans l'app Fichiers, appuyez longuement, choisissez
              Partager → <em>Enregistrer dans Fichiers</em> avec l'option JPEG, ou utilisez l'action
              intégrée <em>Convertir l'image</em> dans l'app Raccourcis.
            </li>
            <li>
              <strong>macOS</strong> — ouvrez le HEIC dans Aperçu, puis Fichier → Exporter… → format JPEG.
            </li>
            <li>
              <strong>Windows 10/11</strong> — installez l'extension gratuite « Extensions d'image HEIF »
              de Microsoft depuis le Microsoft Store, ouvrez le fichier dans Photos et choisissez
              « Enregistrer sous » → JPEG.
            </li>
            <li>
              <strong>Android</strong> — la plupart des Android enregistrent déjà en JPEG. Si vous avez
              reçu un HEIC, ouvrez-le dans Google Photos → menu → « Enregistrer sous » / « Exporter ».
            </li>
          </ul>
          <p style="margin-bottom: 0;">
            Merci d'<strong>éviter les convertisseurs HEIC en ligne</strong> — envoyer votre passeport à
            un service de conversion aléatoire annule tout l'intérêt de ce site.
          </p>
        </details>

        <div class="upload-row">
          <button type="button" id="start-camera">📷 Prendre une photo avec ma caméra</button>
          <button type="button" id="pick-file">🖼️ Choisir une image existante</button>
        </div>

        <div class="camera-panel" id="camera-panel" hidden>
          <video id="video" playsinline muted></video>
          <div class="actions">
            <button type="button" id="shutter" class="primary">Capturer</button>
            <button type="button" id="flip-camera">Changer de caméra</button>
            <button type="button" id="cancel-camera">Annuler</button>
          </div>
          <p class="status" id="camera-status"></p>
        </div>

        <h2>2. Renseignez le filigrane</h2>
        <div class="form-grid">
          <label>
            Pour qui et pour quoi ? (obligatoire — ce texte apparaît dans le filigrane)
            <input type="text" id="purpose" placeholder="ex. ouverture d'un compte chez Exemple SA" maxlength="140" autocomplete="off" required value="check-in location de vacances" />
          </label>
          <label>
            Date de transmission
            <input type="date" id="date" />
          </label>
        </div>

        <div id="editor" hidden>
          <h2>3. Masquez tout ce que vous ne voulez pas partager</h2>
          <p class="hint">
            Faites glisser la souris sur l'image pour tracer un rectangle noir sur un champ que vous ne
            voulez pas transmettre. Sur une carte nationale d'identité française, on masque généralement
            le <strong>numéro de document</strong>, la <strong>signature</strong>, et la <strong>MRZ</strong>
            (les lignes de &lt;&lt;&lt;). Masquez aussi tout <strong>code QR ou code 2D</strong> : il peut
            contenir les mêmes données sous forme lisible par machine.
          </p>
          <div class="canvas-wrap">
            <canvas id="canvas"></canvas>
          </div>
          <label class="check">
            <input type="checkbox" id="limit-res" checked />
            <span>Réduire la résolution (1200 pixels max.) — toujours lisible, mais plus difficile à réutiliser ou à falsifier</span>
          </label>
          <div class="actions">
            <button type="button" id="undo">Annuler le dernier masquage</button>
            <button type="button" id="clear-blackouts" class="danger">Effacer tous les masquages</button>
            <button type="button" id="download" class="primary">⬇ Télécharger la copie filigranée (JPEG)</button>
          </div>
          <p class="hint" style="margin-top: 12px;">
            Astuce : le filigrane se met à jour en direct. Formulez la finalité précisément (pour qui, pour
            quoi) afin que la copie soit visiblement à usage unique.
          </p>
        </div>
      </section>

      <section class="card privacy-card">
        <h2>🔒 Votre image ne quitte jamais cet onglet</h2>
        <ul>
          <li>Aucun serveur d'upload. Aucun appel d'API. Aucune analytique. Aucun traqueur.</li>
          <li>Tout s'exécute en JavaScript pur, sur votre appareil.</li>
          <li>Rien n'est enregistré — ni dans les cookies, ni dans le localStorage, nulle part.</li>
          <li>Rafraîchissez la page, tout est effacé. Fermez l'onglet, tout est effacé.</li>
          <li>Vous pouvez même enregistrer la page (Ctrl+S / ⌘+S) et l'utiliser totalement hors ligne.</li>
          <li>Le JPEG téléchargé est une image entièrement redessinée : les métadonnées cachées de la photo, comme la position GPS ou les infos de l'appareil, ne sont pas conservées.</li>
          <li>
            Cette page ne charge <em>aucun</em> script tiers à l'exécution — pas même pour décoder le
            HEIC — il n'y a donc aucun CDN qui pourrait être compromis pour attaquer votre copie de la page.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Cela compte, car la photo de votre pièce d'identité est une donnée sensible : elle contient vos
          noms et prénoms, votre date de naissance, le numéro du document, votre signature et votre photo
          — l'ingrédient idéal pour une usurpation d'identité.
        </p>
      </section>

      <section class="card">
        <h2>Ce que recommande la CNIL</h2>
        <p>
          En France, la
          <a href="https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite" target="_blank" rel="noopener">CNIL</a>
          (Commission nationale de l'informatique et des libertés) est très concrète sur la transmission
          d'une copie de pièce d'identité. En résumé :
        </p>
        <ul>
          <li>N'envoyez une copie que si c'est <strong>strictement nécessaire</strong> — et jamais par un canal non sécurisé.</li>
          <li>Apposez un <strong>filigrane visible</strong> précisant le destinataire, la finalité et la date. Exemple donné par la CNIL : <em>« Document transmis uniquement pour l'ouverture d'un compte chez [organisme] – [date] »</em>.</li>
          <li>Limitez la <strong>résolution</strong> et la qualité du fichier pour qu'il soit difficilement réutilisable ailleurs.</li>
          <li>Masquez ce qui n'est pas nécessaire à la vérification (numéro de document, MRZ, signature).</li>
        </ul>
        <p style="margin-bottom: 0;">
          La CNIL rappelle aussi qu'un commerçant, un hôtel ou un bailleur ne peut pas exiger une copie
          non filigranée : une demande d'original non annoté doit généralement vous alerter.
        </p>
      </section>

      <section class="card">
        <h2>Recommandations des autres autorités européennes</h2>
        <p>
          Plusieurs autorités européennes de protection des données publient des consignes aussi concrètes
          que celles de la CNIL : masquer les champs non indispensables et apposer un filigrane précisant
          la finalité et la date. Ce site fonctionne pour n'importe laquelle d'entre elles — il suffit de
          recopier la formulation recommandée dans le champ « Finalité ».
        </p>
        <ul>
          <li>
            <strong>Pays-Bas — <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>.</strong>
            Masquer le BSN (numéro national), la photo et la signature, y compris dans la MRZ. Indiquer
            sur la copie qu'il s'agit d'une copie, la finalité et la date. Sur les documents émis à
            partir du 2 août 2021, le BSN figure dans un code QR (au verso de la carte d'identité, sur la page de
            données du passeport) : masquez aussi ce code QR.
            Le gouvernement néerlandais propose aussi sa propre application gratuite pour cela : <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/veilige-kopie-identiteitsbewijs" target="_blank" rel="noopener">KopieID</a>
            (iPhone et Android).
          </li>
          <li>
            <strong>Allemagne — <a href="https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl" target="_blank" rel="noopener">Verbraucherzentrale Niedersachsen</a>.</strong>
            Sur un Personalausweis, masquer le numéro de document, le numéro d'accès/série, la couleur
            des yeux, la taille, la nationalité, la signature, le lieu et la date de naissance, puis
            apposer un filigrane avec destinataire et finalité. Depuis la réforme du PAuswG de 2017,
            seuls le nom, l'adresse, la date de naissance et la validité doivent rester lisibles.
          </li>
          <li>
            <strong>Espagne — <a href="https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni" target="_blank" rel="noopener">AEPD</a>.</strong>
            Au recto du DNI, masquer le numéro de support, le sexe, la nationalité, la date de naissance
            et la signature ; au verso, l'adresse, le lieu de naissance et les noms des parents. Seuls le
            nom, les prénoms, le numéro du document et la photo doivent subsister — avec une mention
            visible de la finalité et de la date.
          </li>
          <li>
            <strong>Belgique — <a href="https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/elektronische-identiteitskaart-eid/praktische-toepassingen" target="_blank" rel="noopener">Autorité de protection des données (APD)</a>.</strong>
            Ne transmettre qu'une copie <em>barrée</em>, en recouvrant tout champ non indispensable —
            notamment le numéro de registre national, le numéro de carte eID, les dates de validité,
            le sexe, la nationalité, le lieu et la date de naissance. Indiquer sur la copie le destinataire
            et l'usage autorisé.
          </li>
          <li>
            <strong>Pologne — <a href="https://uodo.gov.pl/pl/138/2476" target="_blank" rel="noopener">UODO</a>.</strong>
            Lorsqu'une copie du <em>dowód osobisty</em> est vraiment inévitable, masquer tout champ non
            strictement nécessaire à la finalité du contrat. La pratique préférée par l'UODO reste que
            le document soit présenté en personne plutôt que copié.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Le fil rouge est partout le même : partager le minimum, filigraner avec la finalité et la date,
          et noter à qui la copie a été remise.
        </p>
      </section>

      <section class="card">
        <h2>Et au Royaume-Uni ?</h2>
        <p>
          Au Royaume-Uni, les conseils grand public sur la sécurité des pièces d'identité sont répartis
          entre trois organismes, et — à la différence de la CNIL ou des autorités néerlandaise et
          allemande — aucun ne publie de procédure détaillée de masquage d'une copie de passeport.
          L'accent y est mis sur la prévention, le signalement et l'enregistrement protecteur :
        </p>
        <ul>
          <li>
            <a href="https://ico.org.uk/for-the-public/identity-theft/" target="_blank" rel="noopener">Information Commissioner's Office (ICO) — Identity theft</a> :
            la page consommateur du régulateur britannique. Elle explique les signaux d'alerte, que faire
            en cas de compromission de vos données, et conseille de signaler la perte ou le vol à
            l'organisme émetteur.
          </li>
          <li>
            <a href="https://www.actionfraud.police.uk/a-z-of-fraud/identity-fraud-and-identity-theft" target="_blank" rel="noopener">Action Fraud — Identity fraud and identity theft</a> :
            le centre national britannique de signalement des fraudes. Il recommande de conserver ses
            documents à l'abri, de détruire tout document nominatif avant de le jeter, et de signaler
            toute perte de passeport à HM Passport Office.
          </li>
          <li>
            <a href="https://www.cifas.org.uk/services/identity-protection" target="_blank" rel="noopener">Cifas — Identity protection</a> :
            le service britannique de prévention de la fraude. Pour une petite somme, une
            <em>Protective Registration</em> ajoute des contrôles supplémentaires sur tout crédit ou
            compte ouvert en votre nom.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Le principe sous-jacent est universel : partager le moins possible, avec le moins de personnes
          possible, pendant le moins de temps possible, et garder trace des envois. Masquer l'inutile et
          estampiller la copie fonctionne partout, même si seules quelques autorités le détaillent à ce
          point.
        </p>
      </section>

      <section class="card">
        <h2>Avant d'envoyer votre copie</h2>
        <ul>
          <li>Ouvrez l'image téléchargée et zoomez : tout ce que vous vouliez cacher est-il entièrement couvert, y compris les codes QR ou 2D ? Le filigrane est-il lisible ?</li>
          <li>Privilégiez un canal chiffré de bout en bout. Évitez l'e-mail classique si possible.</li>
          <li>Notez le destinataire et la date. Si la copie réapparaît ailleurs, vous saurez qui l'avait reçue.</li>
          <li>En France, un commerçant, un hôtel ou un bailleur n'a en général aucune raison d'exiger une copie non filigranée de votre pièce d'identité : une demande de copie « brute » doit vous alerter.</li>
          <li>Certains organismes sont légalement tenus de voir certaines informations — par exemple, les banques doivent vérifier votre identité au titre de la lutte contre le blanchiment. En cas de doute, demandez au destinataire quels champs lui sont réellement nécessaires.</li>
          <li>Après l'envoi, supprimez la copie de votre dossier Téléchargements et ne la laissez pas traîner dans des conversations ou des brouillons d'e-mail.</li>
        </ul>
      </section>

      <footer>
        Un petit projet open source qui suit les recommandations de la
        <a href="https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite" target="_blank" rel="noopener">CNIL</a>
        et de l'
        <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a> néerlandaise.
        Aucune donnée n'est collectée — ne nous croyez pas sur parole :
        <a href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">consultez le code source sur GitHub</a>.
      </footer>
"""
