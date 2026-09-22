"""Diagramas de bloques del curso, hechos con schemdraw.

    .venv/bin/python recursos/figuras/bloques_schemdraw.py
        -> genera los .svg y los .pdf en recursos/figuras/

SVG para leer el Markdown en GitHub o cualquier visor; PDF vectorial porque
LuaLaTeX/XeLaTeX no incrustan SVG (ver export_pdf.sh).
"""
import schemdraw
import schemdraw.elements as elm
from schemdraw import dsp, flow


def _signos(s, mas='+', menos='−'):
    return (s.label(mas, loc='left', ofst=(-.1, .25))
             .label(menos, loc='bottom', ofst=(-.25, -.1)))


def sistema_caja(ext):
    """Modulo 1, 1.1: la caja entrada -> sistema -> salida."""
    with schemdraw.Drawing(file=f'sistema_caja{ext}', show=False) as d:
        d.config(fontsize=13, unit=2.4)
        d += dsp.Arrow().right().label('u(t)', loc='bottom')
        S = d.add(flow.Box(w=2.6, h=1.4).anchor('W').label('SISTEMA'))
        d += dsp.Arrow().right().at(S.E).label('y(t)', loc='bottom')


def bloque_generico(ext):
    """Modulo 2, 2.3: un bloque solo, U(s) -> G(s) -> Y(s)."""
    with schemdraw.Drawing(file=f'bloque_generico{ext}', show=False) as d:
        d.config(fontsize=13, unit=2)
        d += dsp.Arrow().right().label('U(s)', loc='bottom')
        G = d.add(flow.Box(w=1.8, h=1.1).anchor('W').label('G(s)'))
        d += dsp.Arrow().right().at(G.E).label('Y(s)', loc='bottom')


def punto_suma(ext):
    """Modulo 2, 2.3: punto de suma/resta con dos entradas con signo."""
    with schemdraw.Drawing(file=f'punto_suma{ext}', show=False) as d:
        d.config(fontsize=13, unit=1.8)
        d += dsp.Arrow().right().label('A', loc='top')
        s = d.add(_signos(dsp.Sum().anchor('W')))
        d += dsp.Arrow().up().at((s.S[0], s.S[1] - 1.2)).toy(s.S).label('B', loc='bottom')
        d += dsp.Arrow().right().at(s.E).label('A ± B', loc='top')


def punto_toma(ext):
    """Modulo 2, 2.3: punto de toma, la señal se copia sin consumirse."""
    with schemdraw.Drawing(file=f'punto_toma{ext}', show=False) as d:
        d.config(fontsize=13, unit=1.8)
        d += dsp.Line().right().label('X(s)', loc='top')
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.4).label('a otro bloque', loc='top')
        d += dsp.Line().down().at(tap.center).length(1.2)
        d += dsp.Arrow().right().length(1.4).label('y a otro más', loc='bottom')


def lazo_realimentado_generico(ext):
    """Modulo 2, 2.3: lazo G(s)/H(s) generico con senales R, E, Y."""
    with schemdraw.Drawing(file=f'lazo_realimentado_generico{ext}', show=False) as d:
        d.config(fontsize=13, unit=2.1)
        d += dsp.Arrow().right().label('R(s)', loc='left')
        s = d.add(_signos(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).label('E(s)', loc='top')
        G = d.add(flow.Box(w=1.7, h=1.1).anchor('W').label('G(s)'))
        d += dsp.Line().right().at(G.E).length(1)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.3).label('Y(s)', loc='right')
        d += dsp.Line().down().at(tap.center).length(1.9)
        d += dsp.Line().left().length(0.9)
        H = d.add(flow.Box(w=1.7, h=1.1).anchor('E').label('H(s)'))
        d += dsp.Arrow().left().at(H.W).tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


def control_tacometro(ext):
    """Modulo 2, 2.4: dos lazos anidados, posicion con realimentacion de
    velocidad (tacometro) sobre el sistema rotacional del Modulo 1.
    Lazo interno (K_t) arriba de la fila principal, lazo externo (unitario)
    abajo, para que no se crucen."""
    with schemdraw.Drawing(file=f'control_tacometro{ext}', show=False) as d:
        d.config(fontsize=11, unit=1.9)
        d += dsp.Arrow().right().label('R(s)', loc='left')
        s = d.add(_signos(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).length(0.8).label('E(s)', loc='top')
        Kp = d.add(flow.Box(w=1.2, h=1.0).anchor('W').label('$K_p$'))
        d += dsp.Line().right().at(Kp.E).length(0.6)
        s2 = d.add(_signos(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s2.E).length(0.6)
        G2 = d.add(flow.Box(w=1.8, h=1.0).anchor('W').label('1/(s+3)'))
        d += dsp.Line().right().at(G2.E).length(0.5)
        tapO = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(0.5).label('$\\Omega(s)$', loc='top')
        I = d.add(flow.Box(w=1.2, h=1.0).anchor('W').label('1/s'))
        d += dsp.Line().right().at(I.E).length(0.5)
        tapT = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.0).label('$\\Theta(s)$', loc='right')

        # realimentacion de velocidad (tacometro K_t): entra a s2 por arriba
        d += dsp.Line().up().at(tapO.center).length(1.4)
        d += dsp.Line().left().length(0.5)
        Kt = d.add(flow.Box(w=1.1, h=0.9).anchor('E').label('$K_t$'))
        d += dsp.Line().left().at(Kt.W).tox(s2.N)
        d += dsp.Arrow().down().toy(s2.N)

        # realimentacion de posicion (unitaria): entra a s por abajo
        d += dsp.Line().down().at(tapT.center).length(2.3)
        d += dsp.Line().left().tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


if __name__ == '__main__':
    for backend, ext in (('svg', '.svg'), ('matplotlib', '.pdf')):
        schemdraw.use(backend)
        sistema_caja(ext)
        bloque_generico(ext)
        punto_suma(ext)
        punto_toma(ext)
        lazo_realimentado_generico(ext)
        control_tacometro(ext)
