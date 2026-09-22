# Bibliografía y Recursos

---

## Textos principales

El curso se construye sobre dos textos clásicos de la ingeniería de control, que
se complementan entre sí:

**Kuo, Benjamin C.** — *Automatic Control Systems.*
Referencia principal para el tratamiento matemático riguroso: transformada de
Laplace, diagramas de flujo de señal y fórmula de Mason, lugar geométrico de las
raíces, y análisis en frecuencia. Destaca por su claridad en los procedimientos y
la abundancia de ejemplos.

**Ogata, Katsuhiko** — *Modern Control Engineering.*
Referencia principal para el modelado de sistemas físicos, la representación en
espacio de estado, y el diseño de controladores. Fuerte en la conexión entre la
teoría y los sistemas físicos reales (mecánicos, eléctricos, hidráulicos,
térmicos).

> **Cómo se usan juntos:** en general, Ogata aporta el marco físico e intuitivo y
> Kuo aporta el rigor de las herramientas de análisis. El curso toma lo mejor de
> cada uno y lo reorganiza bajo la filosofía conceptual propia (ver
> [filosofía de estudio](00_filosofia.md)).

### Correspondencia por módulo

| Módulo del curso | Kuo | Ogata |
|------------------|-----|-------|
| 0 — Preliminares matemáticos | Cap. 2 (apéndices de Laplace) | Apéndices A–B |
| 1 — Modelado de sistemas físicos | Cap. 4 | Caps. 2–3 |
| 2 — Función de transferencia y bloques | Cap. 3 | Cap. 2 |
| 3 — Respuesta temporal | Cap. 7 | Cap. 5 |
| 4 — Error en estado estacionario | Cap. 7 | Cap. 5 |
| 5 — Estabilidad (Routh-Hurwitz) | Cap. 6 | Cap. 5 |
| 6 — Lugar geométrico de las raíces | Cap. 8 | Cap. 6 |
| 7 — Análisis en frecuencia | Cap. 9 | Cap. 7 |
| 8 — Diseño de controladores | Cap. 10 | Caps. 6, 8 |
| 9 — Espacio de estado | Cap. 5 | Caps. 9–11 |
| 10 — Control discreto (introducción) | Cap. 11 | (complementario) |

> Los números de capítulo son orientativos y pueden variar según la edición.

---

## Herramientas de software

**Python** — ecosistema científico:
- [`python-control`](https://python-control.readthedocs.io/) — biblioteca central del curso para sistemas de control
- [`numpy`](https://numpy.org/) — cálculo numérico
- [`scipy`](https://scipy.org/) — integración de EDOs, procesamiento de señales
- [`sympy`](https://www.sympy.org/) — matemática simbólica (Laplace, fracciones parciales)
- [`matplotlib`](https://matplotlib.org/) — gráficas

**GNU Octave** — alternativa libre a MATLAB:
- [Octave](https://octave.org/) con los paquetes `control` y `signal`
- Sintaxis casi idéntica a MATLAB, útil si se migra material entre ambos

---

## Recursos complementarios (opcionales)

Otros textos y recursos que pueden enriquecer temas específicos:

- **Nise, N.** — *Control Systems Engineering.* Bueno por sus ejemplos de
  aplicación y casos de estudio integradores.
- **Dorf, R. & Bishop, R.** — *Modern Control Systems.* Amplio en ejercicios.
- **Franklin, Powell & Emami-Naeini** — *Feedback Control of Dynamic Systems.*
  Fuerte en diseño y en la conexión con el control digital.

---

## Nota sobre la filosofía frente a los textos

Los textos anteriores son, en su mayoría, **procedimentales**: presentan las
herramientas como técnicas a ejecutar. Este curso los usa como fuente de rigor y
ejemplos, pero **reorganiza el material bajo una filosofía distinta**, centrada en
el *porqué*, la *intuición* y la *transferencia de ideas entre dominios*. Cuando
haya tensión entre "como lo presenta el libro" y "como se entiende mejor", el
curso prioriza lo segundo.
