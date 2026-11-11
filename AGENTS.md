# AGENTS.md — Maplify

## Proyecto

Maplify es una herramienta web autocontenida (single-file HTML) para generar
mapas de calor de cobertura WiFi (Site Survey). Stack: HTML, CSS, JavaScript
vanilla y Python para el build. No hay framework, bundler ni servidor.

## Arquitectura y Carpetas

```text
Maplify.html           → app compilada (app.html + SheetJS embebido)
Manual.html            → manual compilado (manual.html + imágenes en Base64)
docs/                  → manuales, presentaciones y recursos de documentación
ejemplos/              → datasets (Excel) y planos de referencia para pruebas
fuente/                → código fuente original y script de build (construir.py)
```

Los archivos `Maplify.html` y `Manual.html` de la raíz son **generados**.
Nunca se editan directamente: se regeneran con `python fuente/construir.py`.

## Comandos

- Compilar: `python fuente/construir.py`
- Verificar archivos generados: comparar timestamps de `fuente/` con `Maplify.html` y `Manual.html`.

## Convenciones de código

- HTML semántico; sin frameworks ni librerías adicionales salvo SheetJS.
- CSS embebido dentro del HTML (no hay archivos .css separados).
- JavaScript vanilla; sin TypeScript, sin transpilación.
- Comentarios en español.
- Funciones y variables en camelCase; constantes en UPPER_SNAKE_CASE.
- Cada función debe tener un comentario breve que explique su propósito.

## Política de Modelos y Optimización de Tokens

Para optimizar consumo y costos según el plan de cada integrante:

### Tareas Simples y Operativas (Bajo Consumo)
- Tareas: redacción de commits, apertura de PRs, git status, formateo, tareas mecánicas de documentación menor.
- **Antigravity (Plan Gratuito):** Usar siempre **Gemini Flash** (o Flash-Lite si está disponible). No gastar cuota de modelos avanzados en tareas de soporte.
- **Antigravity (Plan Pago):** Usar modelos ligeros/Flash para git, commits y PRs.
- **Claude Code (Plan Pro):** Usar **Haiku** para commits, descripciones de PR y tareas mecánicas.

### Tareas Complejas y de Razonamiento (Alto Desempeño)
- Tareas: arquitectura, matemáticas de interpolación (IDW, radios de cobertura, dBm), depuración profunda de lógica de cálculo o refactorización estructural.
- **Antigravity (Plan Gratuito):** Usar Gemini Flash optimizando el prompt (contexto mínimo y conciso), o pasar a Gemini Pro solo para la decisión técnica puntual sin mantenerlo activo en conversaciones largas.
- **Antigravity (Plan Pago):** Usar **Gemini Pro / Thinking** para diseño algorítmico y revisión técnica.
- **Claude Code (Plan Pro):** Usar **Sonnet** (o Opus si la complejidad lo amerita) para arquitectura y algoritmos.

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

1. Crear rama desde `main`: `feat/<descripción>`, `fix/<descripción>`, `refactor/<descripción>`, `docs/<descripción>`.
2. Hacer commits atómicos con Conventional Commits.
3. Abrir Pull Request borrador hacia `main`.
4. El humano revisa el diff y aprueba el merge.
5. **Nunca** hacer push directo a `main`; siempre por PR.

## Seguridad

- No incluir secretos, tokens ni credenciales en ningún archivo del repo.
- No ejecutar comandos destructivos (`rm -rf`, borrado masivo) sin aprobación explícita del humano.
- No hacer merge ni deploy sin aprobación humana.

## Definición de terminado

- `python fuente/construir.py` se ejecuta sin errores.
- Los archivos generados (`Maplify.html`, `Manual.html`) reflejan los cambios del código fuente.
- Commits siguen Conventional Commits.
- El cambio tiene un PR revisado antes de llegar a `main`.
