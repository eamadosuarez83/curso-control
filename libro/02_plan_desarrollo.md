# Plan de Desarrollo

> Cómo se construye el curso, en qué orden, y dónde está cada cosa.

---

## Modo de trabajo

- El curso se desarrolla **secuencialmente, un módulo a la vez.**
- Cada módulo se entrega como un **archivo Markdown autónomo** que puede leerse,
  editarse y exportarse a PDF de forma independiente.
- El **Módulo 1 (versión conceptual)** define el estándar de formato y tono para
  todos los módulos restantes. Una versión técnica anterior del Módulo 1 fue
  descartada por ser demasiado procedimental; la reescritura conceptual es el
  artefacto de referencia definitivo.

## Estándar de cada módulo

Definido en detalle en [la filosofía de estudio](00_filosofia.md). En resumen,
cada módulo contiene:

1. Sección 0 — "La gran idea"
2. Teoría con LaTeX (conceptos como personajes antes que ecuaciones)
3. Ejemplos resueltos
4. Bloque de código Python
5. Bloque de código Octave
6. Series de ejercicios A–E con clave y preguntas de visión 👁
7. Recuadro de "lección transferible" por sección
8. Síntesis mapeando arquetipos a comportamientos

## Convención de nombres

```
modulo_NN_nombre_descriptivo.md
```

Ejemplos:
- `modulo_00_preliminares_matematicos.md`
- `modulo_01_modelado_sistemas_fisicos_conceptual.md`

---

## Registro de progreso

### ✅ Completados

| Módulo | Archivo | Contenido |
|--------|---------|-----------|
| **0** | `modulo_00_preliminares_matematicos.md` | Números complejos, Laplace, fracciones parciales, Fourier, EDOs, álgebra matricial, herramientas. Teoría con LaTeX, ejemplos resueltos, código Python/Octave, series A–E con clave. |
| **1** | `modulo_01_modelado_sistemas_fisicos_conceptual.md` | Reescritura conceptual del modelado de sistemas físicos. Estándar canónico de formato. Incluye la gran idea, sistemas mecánicos/eléctricos/hidráulicos/térmicos, analogías como corazón del módulo, linealización, y ejercicios con preguntas de visión 👁. |
| **2** | `modulo_02_funcion_transferencia_diagramas_bloques.md` | Función de transferencia (definición, polos/ceros/ganancia estática), álgebra y reducción de diagramas de bloques, diagramas de flujo de señal y fórmula de Mason. Ejemplo hilo conductor: control de posición con realimentación de velocidad (tacómetro) sobre el sistema rotacional del Módulo 1, conectando explícitamente con $\zeta$ y la forma canónica de segundo orden. |

### ⬜ Pendientes

| Módulo | Título | Prioridad |
|--------|--------|-----------|
| 3 | Respuesta Temporal de Sistemas | Siguiente |
| 4 | Error en Estado Estacionario | — |
| 5 | Estabilidad de Sistemas | — |
| 6 | Lugar Geométrico de las Raíces | — |
| 7 | Análisis en Frecuencia | — |
| 8 | Diseño de Controladores Clásicos | — |
| 9 | Representación en Variables de Estado | — |
| 10 | Introducción al Control Discreto | — |

---

## Hilos conductores entre módulos

Ideas plantadas en un módulo que se cobran en otro posterior. Mantenerlas
consistentes es parte del diseño del curso:

- **Forma canónica de segundo orden** `1/(Ms²+Bs+K)` (Mód. 1) → reaparece en
  respuesta temporal (Mód. 3), estabilidad (Mód. 5) y diseño (Mód. 8).
- **Polo en el origen / sistemas tipo 1** (Mód. 1, sistema rotacional sin
  resorte) → error en estado estacionario (Mód. 4).
- **Integradores con Amp-Op** (Mód. 1) → construcción de controladores PID
  (Mód. 8).
- **Arquetipos primer/segundo orden** (Mód. 1) → lenguaje común de todo el curso.
- **Analogías entre dominios** (Mód. 1) → base conceptual para aplicar la teoría
  fuera de la ingeniería de control.
- **Sistema rotacional con realimentación de velocidad (tacómetro)** (Mód. 2,
  ejemplo de reducción de bloques) → cierra el hilo del "polo en el origen"
  de Mód. 1 y anticipa el diseño con dos perillas independientes (velocidad de
  respuesta vs. amortiguamiento) que se formaliza en Mód. 8.
- **$G(s)H(s)$, la función de transferencia de lazo abierto** (Mód. 2) → objeto
  central de estabilidad (Mód. 5), root locus (Mód. 6) y error en estado
  estacionario vía $K_p,K_v,K_a$ (Mód. 4).

---

## Estilo de diagramas (adoptado 2026-09-21, pendiente de aplicar)

