#!/usr/bin/env bash
# Exporta los módulos del curso (y el libro completo) a PDF.
#
# Requiere: pandoc, TeX Live con lualatex, las fuentes DejaVu + Noto Color
# Emoji (ver README.md si faltan), y para las figuras: un entorno Python con
# schemdraw + matplotlib (.venv/, ver README.md) y el binario `dot` de
# Graphviz para los diagramas de flujo de señal (recursos/figuras/*.dot).
#
# Uso:
#   ./export_pdf.sh            # exporta cada módulo por separado + el libro completo
#   ./export_pdf.sh modulo_02  # exporta solo el módulo indicado (por nombre de archivo, sin .md)

set -euo pipefail
cd "$(dirname "$0")"

OUT=pdf
FIGURAS=recursos/figuras
mkdir -p "$OUT"

PANDOC_OPTS=(
  --pdf-engine=lualatex
  -V geometry:margin=2.5cm
  -V mainfont="DejaVu Serif"
  -V monofont="DejaVu Sans Mono"
  -V mainfontfallback="Noto Color Emoji:mode=harf"
  -V monofontfallback="Noto Color Emoji:mode=harf"
  -V documentclass=report
)

# ------------------------------------------------------------------ figuras
# Cada script de recursos/figuras/*.py emite .svg (para leer el Markdown en
# GitHub) y .pdf (vectorial, para LuaLaTeX, que no incrusta SVG). Los .dot
# de Graphviz se convierten a ambos formatos con `dot`.
generar_figuras() {
  local py
  py="$(command -v python3)"
  [ -x .venv/bin/python ] && py="$(pwd)/.venv/bin/python"

  echo "Generando figuras ($py)..."
  # los scripts escriben con nombre de archivo relativo (Drawing(file=...),
  # fig.savefig(...)): hay que correrlos DESDE recursos/figuras/, si no
  # las figuras terminan en el directorio donde se invocó el script.
  (
    cd "$FIGURAS"
    for f in *.py; do
      [ -e "$f" ] || continue
      "$py" "$f"
    done
    for f in *.dot; do
      [ -e "$f" ] || continue
      dot -Tsvg "$f" -o "${f%.dot}.svg"
      dot -Tpdf "$f" -o "${f%.dot}.pdf"
    done
  )
}

# Sustituye rutas .../figuras/nombre.svg -> .pdf en una copia temporal, para
# que LuaLaTeX use el vectorial. Devuelve la ruta de la copia por stdout.
preparar_md() {
  local origen="$1"
  local copia
  copia="$(dirname "$origen")/.build-$(basename "$origen")"
  sed 's|\(recursos/figuras/[A-Za-z0-9_-]*\)\.svg|\1.pdf|g' "$origen" > "$copia"
  echo "$copia"
}

exportar_modulo() {
  local archivo="$1"
  local base copia
  base=$(basename "$archivo" .md)
  copia=$(preparar_md "$archivo")
  echo "-> $OUT/$base.pdf"
  pandoc "$copia" -o "$OUT/$base.pdf" \
    --resource-path="$(dirname "$archivo")" \
    "${PANDOC_OPTS[@]}"
  rm -f "$copia"
}

generar_figuras

if [ $# -ge 1 ]; then
  # Exportar solo el/los módulo(s) pedido(s)
  for nombre in "$@"; do
    exportar_modulo "modulos/${nombre}.md"
  done
  exit 0
fi

echo "Exportando módulos individuales..."
for f in modulos/modulo_*.md; do
  exportar_modulo "$f"
done

echo "Exportando libro completo..."
COPIAS=()
for f in libro/00_filosofia.md libro/01_indice_general.md modulos/modulo_*.md libro/03_bibliografia.md; do
  COPIAS+=("$(preparar_md "$f")")
done
pandoc "${COPIAS[@]}" \
  -o "$OUT/curso_control_completo.pdf" \
  --resource-path=libro:modulos \
  --toc \
  "${PANDOC_OPTS[@]}"
rm -f "${COPIAS[@]}"
echo "-> $OUT/curso_control_completo.pdf"

echo "Listo. PDFs en $OUT/ (carpeta ignorada por git)."
