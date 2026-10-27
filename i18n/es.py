# Spanish (es) translation of ../index.html. After editing, run: python3 i18n/build.py

CODE = 'es'
NAV_LABEL = 'Idioma'
TITLE = 'Copia segura del DNI o pasaporte – marca de agua y tachado'
DESC = 'Añade una marca de agua y tacha los datos personales en una copia de tu DNI o pasaporte, todo en tu navegador. No se sube nada, no se guarda nada.'
OG_TITLE = 'Copia segura del DNI: marca de agua y tachado'
OG_DESC = 'Tacha datos personales y añade una marca de agua a una copia de tu DNI o pasaporte, todo en tu navegador. Sin subidas, sin rastreadores.'
TW_DESC = 'Tacha y pon una marca de agua a una copia de tu DNI, todo en tu navegador. Sin subidas, sin rastreadores.'
OG_ALT = "Un pasaporte simulado con campos tachados y una marca de agua diagonal COPY, junto al titular 'Watermark your ID copy.'"
TW_ALT = 'Un pasaporte simulado con campos tachados y una marca de agua diagonal COPY.'
LD_NAME = 'Copia segura del DNI o pasaporte – marca de agua y tachado'
LD_DESC = 'Una herramienta que funciona solo en el navegador: tacha datos personales y añade una marca de agua con finalidad y fecha a una copia de tu DNI o pasaporte. Sin subidas, sin rastreadores: tus datos nunca salen de tu dispositivo.'

# (English source, translation) pairs for user-facing strings inside the <script>.
JS = [
    ("'HEIC files can\\'t be decoded safely in the browser without a third-party library. ' +\n            'Please convert the photo to JPEG or PNG first — see the instructions below.'",
     "'Los archivos HEIC no se pueden abrir de forma segura en el navegador sin una biblioteca externa. ' +\n            'Convierte primero la foto a JPEG o PNG; consulta las instrucciones de abajo.'"),
    ("'That file is not an image. Try again.'",
     "'Ese archivo no es una imagen. Inténtalo de nuevo.'"),
    ("'loaded locally. Drop a new image to replace.'",
     "'cargada localmente. Arrastra otra imagen para sustituirla.'"),
    ("'Could not read that image. Try a different file.'",
     "'No se ha podido leer la imagen. Prueba con otro archivo.'"),
    ('\'This browser does not support live camera access. Use "Choose an existing image" instead.\'',
     '\'Este navegador no permite acceder a la cámara. Usa "Elegir una imagen existente".\''),
    ("'Camera access denied or unavailable: '",
     "'Acceso a la cámara denegado o no disponible: '"),
    ("'(purpose not set)'",
     "'(finalidad no indicada)'"),
    ("'COPY  •  '",
     "'COPIA  •  '"),
    ("'(date not set)'",
     "'(fecha no indicada)'"),
]

