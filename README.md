# Curso de Control Analógico

> Un curso completo de sistemas de control analógico en español, escrito para
> **entender** — no solo para calcular.

[![Licencia](https://img.shields.io/badge/licencia-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow.svg)]()
[![Módulos](https://img.shields.io/badge/módulos-2%2F11-orange.svg)]()

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
│   └── modulo_01_modelado_sistemas_fisicos_conceptual.md
├── codigo/                    ← código de las prácticas
│   ├── python/
│   └── octave/
└── recursos/                  ← imágenes, diagramas, material extra
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

## Exportar a PDF

Todo el material está en Markdown con LaTeX, pensado para exportarse a PDF:

```bash
# Con Pandoc + XeLaTeX (mejor calidad matemática)
pandoc modulos/modulo_00_preliminares_matematicos.md \
  -o modulo_00.pdf --pdf-engine=xelatex -V geometry:margin=2.5cm

# Para compilar el libro completo (ver plan de desarrollo)
```

---

## Estado del proyecto

| Módulo | Título | Estado |
|--------|--------|--------|
| 0 | Preliminares Matemáticos | ✅ Completo |
| 1 | Modelado de Sistemas Físicos | ✅ Completo |
| 2 | Función de Transferencia y Diagramas de Bloques | ⬜ Pendiente |
| 3–10 | (ver plan de desarrollo) | ⬜ Pendiente |

Ver el [plan de desarrollo](libro/02_plan_desarrollo.md) para el detalle completo.

---

## Licencia

Este material se distribuye bajo licencia
[Creative Commons BY-SA 4.0](LICENSE). Puedes usarlo, adaptarlo y compartirlo,
siempre citando la fuente y manteniendo la misma licencia.
