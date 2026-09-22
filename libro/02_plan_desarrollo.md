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

## Compilar el libro completo a PDF

Cuando haya varios módulos, se pueden concatenar en orden y exportar de una vez:

```bash
# Orden de compilación
pandoc \
  libro/00_filosofia.md \
  libro/01_indice_general.md \
  modulos/modulo_00_preliminares_matematicos.md \
  modulos/modulo_01_modelado_sistemas_fisicos_conceptual.md \
  libro/03_bibliografia.md \
  -o curso_control_completo.pdf \
  --pdf-engine=xelatex \
  --toc \
  -V geometry:margin=2.5cm \
  -V mainfont="DejaVu Serif" \
  -V documentclass=report
```
