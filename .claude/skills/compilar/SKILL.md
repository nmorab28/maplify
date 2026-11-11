---
name: compilar
description: >-
  Compila los archivos autocontenidos Maplify.html y Manual.html desde el
  código fuente. Úsala después de editar archivos en fuente/.
---

# Compilar Maplify

Ejecuta el script de empaquetado para regenerar los archivos autocontenidos.

## Pasos

1. Asegúrate de que Python está disponible en el PATH.
2. Ejecuta:
   ```bash
   python fuente/construir.py
   ```
3. Verifica que la salida muestre los tamaños de `Maplify.html` y
   `Manual.html` sin errores.
4. Si hay errores:
   - `app.html debe contener la etiqueta de SheetJS exactamente una vez`:
     revisa que `fuente/app.html` tenga la línea
     `<script src="vendor/xlsx.full.min.js"></script>` intacta.
   - `Falta la imagen <ruta>`: verifica que todas las imágenes referenciadas
     en `fuente/manual.html` existan en `fuente/img/`.
   - `Quedó una imagen sin incluir en el manual`: algún `src="img/..."` no
     coincide con el patrón esperado (solo `.jpg`).

## Notas

- El script embebe `xlsx.full.min.js` directamente en `Maplify.html`.
- Las imágenes de `fuente/img/` se convierten a Base64 dentro de `Manual.html`.
- Los archivos generados van a la raíz del proyecto, no a `fuente/`.
