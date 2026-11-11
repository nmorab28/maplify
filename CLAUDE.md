@AGENTS.md

## Claude Code

- **Selección de modelo y tokens (Plan Pro):**
  - Para tareas rutinarias (commits, PRs, lint, git, resúmenes mecánicos): configurar o invocar con modelo **Haiku** (`--model haiku`).
  - Para arquitectura, diseño de algoritmos de calor y refactorizaciones críticas: usar **Sonnet** (`--model sonnet`).
- Usa plan mode para cambios que toquen más de 3 archivos.
- Antes de editar código en `fuente/`, lee `fuente/construir.py` para entender cómo se empaqueta el proyecto.
- Los archivos `Maplify.html` y `Manual.html` de la raíz son generados; nunca los edites directamente. Edita `fuente/app.html` o `fuente/manual.html` y luego ejecuta `python fuente/construir.py`.
- Responde en español salvo que el usuario escriba en otro idioma.
- Antes de crear un commit, verifica que el mensaje siga Conventional Commits según las reglas de AGENTS.md.
- No hagas `git push`, `git merge` ni operaciones destructivas sin aprobación explícita del usuario.