# Everything from <h1> up to (not including) </main>.
BODY = """\
      <h1>Copia segura de tu DNI o pasaporte</h1>
      <p class="hero-copy">
        Sube o fotografía tu DNI o pasaporte, tacha los datos personales que no quieras compartir y añade una
        marca de agua diagonal con la finalidad y la fecha, todo dentro de tu navegador.
      </p>
      <a class="back" href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">⟨/⟩ Ver el código fuente en GitHub: código abierto, nada oculto</a>
    </header>

    <main>
      <section class="card tool">
        <h2>1. Añade tu DNI o pasaporte</h2>
        <noscript><p class="status error">Esta herramienta necesita JavaScript, que está desactivado en tu navegador. Funciona por completo en tu dispositivo: no se sube nada.</p></noscript>
        <p class="hint">Elige un archivo de tu dispositivo o haz una foto con la cámara. En ambos casos la imagen no sale de este navegador.</p>

        <label class="file-drop" id="drop">
          <input type="file" id="file" accept="image/*,.heic,.heif,image/heic,image/heif" />
          <span id="drop-label">Arrastra una imagen aquí o haz clic para elegir un archivo (JPEG o PNG)</span>
        </label>

        <details id="heic-help" class="heic-help">
          <summary>¿Tienes una foto <code>.HEIC</code> de un iPhone? Cómo convertirla primero</summary>
          <p>
            HEIC es el formato de foto por defecto de Apple. Esta herramienta no incluye a propósito ningún
            decodificador HEIC, porque cualquier decodificador externo cargado en tiempo de ejecución sería un
            riesgo para la cadena de suministro en una página que maneja tu documento. Así puedes convertir HEIC a
            JPEG en tu propio dispositivo:
          </p>
          <ul>
            <li>
              <strong>iPhone / iPad</strong>: lo más sencillo es ir a Ajustes → Cámara → Formatos → elegir
              <em>Más compatible</em> y repetir la foto; las fotos nuevas se guardarán en JPEG. Para un HEIC que
              ya tengas, abre la foto en la app Archivos, mantenla pulsada y elige Compartir →
              <em>Guardar en Archivos</em> con la opción "JPEG", o usa la acción <em>Convertir imagen</em> de la
              app Atajos.
            </li>
            <li>
              <strong>macOS</strong>: haz doble clic en el HEIC para abrirlo en Vista Previa y elige Archivo →
              Exportar… → Formato: JPEG.
            </li>
            <li>
              <strong>Windows 10/11</strong>: instala las "Extensiones de imagen HEIF" gratuitas de Microsoft desde
              Microsoft Store, abre el archivo en Fotos y elige "Guardar como" → JPEG.
            </li>
            <li>
              <strong>Android</strong>: la mayoría de los Android ya guardan las fotos en JPEG. Si has recibido un
              HEIC, ábrelo en Google Fotos → menú → "Guardar como" / "Exportar".
            </li>
          </ul>
          <p style="margin-bottom: 0;">
            <strong>Evita los conversores HEIC en línea</strong> para esto: subir tu documento a un servicio de
            conversión cualquiera anula todo el sentido de esta herramienta.
          </p>
        </details>

        <div class="upload-row">
          <button type="button" id="start-camera">📷 Hacer una foto con la cámara</button>
          <button type="button" id="pick-file">🖼️ Elegir una imagen existente</button>
        </div>

        <div class="camera-panel" id="camera-panel" hidden>
          <video id="video" playsinline muted></video>
          <div class="actions">
            <button type="button" id="shutter" class="primary">Capturar</button>
            <button type="button" id="flip-camera">Cambiar de cámara</button>
            <button type="button" id="cancel-camera">Cancelar</button>
          </div>
          <p class="status" id="camera-status"></p>
        </div>

        <h2>2. Rellena la marca de agua</h2>
        <div class="form-grid">
          <label>
            ¿Para quién y para qué? (obligatorio: este texto aparece en la marca de agua)
            <input type="text" id="purpose" placeholder="p. ej. contrato de alquiler con Inmobiliaria S.L." maxlength="140" autocomplete="off" required value="registro en alojamiento vacacional" />
          </label>
          <label>
            Fecha de envío
            <input type="date" id="date" />
          </label>
        </div>

        <div id="editor" hidden>
          <h2>3. Tacha lo que no quieras compartir</h2>
          <p class="hint">
            Arrastra sobre la imagen para dibujar un rectángulo negro encima de cualquier dato que prefieras no
            compartir. En un DNI español, la AEPD recomienda tachar el <strong>número de soporte</strong>, el
            <strong>sexo</strong>, la <strong>nacionalidad</strong>, la <strong>fecha de nacimiento</strong> y la
            <strong>firma</strong>, y en el reverso la <strong>dirección</strong>, el <strong>lugar de nacimiento</strong>
            y los <strong>nombres de los padres</strong>. Tapa también cualquier <strong>código QR</strong>: puede
            contener los mismos datos en formato legible por máquina.
          </p>
          <div class="canvas-wrap">
            <canvas id="canvas"></canvas>
          </div>
          <label class="check">
            <input type="checkbox" id="limit-res" checked />
            <span>Reducir la resolución (máx. 1200 píxeles): sigue siendo legible, pero es más difícil de reutilizar o falsificar</span>
          </label>
          <div class="actions">
            <button type="button" id="undo">Deshacer el último tachado</button>
            <button type="button" id="clear-blackouts" class="danger">Borrar todos los tachados</button>
            <button type="button" id="download" class="primary">⬇ Descargar copia con marca de agua (JPEG)</button>
          </div>
          <p class="hint" style="margin-top: 12px;">
            Consejo: la marca de agua se actualiza mientras escribes. Indica una finalidad concreta (para quién y
            para qué) para que quede claro que la copia es de un solo uso.
          </p>
        </div>
      </section>

      <section class="card privacy-card">
        <h2>🔒 Tu imagen nunca sale de esta pestaña del navegador</h2>
        <ul>
          <li>Sin servidores de subida. Sin llamadas a APIs. Sin analítica. Sin rastreadores.</li>
          <li>Todo funciona con JavaScript puro en tu dispositivo.</li>
          <li>No se guarda nada: ni en cookies, ni en localStorage, ni en ningún sitio.</li>
          <li>Recarga la página y desaparece. Cierra la pestaña y desaparece.</li>
          <li>Incluso puedes guardar esta página (Ctrl+S / ⌘+S) y usarla totalmente sin conexión.</li>
          <li>El JPEG descargado es una imagen generada de nuevo: los metadatos ocultos de la foto, como la ubicación GPS o los datos de la cámara, no se conservan.</li>
          <li>
            Esta página no carga a propósito <em>ningún</em> script de terceros en tiempo de ejecución, ni
            siquiera para decodificar HEIC, así que no hay ningún CDN que se pueda comprometer para atacar tu copia
            de la página.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          Esto importa porque una foto de tu documento de identidad es un dato sensible: contiene tu nombre
          completo, fecha de nacimiento, número de documento, firma, foto y, en el DNI, el número de soporte.
          Hacerla circular sin protección es uno de los ingredientes favoritos de la suplantación de identidad.
        </p>
      </section>

      <section class="card">
        <h2>Lo que recomienda la AEPD en España</h2>
        <p>
          La <a href="https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni" target="_blank" rel="noopener">Agencia Española de Protección de Datos (AEPD)</a>
          explica qué hacer si te piden una copia del DNI. En resumen:
        </p>
        <ul>
          <li>En el anverso, borra o difumina el <strong>número de soporte</strong>, el <strong>sexo</strong>, la <strong>nacionalidad</strong>, la <strong>fecha de nacimiento</strong> y la <strong>firma</strong>.</li>
          <li>En el reverso, la <strong>dirección</strong>, el <strong>lugar de nacimiento</strong> y los <strong>nombres de los padres</strong>.</li>
          <li>Solo hace falta que queden visibles el <strong>nombre</strong>, los <strong>apellidos</strong>, el <strong>número de documento</strong> y la <strong>foto</strong>.</li>
          <li>Añade una nota visible con la <strong>finalidad</strong> de la copia y la <strong>fecha</strong>.</li>
        </ul>
        <p style="margin-bottom: 0;">
          Esta herramienta hace exactamente eso: tachas los campos que sobran y la marca de agua con la
          finalidad y la fecha se añade automáticamente.
        </p>
      </section>

      <section class="card">
        <h2>Lo que recomienda el gobierno neerlandés</h2>
        <p>
          Esta herramienta nació a partir del consejo oficial de los Países Bajos, donde dos fuentes coinciden:
          <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs" target="_blank" rel="noopener">Rijksoverheid</a>
          (el portal del gobierno central) y la
          <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>
          (la autoridad neerlandesa de protección de datos). En resumen:
        </p>
        <ul>
          <li>Haz ilegible el <strong>BSN</strong> (el número de identificación de los ciudadanos neerlandeses) en la copia, <em>también</em> en los dígitos legibles por máquina de la parte inferior del documento.</li>
          <li>En los documentos emitidos desde el <strong>2 de agosto de 2021</strong>, el BSN está en un <strong>código QR</strong> (en el reverso del documento de identidad y en la página de datos del pasaporte): tápalo también.</li>
          <li>También puedes tachar la <strong>foto</strong> y la <strong>firma</strong>.</li>
          <li>Escribe en la copia que es una <strong>copia</strong>, y para quién o para qué producto o finalidad está destinada.</li>
          <li>Escribe en la copia la <strong>fecha</strong> en que la entregas.</li>
        </ul>
        <p>
          La Autoriteit Persoonsgegevens deja claro que algunas organizaciones, por ejemplo operadoras de
          telecomunicaciones y empresas de alquiler de coches, ni siquiera pueden tratar el BSN ni la foto, y
          deben taparlos ellas mismas si hacen una copia.
        </p>
        <p style="margin-bottom: 0;">
          ¿Prefieres una app? El gobierno neerlandés tiene su propia app gratuita para esto, <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/veilige-kopie-identiteitsbewijs" target="_blank" rel="noopener">KopieID</a>
          (iPhone y Android): tachas los datos que el destinatario no necesita y añades una marca de agua con la
          finalidad.
        </p>
      </section>

      <section class="card">
        <h2>Consejos similares de otros reguladores europeos</h2>
        <p>
          Otras autoridades de protección de datos de la UE dan consejos equivalentes: tacha los campos que el
          destinatario no necesita estrictamente y marca la copia con la finalidad y la fecha. Esta herramienta
          sirve para todos los casos: solo tienes que escribir en el campo de finalidad el texto que recomiende
          cada regulador.
        </p>
        <ul>
          <li>
            <strong>Francia — <a href="https://www.cnil.fr/fr/cnil-direct/question/ma-banque-peut-elle-faire-une-copie-de-ma-piece-didentite" target="_blank" rel="noopener">CNIL</a>.</strong>
            Añade una marca de agua visible con el destinatario, la finalidad y la fecha; el ejemplo de la propia
            CNIL es <em>"Document transmis uniquement pour l'ouverture d'un compte chez [organisme] – [date]"</em>.
            La CNIL también recomienda limitar la resolución de la copia para que sea más difícil reutilizarla.
          </li>
          <li>
            <strong>Alemania — <a href="https://www.verbraucherzentrale-niedersachsen.de/themen/internet-telefon/datenschutz/ausweiskopien-wasserzeichen-so-schuetzen-sie-sich-vor-identitaetsdiebstahl" target="_blank" rel="noopener">Verbraucherzentrale Niedersachsen</a>.</strong>
            En un Personalausweis, tacha el número de documento, el número de acceso/serie, el color de ojos, la
            estatura, la nacionalidad, la firma y el lugar/fecha de nacimiento, y añade una marca de agua con el
            destinatario y la finalidad. Desde la reforma de la PAuswG de 2017, normalmente solo deben quedar
            visibles el nombre, la dirección, la fecha de nacimiento y la validez.
          </li>
          <li>
            <strong>Bélgica — <a href="https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/elektronische-identiteitskaart-eid/praktische-toepassingen" target="_blank" rel="noopener">Autoridad de Protección de Datos (APD/GBA)</a>.</strong>
            Entrega solo una copia tachada, ocultando cualquier campo que no sea estrictamente necesario
            —sobre todo el número de registro nacional, el número de la tarjeta eID, las fechas de validez, el
            sexo, la nacionalidad y el lugar/fecha de nacimiento— y escribe en la copia el nombre del destinatario
            y el uso concreto autorizado.
          </li>
          <li>
            <strong>Polonia — <a href="https://uodo.gov.pl/pl/138/2476" target="_blank" rel="noopener">UODO</a>.</strong>
            Si una copia del <em>dowód osobisty</em> es realmente inevitable, oculta todos los campos que la
            finalidad del contrato no exija estrictamente. La práctica preferida por la UODO es mostrar el
            documento en persona en lugar de copiarlo.
          </li>
        </ul>
        <p style="margin-bottom: 0;">
          El hilo común de todos estos consejos es el mismo: comparte lo mínimo, pon una marca de agua con la
          finalidad y la fecha, y apunta quién ha recibido la copia.
        </p>
      </section>

      <section class="card">
        <h2>Antes de enviar tu copia</h2>
        <ul>
          <li>Abre la imagen descargada y amplíala: ¿está bien tapado todo lo que querías ocultar, incluido cualquier código QR? ¿Se lee la marca de agua?</li>
          <li>Envíala preferiblemente por un canal con cifrado de extremo a extremo. Evita el correo electrónico normal si puedes.</li>
          <li>Apunta el destinatario y la fecha. Si la copia aparece alguna vez en otro sitio, sabrás quién la tenía.</li>
          <li>Si te piden una copia sin tachar del DNI sin una razón clara, pregunta para qué la necesitan y en qué base legal se apoyan. A menudo es una señal de alarma.</li>
          <li>Algunas organizaciones están obligadas por ley a ver ciertos datos: por ejemplo, los bancos deben verificar tu identidad por la normativa contra el blanqueo de capitales, y los alojamientos turísticos deben registrar los datos de tu documento. Si tienes dudas, pregunta al destinatario qué datos necesita realmente.</li>
          <li>Después de enviarla, borra la copia de tu carpeta de descargas y no la dejes olvidada en chats o borradores de correo.</li>
        </ul>
      </section>

      <footer>
        Un pequeño experimento de código abierto que sigue los consejos de la
        <a href="https://www.aepd.es/preguntas-frecuentes/1-tus-derechos/3-identificacion-con-dni/FAQ-0116-que-puedo-hacer-si-me-solicitan-una-copia-del-dni" target="_blank" rel="noopener">AEPD</a>,
        <a href="https://www.rijksoverheid.nl/onderwerpen/identiteitsfraude/vraag-en-antwoord/fraude-voorkomen-met-kopie-id-bewijs" target="_blank" rel="noopener">Rijksoverheid</a>
        y la
        <a href="https://www.autoriteitpersoonsgegevens.nl/nl/onderwerpen/identificatie/identiteitsbewijs" target="_blank" rel="noopener">Autoriteit Persoonsgegevens</a>.
        No se recoge ningún dato; no hace falta que nos creas:
        <a href="https://github.com/rmeertens/passport-privacy" target="_blank" rel="noopener">lee el código fuente en GitHub</a>.
      </footer>
"""
