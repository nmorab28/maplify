# Reglas de Antigravity — Maplify

@AGENTS.md

## Antigravity / Gemini

- **Selección de modelo y cuotas:**
  - **Plan Free (Nicolás):** Mantener de forma predeterminada **Gemini 3.8 Flash** para todas las tareas habituales, git, commits y redacción de PRs. Evita agotar la cuota diaria gratuita. Solo si una tarea de lógica matemática o algorítmica compleja falla con Flash, sugerir elevar temporalmente a Pro para esa respuesta puntual y luego regresar a Flash.
  - **Plan Pago (Amigo):** Usar Flash para git/commits/PR y Pro/Thinking para razonamiento y arquitectura.
- Usa las herramientas de lectura de archivos para entender el contexto antes de proponer cambios.
- Cuando edites código en `fuente/`, recuerda que los archivos de la raíz (`Maplify.html`, `Manual.html`) son generados. Indica al usuario que ejecute `python fuente/construir.py` después de cada cambio, o ejecútalo tú si tienes acceso.
- Responde en español salvo que el usuario escriba en otro idioma.
- Antes de crear un commit, verifica que el mensaje siga Conventional Commits según las reglas de AGENTS.md.
- No hagas `git push` ni `git merge` sin aprobación explícita.
- Para operaciones de red (push, pull, fetch), usa `BypassSandbox: true`.
