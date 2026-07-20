/**
 * escalado.js
 * ============================================================
 * Sistema de escalado responsivo para diseños de base 1920px.
 *
 * Cómo funciona:
 *   - El diseño está construido sobre un canvas de 1920px de ancho.
 *   - Este script calcula un factor (scale = viewport / 1920) y aplica
 *     CSS zoom al contenedor principal, de modo que el diseño llena
 *     el 100% del viewport en cualquier resolución (móvil, tablet,
 *     laptop, 4K, ultrawide, etc.).
 *   - Un wrapper #clipper con overflow:hidden evita cualquier desborde
 *     lateral independientemente de cómo el browser calcule el layout box.
 *   - Los elementos position:fixed heredan automáticamente el zoom del padre
 *     en navegadores modernos, por lo que no requieren escalado manual.
 *
 * Estructura HTML requerida:
 * ─────────────────────────────────────────────────────────────
 *   <style>
 *     *, *::before, *::after { box-sizing: border-box; }
 *     html, body { margin: 0; padding: 0; }
 *     #clipper {
 *       width: 100%;
 *       max-width: 100vw;
 *       overflow: hidden;
 *     }
 *   </style>
 *
 *   <body>
 *     <div id="clipper">           <!-- recorta el desborde lateral -->
 *       <div id="container">       <!-- aquí se aplica el zoom      -->
 *         <!-- todo el contenido de la página -->
 *       </div>
 *     </div>
 *   </body>
 *
 * Uso:
 *   <script src="escalado.js"></script>
 * ─────────────────────────────────────────────────────────────
 */

(function () {
  'use strict';

  /** Ancho base del diseño en Figma (px) */
  var BASE_WIDTH = 1920;

  /**
   * Calcula el factor de escala y lo aplica al contenedor principal.
   * Se llama al cargar la página y en cada resize.
   */
  function scaleDesign() {
    var container = document.getElementById('container');
    var clipper   = document.getElementById('clipper');
    if (!container || !clipper) return;

    /**
     * window.innerWidth  = ancho total del viewport, scrollbar incluida.
     * Coincide con 100vw → el clipper (max-width: 100vw) y el contenido
     * escalado tienen exactamente el mismo ancho → sin espacio lateral.
     */
    var viewWidth = window.innerWidth;
    var scale     = viewWidth / BASE_WIDTH; // sin límite: escala tanto arriba como abajo

    /* ── Contenedor principal ─────────────────────────────── */
    container.style.width = BASE_WIDTH + 'px'; // fuerza el ancho base
    container.style.zoom  = scale;             // escala proporcional al viewport

    /* ── Altura del clipper y del body ───────────────────── */
    var scaledHeight = Math.ceil(container.offsetHeight * scale);
    clipper.style.height       = scaledHeight + 'px';
    document.body.style.height = scaledHeight + 'px';
  }

  /* ── Eventos ─────────────────────────────────────────────── */
  window.addEventListener('resize', scaleDesign);  // redimensionado de ventana
  window.addEventListener('load',   scaleDesign);  // después de cargar imágenes
  scaleDesign();                                    // ejecución inmediata
})();
