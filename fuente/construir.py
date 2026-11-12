"""Genera los dos archivos que se entregan, en la carpeta principal:
- Maplify.html: app.html (el programa Maplify) con SheetJS incluida.
- Manual.html: manual.html con todas las imágenes de img/ incluidas.
"""
import base64
import json
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
# Cada imagen se guarda UNA vez en window.IMAGENES y las etiquetas quedan con data-img;
# el manual les pone la imagen al mostrarlas (función fuenteImagen).
manual = (carpeta / 'manual.html').read_text(encoding='utf-8')
cache = {}


def registrar(nombre):
    if nombre not in cache:
        ruta = carpeta / 'img' / nombre
        if not ruta.exists():
            raise SystemExit(f'Falta la imagen {ruta}')
        cache[nombre] = 'data:image/jpeg;base64,' + base64.b64encode(ruta.read_bytes()).decode()


def a_data_img(coincidencia):
    registrar(coincidencia.group(1))
    return f'data-img="{coincidencia.group(1)}"'


manual, cantidad = re.subn(r'src="img/([\w.-]+\.jpg)"', a_data_img, manual)
# Imágenes nombradas desde el código con fuenteImagen('nombre.jpg')
for nombre in re.findall(r"fuenteImagen\('([\w.-]+\.jpg)'\)", manual):
    registrar(nombre)
if 'src="img/' in manual:
    raise SystemExit('Quedó una imagen sin incluir en el manual')
if '</head>' not in manual:
    raise SystemExit('manual.html no tiene </head>')
datos = '<script>window.IMAGENES = ' + json.dumps(cache) + ';</script>\n</head>'
manual = manual.replace('</head>', datos, 1)

salida = carpeta.parent / 'Manual.html'
salida.write_text(manual, encoding='utf-8', newline='\n')
print(salida, salida.stat().st_size, 'bytes', f'({cantidad} referencias, {len(cache)} imágenes distintas)')
