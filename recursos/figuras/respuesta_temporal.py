"""Figuras del Módulo 3 (respuesta temporal), con matplotlib.

    .venv/bin/python recursos/figuras/respuesta_temporal.py
        -> genera los .svg y los .pdf en recursos/figuras/

Estilo minimalista fijo (igual en todo el curso): cuadricula punteada tenue,
bordes superior/derecho ocultos, marcadores negros, fondo transparente.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt'] = 'curso-control'
import matplotlib.pyplot as plt


def _guardar(fig, nombre):
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True, metadata={'Date': None})
    plt.close(fig)


def _sin_bordes(ax):
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)


def senales_prueba(nombre):
    """3.1: las cuatro señales de prueba estándar, en pequeños múltiplos."""
    t = np.linspace(0, 3, 400)
    fig, axs = plt.subplots(1, 4, figsize=(9.5, 2.4), sharey=False)

    axs[0].annotate('', xy=(0, 1), xytext=(0, 0),
                     arrowprops=dict(arrowstyle='-|>', lw=1.8, color='black'))
    axs[0].plot([0.02, 3], [0, 0], color='black', lw=1.2)
    axs[0].set_ylim(-0.1, 1.15)
    axs[0].set_title(r'Impulso $\delta(t)$', fontsize=9)

    escalon = np.where(t >= 0, 1.0, 0.0)
    axs[1].plot(t, escalon, color='black', lw=1.6)
    axs[1].set_title(r'Escalón $u(t)$', fontsize=9)

    axs[2].plot(t, t, color='black', lw=1.6)
    axs[2].set_title(r'Rampa $t\,u(t)$', fontsize=9)

    axs[3].plot(t, 0.5 * t**2, color='black', lw=1.6)
    axs[3].set_title(r'Parábola $\frac{1}{2}t^2 u(t)$', fontsize=9)

    for ax in axs:
        _sin_bordes(ax)
        ax.set_xlim(-0.15, 3)
        ax.set_ylim(bottom=-0.1)
        ax.set_xlabel('$t$', fontsize=8)
        ax.grid(True, ls=':', lw=0.5, color='0.8')
        ax.tick_params(labelsize=7)

    _guardar(fig, nombre)


def especificaciones_segundo_orden(nombre, zeta=0.45, wn=3.0):
    """3.3-3.4: respuesta subamortiguada genérica con tr, tp, Mp, ts marcados."""
    wd = wn * np.sqrt(1 - zeta**2)
    beta = np.arccos(zeta)
    tp = np.pi / wd
    tr = (np.pi - beta) / wd
    ts = 4 / (zeta * wn)
    Mp = np.exp(-zeta * np.pi / np.sqrt(1 - zeta**2))
    pico = 1 + Mp

    t = np.linspace(0, 4.5, 1000)
    y = 1 - (np.exp(-zeta * wn * t) / np.sqrt(1 - zeta**2)) * np.sin(wd * t + beta)

    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.plot(t, y, color='black', lw=1.8)
    ax.axhline(1, color='0.4', lw=0.8, ls='-')
    ax.axhspan(0.98, 1.02, color='0.85', zorder=0)

    ax.plot([tp], [pico], 'o', ms=5, color='black')
    ax.annotate(f'$M_p$', (tp, pico), xytext=(tp + 0.12, pico + 0.01), fontsize=10)
    ax.plot([tp, tp], [0, pico], ls=':', lw=0.8, color='0.4')
    ax.annotate('$t_p$', (tp, -0.06), ha='center', fontsize=10)

    ax.plot([tr, tr], [0, 1], ls=':', lw=0.8, color='0.4')
    ax.annotate('$t_r$', (tr, -0.06), ha='center', fontsize=10)

    ax.plot([ts, ts], [0, 1.02], ls=':', lw=0.8, color='0.4')
    ax.annotate('$t_s$', (ts, -0.06), ha='center', fontsize=10)

    ax.set_xlim(0, 4.5)
    ax.set_ylim(-0.12, pico + 0.1)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('$y(t)$')
    ax.set_title(rf'Segundo orden subamortiguado: $\zeta={zeta}$, $\omega_n={wn}$ rad/s',
                 fontsize=10)
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    _sin_bordes(ax)

    _guardar(fig, nombre)
    return dict(wd=wd, tp=tp, tr=tr, ts=ts, Mp=Mp)


def polos_dominantes(nombre):
    """3.5: un par complejo dominante y un polo real rápido, para contrastar."""
    fig, ax = plt.subplots(figsize=(4.8, 3.4))
    ax.axhline(0, color='0.35', lw=0.9)
    ax.axvline(0, color='0.35', lw=0.9)

    for sig, om in [(-1, 3), (-1, -3)]:
        ax.plot(sig, om, 'x', ms=12, mew=2.4, color='black')
    ax.annotate('polo dominante\n(par complejo)', (-1, 3), xytext=(-3.6, 3.4),
                fontsize=8, ha='center')

    ax.plot(-8, 0, 'x', ms=12, mew=2.4, color='black')
    ax.annotate('polo rápido\n(despreciable)', (-8, 0), xytext=(-8, -2.0),
                fontsize=8, ha='center')

    ax.set_xlim(-10, 2)
    ax.set_ylim(-4.5, 4.5)
    ax.set_xlabel(r'$\sigma$')
    ax.set_ylabel(r'$j\omega$')
    ax.set_title('Polo dominante vs. polo rápido: 8× más lejos del eje', fontsize=9)
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    _sin_bordes(ax)

    _guardar(fig, nombre)


if __name__ == '__main__':
    senales_prueba('senales_prueba')
    specs = especificaciones_segundo_orden('especificaciones_segundo_orden')
    print('Specs figura:', specs)
    polos_dominantes('polos_dominantes')
