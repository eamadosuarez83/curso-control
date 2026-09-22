#!/usr/bin/env bash
# Exporta los módulos del curso (y el libro completo) a PDF.
#
# Requiere: pandoc, TeX Live con lualatex, y las fuentes DejaVu + Noto Color
# Emoji (ya vienen en la mayoría de distros; ver README.md si faltan).
#
# Uso:
#   ./export_pdf.sh            # exporta cada módulo por separado + el libro completo
#   ./export_pdf.sh modulo_02  # exporta solo el módulo indicado (por nombre de archivo, sin .md)

set -euo pipefail
cd "$(dirname "$0")"

OUT=pdf
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

exportar_modulo() {
  local archivo="$1"
  local base
  base=$(basename "$archivo" .md)
  echo "-> $OUT/$base.pdf"
  pandoc "$archivo" -o "$OUT/$base.pdf" "${PANDOC_OPTS[@]}"
}

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
pandoc \
  libro/00_filosofia.md \
  libro/01_indice_general.md \
  modulos/modulo_*.md \
  libro/03_bibliografia.md \
  -o "$OUT/curso_control_completo.pdf" \
  --toc \
  "${PANDOC_OPTS[@]}"
echo "-> $OUT/curso_control_completo.pdf"

echo "Listo. PDFs en $OUT/ (carpeta ignorada por git)."
