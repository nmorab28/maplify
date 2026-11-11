# AGENTS.md — Maplify

## Proyecto

Maplify es una herramienta web autocontenida (single-file HTML) para generar
mapas de calor de cobertura WiFi (Site Survey). Stack: HTML, CSS, JavaScript
vanilla y Python para el build. No hay framework, bundler ni servidor.

## Arquitectura

```
fuente/app.html        → código fuente de la aplicación
fuente/manual.html     → código fuente del manual interactivo
fuente/construir.py    → empaqueta todo en archivos autocontenidos
fuente/vendor/          → librerías de terceros (SheetJS)
fuente/img/             → imágenes del manual

Maplify.html           → app compilada (app.html + SheetJS embebido)
Manual.html            → manual compilado (manual.html + imágenes en Base64)
```

Los archivos `Maplify.html` y `Manual.html` de la raíz son **generados**.
Nunca se editan directamente: se regeneran con `python fuente/construir.py`.

## Comandos

- Compilar: `python fuente/construir.py`
- Verificar que los archivos generados están al día: comparar timestamps de
  `fuente/` con `Maplify.html` y `Manual.html`.

## Convenciones de código

- HTML semántico; sin frameworks ni librerías adicionales salvo SheetJS.
- CSS embebido dentro del HTML (no hay archivos .css separados).
- JavaScript vanilla; sin TypeScript, sin transpilación.
- Comentarios en español.
- Funciones y variables en camelCase; constantes en UPPER_SNAKE_CASE.
- Cada función debe tener un comentario breve que explique su propósito.

## Convenciones de commits (Conventional Commits)

- `feat:` nueva funcionalidad
- `fix:` corrección de bug
- `docs:` cambios en documentación
- `style:` formato, sin cambio de lógica
- `refactor:` reestructuración sin cambio funcional
- `build:` cambios en construir.py o vendor/
- `chore:` tareas menores (gitignore, configuración de agentes)

Mensaje en español, imperativo, primera letra en minúscula tras el prefijo.
Línea de asunto ≤ 72 caracteres. Cuerpo opcional con viñetas.

## Flujo Git

1. Crear rama desde `main`: `feat/<descripción>`, `fix/<descripción>`,
   `docs/<descripción>`.
2. Hacer commits atómicos con Conventional Commits.
3. Abrir Pull Request borrador hacia `main`.
4. El humano revisa el diff y aprueba el merge.
5. **Nunca** hacer push directo a `main`; siempre por PR.

## Seguridad

- No incluir secretos, tokens ni credenciales en ningún archivo del repo.
- No ejecutar comandos destructivos (`rm -rf`, borrado masivo) sin
  aprobación explícita del humano.
- No hacer merge ni deploy sin aprobación humana.

## Definición de terminado

- `python fuente/construir.py` se ejecuta sin errores.
- Los archivos generados (`Maplify.html`, `Manual.html`) reflejan los
  cambios del código fuente.
- Commits siguen Conventional Commits.
- El cambio tiene un PR revisado antes de llegar a `main`.

