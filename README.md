<p>
<a href="https://velaarturo.com/">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/hero-mobile-dark.svg">
    <source media="(max-width: 600px)" srcset="./assets/hero-mobile-light.svg">
    <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
    <img src="./assets/hero-light.svg" width="100%" alt="Arturo Vela — Desarrollo web y de producto. React, TypeScript, Cloudflare y SQL. Visita mi portafolio.">
  </picture>
</a>
</p>

Construyo **productos web y sistemas para operaciones reales**: desde entradas con trazabilidad blockchain hasta catálogos comerciales, herramientas internas y aplicaciones de uso diario.

Desde **Tarapoto, Perú · UTC−5**. Estudiante de Ingeniería de Sistemas en la **UNSM**. Disponible para roles full-stack, proyectos freelance y colaboración técnica.

[Portafolio](https://velaarturo.com/) · [CV](https://cv.velaarturo.com/) · [Artículos](https://blog.velaarturo.com/es/articulos) · [Contacto](mailto:dev@velaarturo.com)

[Productos destacados](#productos-destacados) · [Más productos](#más-productos) · [Stack](#stack-actual) · [Actividad](#actividad-en-github)

## Productos destacados

### 01 / Vela Entradas · Blockchain aplicada

<a href="https://bc.velaarturo.com/blockchain">
  <img src="./assets/screenshots/blockchain.jpg" width="100%" alt="Captura real de Vela Entradas: explorador blockchain con bloques recientes, enlaces entre bloques y raíz Merkle.">
</a>

Plataforma de entradas para asistentes y organizadores. Combina **QR temporales, canje único y transferencias** con un registro verificable de emisión, uso y revocación.

La blockchain privada enlaza bloques SHA-256 y pruebas Merkle. **OpenTimestamps permite verificar su existencia en Bitcoin** cuando el sello externo se confirma. Vela opera la cadena; no utiliza consenso descentralizado.

`React` `TypeScript` `Cloudflare Workers` `D1` `R2` `SHA-256` `OpenTimestamps`

[Abrir producto](https://bc.velaarturo.com/) · [Explorar blockchain](https://bc.velaarturo.com/blockchain) · [Ver proyecto](https://velaarturo.com/es/proyectos/bc)

### 02 / Agromaf · Catálogo y cotización

<a href="https://web.agromaf.pe/">
  <img src="./assets/screenshots/agromaf.jpg" width="100%" alt="Captura real de Agromaf: catálogo con fotografías de equipos, precios en soles, filtros y carrito de cotización.">
</a>

Web comercial para **Cia Agromaf y Cia Agromaf Perú**. Catálogo por empresa, marcas, fichas técnicas, comparación de productos y carrito de cotización que prepara la consulta por WhatsApp.

Administración de productos y contenido, permisos por empresa, fotografías en R2 y catálogos PDF. Una misma plataforma conecta la consulta pública con el trabajo del equipo.

`Astro` `TypeScript` `Supabase` `Cloudflare Workers` `R2`

[Visitar Agromaf](https://web.agromaf.pe/) · [Explorar catálogo](https://web.agromaf.pe/catalogo)

### 03 / Nieto Import · Operaciones y datos

<a href="https://nieto.velaarturo.com/">
  <img src="./assets/screenshots/nieto.jpg" width="100%" alt="Captura real de NIETO Hub: presentación pública de DATANIETO y Nieto Import, con sus vistas previas y enlaces de acceso.">
</a>

Herramientas internas para **Nieto Import y Agromaf**: etiquetas, documentación, firmas corporativas y formularios de gestión, con permisos y acceso web y móvil.

El ecosistema incluye **DATANIETO**, que convierte información comercial histórica en paneles consultables, y **NIETO Hub**, su escaparate público. Los sistemas operativos requieren autorización.

`Next.js` `React` `TypeScript` `Supabase` `Capacitor` `Cloudflare`

[Ver NIETO Hub](https://nieto.velaarturo.com/) · [Caso Nieto Import](https://velaarturo.com/es/proyectos/nieto-import) · [Caso DATANIETO](https://velaarturo.com/es/proyectos/db-nieto)

## Más productos

<details open>
<summary><strong>Second Brain</strong> · Conocimiento y publicación</summary>

Espacio privado para conocimiento, tareas, relaciones y archivos versionados. Publica contenido hacia mi portafolio, blog y CV.

`React` `TypeScript` `Mantine` `Workers` `D1` `R2` `Queues`

[Ver caso de estudio](https://velaarturo.com/es/proyectos/second-brain) · Acceso privado

</details>

<details>
<summary><strong>Vela Ventas</strong> · Operación comercial</summary>

Ventas, compras, inventario por sucursal, caja diaria y Kardex para comercios peruanos. Permisos por negocio y aislamiento de datos en el servidor.

`React` `TypeScript` `Chakra UI` `Hono` `Workers` `D1`

[Abrir producto](https://ventas.velaarturo.com/)

</details>

<details>
<summary><strong>Explora San Martín</strong> · Turismo con fuentes verificables</summary>

Mapa turístico, **164 lugares documentados** con fuentes y pasaporte personal. Combina fichas renderizadas en el servidor con flujos editoriales protegidos.

`React Router` `React` `TypeScript` `MapLibre` `Workers` `D1` `R2`

[Explorar la app](https://explora.velaarturo.com/) · [Ver caso de estudio](https://velaarturo.com/es/proyectos/explora-san-martin)

</details>

<details>
<summary><strong>Cafetero</strong> · Directorio y pasaporte de cafeterías</summary>

Cafeterías del Perú con mapas, fichas verificables y registro de visitas.

`React Router` `React` `TypeScript` `Chakra UI`

[Ver caso de estudio](https://velaarturo.com/es/proyectos/coffee)

</details>

<details>
<summary><strong>Cotiza</strong> · Cotizaciones y documentos</summary>

Cotizaciones y borradores de contratos con cálculos decimales, borradores recuperables y exportación PDF.

[Abrir herramienta](https://cotiza.velaarturo.com/) · [Cómo lo construí](https://blog.velaarturo.com/es/articulos/como-se-creo-cotiza)

</details>

<details>
<summary><strong>Más SaaS y herramientas de mi ecosistema</strong></summary>

Productos para finanzas, operaciones y fidelización. Algunas aplicaciones requieren cuenta o autorización.

<!-- Los enlaces envuelven cada SVG: GitHub no permite interacción dentro de las imágenes. -->
<p>
  <a href="https://finanzas.velaarturo.com/"><img src="./assets/link-finanzas.svg" width="248" height="120" alt="Finanzas — Cuentas, movimientos y metas."></a>
  <a href="https://ventas.velaarturo.com/"><img src="./assets/link-ventas.svg" width="248" height="120" alt="Ventas — Ventas, inventario y caja."></a>
  <a href="https://agua.velaarturo.com/"><img src="./assets/link-agua.svg" width="248" height="120" alt="AquaVigía — Plataforma de agua con acceso autorizado."></a>
  <a href="https://agro.velaarturo.com/"><img src="./assets/link-agro.svg" width="248" height="120" alt="Agro Vela — Tu campo, tus cuentas."></a>
  <a href="https://bc.velaarturo.com/"><img src="./assets/link-bc.svg" width="248" height="120" alt="Vela Entradas — Entradas digitales para eventos."></a>
  <a href="https://tarjetas.velaarturo.com/"><img src="./assets/link-tarjetas.svg" width="248" height="120" alt="Tarjetas — Fidelización para tu negocio."></a>
</p>

También construyo herramientas que procesan archivos en el navegador: [PDF](https://pdf.velaarturo.com/) y [Foto](https://foto.velaarturo.com/). Encuentra el resto en [mi catálogo de proyectos](https://velaarturo.com/es/proyectos).

</details>

## Stack actual

- **Interfaces:** React, TypeScript, Astro, Next.js, React Router, Chakra UI y Mantine.
- **APIs y datos:** Cloudflare Workers, Hono, SQL, D1 y Supabase.
- **Archivos y tareas en segundo plano:** R2, Queues y Worker Service Bindings.
- **Verificación:** Vitest, Playwright, comprobación de tipos y Git.

<p>
  <img src="https://img.shields.io/badge/React-0E1420?style=flat-square&amp;logo=react&amp;logoColor=91ADFF" alt="React">
  <img src="https://img.shields.io/badge/TypeScript-0E1420?style=flat-square&amp;logo=typescript&amp;logoColor=91ADFF" alt="TypeScript">
  <img src="https://img.shields.io/badge/Cloudflare-0E1420?style=flat-square&amp;logo=cloudflare&amp;logoColor=F18B72" alt="Cloudflare">
  <img src="https://img.shields.io/badge/Astro-0E1420?style=flat-square&amp;logo=astro&amp;logoColor=F18B72" alt="Astro">
  <img src="https://img.shields.io/badge/Supabase-0E1420?style=flat-square&amp;logo=supabase&amp;logoColor=78CEAF" alt="Supabase">
</p>

## Actividad en GitHub

Commits, pull requests, estrellas, lenguajes y rachas. Las tarjetas se generan diariamente en este repositorio; cada componente utiliza el período que indica.

<p>
  <a href="https://github.com/ArturoVela?tab=repositories">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./assets/github-stats-dark.svg">
      <img src="./assets/github-stats-light.svg" height="195" alt="Estadísticas de ArturoVela: commits del período indicado, estrellas, pull requests, incidencias y repositorios con contribuciones.">
    </picture>
  </a>
  <a href="https://github.com/ArturoVela?tab=repositories">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./assets/github-languages-dark.svg">
      <img src="./assets/github-languages-light.svg" height="195" alt="Lenguajes más usados en los repositorios públicos de ArturoVela.">
    </picture>
  </a>
</p>

<a href="https://github.com/ArturoVela?tab=overview">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/github-streak-dark.svg">
    <img src="./assets/github-streak-light.svg" width="495" alt="Contribuciones totales, racha actual y racha más larga de ArturoVela. Zona horaria: Lima.">
  </picture>
</a>

<details>
<summary><strong>Mi calendario de contribuciones, en modo Snake</strong></summary>

Una serpiente recorre el calendario de contribuciones del último año.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/github-snake-dark.svg">
  <img src="./assets/github-snake-light.svg" width="100%" alt="Animación Snake del calendario de contribuciones de ArturoVela, con acentos azul y coral.">
</picture>

</details>

<sub>Las estadísticas de código reflejan repositorios públicos; las rachas siguen mi calendario visible de GitHub. Los lenguajes no miden dominio técnico. Componentes: <a href="https://github.com/stats-organization/github-readme-stats-action">Readme Stats Action</a>, <a href="https://github.com/DenverCoder1/github-readme-streak-stats">Streak Stats</a> y <a href="https://github.com/Platane/snk">Snake</a>. <a href="https://github.com/ArturoVela/ArturoVela/actions/workflows/profile-cards.yml">Ver actualización</a>.</sub>

## Código público

- [Porta](https://github.com/ArturoVela/Porta) — portafolio con React, Vite, Chakra UI y Cloudflare Workers; contenido desde Second Brain.
- [ApiRest](https://github.com/ArturoVela/ApiRest) — API de gestión académica con Java 17 y Spring Boot.

**¿Tienes un producto o proceso por mejorar?** [Hablemos](https://velaarturo.com/es/contacto).
