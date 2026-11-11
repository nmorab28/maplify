"""Genera los dos archivos que se entregan, en la carpeta principal:
- Maplify.html: app.html (el programa Maplify) con SheetJS incluida.
- Manual.html: manual.html con todas las imágenes de img/ incluidas.
"""
import base64
import re
from pathlib import Path

carpeta = Path(__file__).resolve().parent

# ---- Programa ----
html = (carpeta / 'app.html').read_text(encoding='utf-8')
sheetjs = (carpeta / 'vendor' / 'xlsx.full.min.js').read_text(encoding='utf-8')

etiqueta = '<script src="vendor/xlsx.full.min.js"></script>'
if html.count(etiqueta) != 1:
    raise SystemExit('app.html debe contener la etiqueta de SheetJS exactamente una vez')
if '</script' in sheetjs.lower():
    raise SystemExit('SheetJS contiene una etiqueta de cierre que rompería la página')

salida = carpeta.parent / 'Maplify.html'
salida.write_text(html.replace(etiqueta, '<script>' + sheetjs + '</script>'), encoding='utf-8', newline='\n')
print(salida, salida.stat().st_size, 'bytes')

# ---- Manual ----
manual = (carpeta / 'manual.html').read_text(encoding='utf-8')
cache = {}


def incluir(coincidencia):
    nombre = coincidencia.group(1)
    if nombre not in cache:
        ruta = carpeta / 'img' / nombre
        if not ruta.exists():
            raise SystemExit(f'Falta la imagen {ruta}')
        cache[nombre] = 'data:image/jpeg;base64,' + base64.b64encode(ruta.read_bytes()).decode()
    return f'src="{cache[nombre]}"'


manual, cantidad = re.subn(r'src="img/([\w.-]+\.jpg)"', incluir, manual)
if 'src="img/' in manual:
    raise SystemExit('Quedó una imagen sin incluir en el manual')

salida = carpeta.parent / 'Manual.html'
salida.write_text(manual, encoding='utf-8', newline='\n')
print(salida, salida.stat().st_size, 'bytes', f'({cantidad} imágenes, {len(cache)} distintas)')
