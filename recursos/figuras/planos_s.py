"""Mapas de polos y ceros en el plano s del curso, con matplotlib.

    .venv/bin/python recursos/figuras/planos_s.py
        -> genera los .svg y los .pdf en recursos/figuras/

Estilo minimalista fijo (igual en todo el curso): cuadricula punteada tenue,
bordes superior/derecho ocultos, marcadores negros, fondo transparente.
"""
import matplotlib
matplotlib.use('Agg')
# SVG reproducible: sin esto, cada corrida cambia el timestamp y los IDs
# internos (clip-path, glyphs) aunque la figura sea visualmente idéntica,
# y el .svg aparece como "modificado" en git sin ningún cambio real.
matplotlib.rcParams['svg.hashsalt'] = 'curso-control'
import matplotlib.pyplot as plt


def plano_polos_ceros(nombre, polos, ceros, titulo, xlim, ylim):
    """polos y ceros: listas de (sigma, omega, etiqueta). Dibuja x=polo, o=cero."""
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.axhline(0, color='0.35', lw=0.9)
    ax.axvline(0, color='0.35', lw=0.9)
    for sig, om, etq in polos:
        ax.plot(sig, om, 'x', ms=11, mew=2.2, color='black')
        ax.annotate(etq, (sig, om), textcoords='offset points',
                    xytext=(0, 8), fontsize=9, ha='center')
    for sig, om, etq in ceros:
        ax.plot(sig, om, 'o', ms=8, mfc='none', mec='black', mew=1.8)
        ax.annotate(etq, (sig, om), textcoords='offset points',
                    xytext=(0, 8), fontsize=9, ha='center')
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel(r'$\sigma$')
    ax.set_ylabel(r'$j\omega$')
    ax.set_title(titulo, fontsize=10)
    ax.grid(True, ls=':', lw=0.5, color='0.8')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True, metadata={'Date': None})
    plt.close(fig)


def plano_regiones_estabilidad(nombre):
    """Modulo 0, 0.1: el plano s dividido en SPI/eje/SPD, sin polos ni
    ceros concretos -- es el mapa conceptual, no un caso particular."""
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    ax.axvspan(-4, 0, color='0.88', zorder=0)
    ax.axvspan(0, 4, color='1.0', zorder=0)
    ax.axhline(0, color='0.35', lw=0.9, zorder=2)
    ax.axvline(0, color='black', lw=1.4, zorder=2)
    ax.text(-2.6, 2.3, 'SPI\n(estable)', ha='center', va='center', fontsize=10)
    ax.text(2.2, 2.3, 'SPD\n(inestable)', ha='center', va='center', fontsize=10)
    ax.annotate('eje imaginario:\nmarginalmente estable',
                (0, -2.1), xytext=(1.7, -2.9), fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', lw=0.8, color='0.35'))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3.3, 3.3)
    ax.set_xlabel(r'$\sigma$')
    ax.set_ylabel(r'$j\omega$')
    ax.set_title('El plano $s$: dónde vive la estabilidad', fontsize=10)
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True, metadata={'Date': None})
    plt.close(fig)


if __name__ == '__main__':
    plano_regiones_estabilidad('plano_regiones_estabilidad')
    plano_polos_ceros(
        'plano_polos_ceros_m2',
        polos=[(-2, 0, '-2'), (-3, 0, '-3')],
        ceros=[(-1 / 3, 0, r'$-\frac{1}{3}$')],
        titulo=r'$G(s)=\frac{3s+1}{(s+2)(s+3)}$: polos $-2,-3$, cero $-\frac{1}{3}$',
        xlim=(-4, 1), ylim=(-1.5, 1.5),
    )
