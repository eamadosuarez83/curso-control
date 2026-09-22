# Curso de Control Analógico

> Un curso completo de sistemas de control analógico en español, escrito para
> **entender** — no solo para calcular.

[![Licencia](https://img.shields.io/badge/licencia-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow.svg)]()
[![Módulos](https://img.shields.io/badge/módulos-4%2F11-orange.svg)]()

---

## ¿Qué es esto?

Un curso de **control analógico** desarrollado como recurso personal de estudio y
referencia, basado en los textos clásicos de **Kuo** y **Ogata**. Cubre desde los
fundamentos matemáticos hasta el diseño de controladores clásicos y la
representación en espacio de estado.

Lo que distingue a este curso de un libro de texto convencional es su **filosofía
de estudio**: cada tema se explica primero por *qué existe*, *qué problema
resuelve* y *dónde más aparece la misma idea*, antes de tocar una sola ecuación.
El objetivo no es aprender a resolver ejercicios, sino aprender a **ver el mundo
como sistemas** y usar la teoría de control como una herramienta general de
pensamiento — aplicable incluso a problemas que nunca fueron "de control".

Lee la [**Filosofía de Estudio**](libro/00_filosofia.md) para entender el enfoque
completo.

---

## Cómo está organizado

```
curso-control/
├── README.md                  ← este archivo
├── libro/                     ← documentos maestros del curso
│   ├── 00_filosofia.md        ← filosofía y método de estudio
│   ├── 01_indice_general.md   ← temario completo (11 módulos)
│   ├── 02_plan_desarrollo.md  ← plan de trabajo y progreso
│   └── 03_bibliografia.md     ← referencias y recursos
├── modulos/                   ← los módulos del curso (contenido)
│   ├── modulo_00_preliminares_matematicos.md
│   ├── modulo_01_modelado_sistemas_fisicos_conceptual.md
│   ├── modulo_02_funcion_transferencia_diagramas_bloques.md
│   └── modulo_03_respuesta_temporal_sistemas.md
├── codigo/                    ← código de las prácticas
│   ├── python/
│   └── octave/
└── recursos/
    └── figuras/                ← diagramas del curso: scripts + .svg (el .pdf no se versiona)
        ├── bloques_schemdraw.py    ← diagramas de bloques y circuitos (schemdraw)
        ├── planos_s.py             ← mapas de polos/ceros, Bode, root locus (matplotlib)
        └── sfg_*.dot               ← diagramas de flujo de señal (Graphviz)
```

---

## Empezar a estudiar

1. Lee la [filosofía de estudio](libro/00_filosofia.md) — es corta y cambia cómo lees todo lo demás.
2. Revisa el [índice general](libro/01_indice_general.md) para ver el mapa completo.
3. Empieza por el [Módulo 0 — Preliminares Matemáticos](modulos/modulo_00_preliminares_matematicos.md).

Cada módulo es un archivo Markdown autónomo, editable, con matemáticas en LaTeX y
prácticas en **Python** y **Octave**.

---

## Herramientas

**Python:**
```bash
pip install numpy scipy matplotlib sympy control jupyter
```

**Octave:**
```octave
pkg install -forge control
pkg install -forge signal
pkg load control
```

---

## Diagramas

Ninguna figura suelta: todo diagrama del curso tiene un script fuente
versionado en `recursos/figuras/`, siguiendo el mismo estilo del repo hermano
[apuntes_control](https://github.com/eamadosuarez83/apuntes_control) (mismo autor).

| Tipo de figura | Herramienta |
|---|---|
| Diagramas de bloques (cajas, sumadores, puntos de toma) | [`schemdraw`](https://schemdraw.readthedocs.io/), submódulo `dsp` |
| Circuitos eléctricos | `schemdraw`, módulo `elements` |
| Mapas de polos/ceros, Bode, root locus | `matplotlib`, estilo minimalista fijo |
| Diagramas de flujo de señal (nodos y ramas) | [Graphviz](https://graphviz.org/) (`.dot`) |

Cada script/`.dot` genera **`.svg`** (versionado en git, para leer el Markdown
en GitHub) y **`.pdf`** (vectorial, no versionado, se regenera al compilar —
LuaLaTeX no incrusta SVG). `export_pdf.sh` corre todo esto automáticamente.

Instalación (entorno virtual, porque el Python del sistema suele estar
protegido por PEP 668):

```bash
python3 -m venv .venv
.venv/bin/pip install schemdraw matplotlib

# Graphviz (paquete de sistema, no de pip)
sudo pacman -S graphviz          # Arch/Manjaro
sudo apt install graphviz        # Debian/Ubuntu
```

`export_pdf.sh` usa `.venv/bin/python` automáticamente si existe esa carpeta;
si no, cae de vuelta a `python3` del sistema.

---

## Exportar a PDF

Todo el material está en Markdown con LaTeX, pensado para exportarse a PDF.

### Requisitos

- [Pandoc](https://pandoc.org/) 2.18+
- TeX Live con **LuaLaTeX** (no XeLaTeX: las letras griegas dentro de bloques
  de código y los emoji 👁/✅/⬜ solo compilan limpio con LuaLaTeX + fallback
  automático de fuente)
- Fuentes **DejaVu** (Serif y Sans Mono) y **Noto Color Emoji**
- Graphviz (`dot`) y un entorno Python con `schemdraw`/`matplotlib` para
  regenerar las figuras — ver [Diagramas](#diagramas) arriba

En Arch/Manjaro:

```bash
sudo pacman -S pandoc texlive-xetex texlive-core noto-fonts-emoji ttf-dejavu
```

En Debian/Ubuntu:

```bash
sudo apt install pandoc texlive-luatex texlive-latex-extra \
  fonts-dejavu fonts-noto-color-emoji
```

### Comando

Con todo instalado, un solo comando exporta cada módulo y el libro completo:

```bash
./export_pdf.sh              # todos los módulos + el libro completo, a pdf/
./export_pdf.sh modulo_02    # solo el módulo indicado (por nombre de archivo)
```

Los PDFs se generan en `pdf/` (ignorada por git; no se versiona el binario,
solo el Markdown fuente ni las figuras generadas). El script, en esencia: (1)
regenera todas las figuras de `recursos/figuras/`, (2) por cada archivo hace
una copia temporal sustituyendo las rutas de imagen `.svg`→`.pdf` (LuaLaTeX no
incrusta SVG), y (3) compila esa copia con:

```bash
pandoc modulos/.build-modulo_00_preliminares_matematicos.md \
  -o pdf/modulo_00.pdf \
  --pdf-engine=lualatex \
  --resource-path=modulos \
  -V geometry:margin=2.5cm \
  -V mainfont="DejaVu Serif" \
  -V monofont="DejaVu Sans Mono" \
  -V mainfontfallback="Noto Color Emoji:mode=harf" \
  -V monofontfallback="Noto Color Emoji:mode=harf"
```

> **Nota técnica:** `--resource-path` es necesario porque pandoc resuelve las
> imágenes relativas (`../recursos/figuras/...`) contra su directorio de
> trabajo, no contra la carpeta del archivo `.md` — sin esa opción, LuaLaTeX
> no encuentra las figuras al compilar desde la raíz del proyecto.

> **Nota técnica:** si necesitas añadir *otra* fuente de reserva además de
> Noto Color Emoji (por ejemplo para un símbolo nuevo que no cubra), no la
> agregues como una segunda entrada en `mainfontfallback`/`monofontfallback`:
> mezclar dos fuentes de reserva rompe `lualatex` (`luaotfload.add_fallback`
> falla con fuentes de color mezcladas con fuentes normales). En su lugar,
> cambia el carácter por un equivalente que sí cubra Noto Color Emoji.

---

## Estado del proyecto

| Módulo | Título | Estado |
|--------|--------|--------|
| 0 | Preliminares Matemáticos | ✅ Completo |
| 1 | Modelado de Sistemas Físicos | ✅ Completo |
| 2 | Función de Transferencia y Diagramas de Bloques | ✅ Completo |
| 3 | Respuesta Temporal de Sistemas | ✅ Completo |
| 4 | Error en Estado Estacionario | ⬜ Pendiente |
| 5–10 | (ver plan de desarrollo) | ⬜ Pendiente |

Ver el [plan de desarrollo](libro/02_plan_desarrollo.md) para el detalle completo.

---

## Licencia

Este material se distribuye bajo licencia
[Creative Commons BY-SA 4.0](LICENSE). Puedes usarlo, adaptarlo y compartirlo,
siempre citando la fuente y manteniendo la misma licencia.