**Decisión:** dejar de usar diagramas ASCII en el Markdown (los del Módulo 1
§1.1 y sobre todo los de bloques del Módulo 2 quedaron feos/difíciles de leer
— ver `2.4` en la versión actual). En su lugar, adoptar el estilo del repo
hermano del mismo autor, **[apuntes_control](https://github.com/eamadosuarez83/apuntes_control)**
(curso de Control Digital, mismo enfoque de Markdown → Pandoc → PDF).

**Regla de oro de ese repo, y la que se adopta aquí:** ninguna figura suelta.
Todo diagrama tiene un script Python fuente, versionado, que lo regenera.

### Herramientas, una por tipo de figura

| Tipo de figura | Herramienta | Por qué |
|---|---|---|
| Diagramas de bloques (cajas, sumadores, flechas, puntos de toma) | **schemdraw**, submódulo `dsp` | Trae sumador con cruz y signos ±, nodos de derivación, posicionamiento explícito — justo lo que pide un diagrama de bloques. En `apuntes_control` lo evaluaron contra Graphviz y TikZ y ganó schemdraw para este caso específico (ver `notas/NOTAS-DESARROLLO.md` de ese repo, sección "Herramientas para los diagramas de bloques"). |
| Circuitos eléctricos | **schemdraw**, módulo `elements` (no `dsp`) | Mismo motor, biblioteca de componentes (resistencias, capacitores, fuentes, etc.) en vez de bloques de señal. |
| Gráficas cuantitativas: mapa de polos/ceros en el plano $s$, Bode, lugar de raíces | **matplotlib**, estilo minimalista fijo | Cuadrícula punteada tenue (`ls=':', lw=0.5, color='0.8'`), bordes superior/derecho ocultos (`ax.spines[...].set_visible(False)`), marcadores negros (`x` para polos), fondo transparente al guardar, título con LaTeX. Ver `apoyo/figuras/planos_s.py` de `apuntes_control` como plantilla exacta. |
| Diagramas de flujo de señal (SFG, nodos y ramas — Mód. 2 §2.5-2.6) | **Graphviz** (`.dot`), a evaluar mañana | `apuntes_control` usa schemdraw para bloques pero mantiene `.dot` como alternativa documentada para el mismo tipo de diagrama; un SFG es literalmente un grafo dirigido de nodos y ganancias, así que Graphviz podría ajustar mejor aquí que forzarlo con `dsp`. Decisión pendiente — probar ambos con el ejemplo de Mason ya escrito (dos trayectorias, lazos que no se tocan) antes de elegir. |

### Publicación dual: SVG versionado + PDF regenerado

Cada script de figura genera **dos salidas**: `.svg` (se versiona en git, para
leer el Markdown en GitHub o cualquier visor) y `.pdf` (vectorial, **no** se
versiona — se regenera en cada build, porque XeLaTeX/LuaLaTeX no incrustan
SVG). El build sustituye las rutas `.svg`→`.pdf` al vuelo antes de compilar
con pandoc. Ese es exactamente el mecanismo de `apoyo/build.sh` en
`apuntes_control`; `export_pdf.sh` de este proyecto hay que extenderlo igual.

### Pendiente para la próxima sesión (retroactivo, según lo pedido)

1. Crear `recursos/figuras/` (la carpeta `recursos/` ya existe y ya está
   declarada en el README para "imágenes, diagramas, material extra";
   solo falta poblarla) con un script por categoría, mismo criterio que
   `apuntes_control`: `bloques_schemdraw.py`, `planos_s.py`, y el que
   corresponda para las SFG.
2. Migrar el diagrama ASCII entrada→sistema→salida del **Módulo 1 §1.1**.
3. Migrar **todos** los diagramas de bloques del **Módulo 2**: los tres
   básicos de §2.3 (serie, paralelo, realimentación con signos), y el
   ejemplo de dos lazos anidados con tacómetro de §2.4 (el que peor quedó
   en ASCII).
4. Migrar el mapa de polos/ceros en el plano $s$ del **Módulo 2 §2.2** (hoy
   es un bloque de texto centrado imitando un eje) a `matplotlib`, siguiendo
   la plantilla de `planos_s.py`.
5. Resolver el SFG de §2.5-2.6 (schemdraw vs. Graphviz, ver tabla arriba) y
   migrarlo.
6. Actualizar `export_pdf.sh` para correr los scripts de `recursos/figuras/`
   y hacer la sustitución `.svg`→`.pdf` antes de invocar pandoc (hoy no lo
   hace porque no había figuras generadas por script).
7. Documentar en el `README.md` las dependencias nuevas:
   `pip install schemdraw matplotlib` (matplotlib ya estaba pedido; falta
   `schemdraw`) y, si se termina usando para las SFG, `graphviz` a nivel de
   sistema (`pacman -S graphviz` / `apt install graphviz`) para el binario
   `dot`.
8. Las imágenes se referencian en el Markdown con sintaxis estándar
   `![texto alternativo](../recursos/figuras/nombre.svg)` — el texto
   alternativo hace de pie de figura, sin mecanismo aparte (así lo hace
   `apuntes_control`, y no hay razón para inventar algo distinto).

---

## Compilar el libro completo a PDF

```bash
./export_pdf.sh
```

Exporta cada módulo por separado y el libro completo concatenado
(`libro/00_filosofia.md` → índice → módulos en orden → bibliografía) a
`pdf/curso_control_completo.pdf`. Ver [README.md](../README.md#exportar-a-pdf)
para requisitos (Pandoc + LuaLaTeX + fuentes DejaVu/Noto) y el detalle del
comando de Pandoc subyacente.
