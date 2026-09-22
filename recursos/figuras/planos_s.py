"""Mapas de polos y ceros en el plano s del curso, con matplotlib.

    .venv/bin/python recursos/figuras/planos_s.py
        -> genera los .svg y los .pdf en recursos/figuras/

Estilo minimalista fijo (igual en todo el curso): cuadricula punteada tenue,
bordes superior/derecho ocultos, marcadores negros, fondo transparente.
"""
import matplotlib
matplotlib.use('Agg')
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
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    plano_polos_ceros(
        'plano_polos_ceros_m2',
        polos=[(-2, 0, '-2'), (-3, 0, '-3')],
        ceros=[(-1 / 3, 0, r'$-\frac{1}{3}$')],
        titulo=r'$G(s)=\frac{3s+1}{(s+2)(s+3)}$: polos $-2,-3$, cero $-\frac{1}{3}$',
        xlim=(-4, 1), ylim=(-1.5, 1.5),
    )
