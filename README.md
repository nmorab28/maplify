# Maplify 📶🗺️

**Maplify** es una herramienta web ligera y autónoma diseñada para la generación, análisis y visualización de mapas de cobertura de señal WiFi (*Site Survey*), desarrollada para la asignatura de **Redes de Datos II** en la **Universidad El Bosque**.

Permite importar planos arquitectónicos y mediciones de intensidad de señal (RSSI en dBm) desde hojas de cálculo de Excel para interpolar y proyectar mapas de calor sobre el plano del entorno auditado, validar la ubicación de routers y generar gráficos estadísticos de cobertura y calidad por banda.

---

## 🚀 Características

- **100% Offline y Autocontenido:** No requiere conexión a internet, servidores locales ni instalación de dependencias externas.
- **Formato Single-File:** Tanto la aplicación (`Maplify.html`) como el manual (`Manual.html`) se compilan en archivos HTML únicos con librerías, gráficos e imágenes embebidas en Base64.
- **Importación Flexible de Datos:** Lectura directa de mediciones y niveles de señal (RSSI en dBm) desde archivos Excel (`.xlsx`), con plantilla descargable incluida.
- **Misión Guiada y Laboratorio Libre:** Modo interactivo gamificado paso a paso para usuarios nuevos, y entorno profesional avanzado para mover puntos, calibrar escalas y ajustar parámetros.
- **Validación de Routers:** Ubicación física de Puntos de Acceso en el plano con detección automática de inconsistencias o lecturas anómalas de señal.
- **Panel de Gráficas Estadísticas (`📈 Gráficas`):** Comparación visual de potencia por punto entre bandas (2.4 GHz vs 5 GHz), distribución porcentual de calidad de cobertura y conclusiones técnicas descargables en PNG.

---

## 📂 Estructura del Repositorio

```text
maplify/
├── Maplify.html                    # Aplicación lista para usar (autocontenida)
├── Manual.html                     # Manual interactivo gamificado
├── README.md                       # Documentación principal del proyecto
├── AGENTS.md                       # Contrato central de reglas para agentes de IA
├── CLAUDE.md                       # Configuración y directrices para Claude Code
├── GEMINI.md                       # Configuración y directrices para Antigravity / Gemini
│
├── docs/                           # Documentación y presentaciones del proyecto
│   ├── Cuestionario_Cisco_Site_Survey_Maplify.pdf # Cuestionario técnico estilo Cisco CCNA en IEEE
│   ├── Haz esto para empezar.txt   # Guía rápida de inicio
│   ├── Maplify · Site survey WiFi.pptx # Presentación ejecutiva actualizada (con referencias IEEE)
│   ├── Site survey WiFi - Presentación.pptx # Presentación base
│   ├── Portada presentación.PNG   # Portada del proyecto
│   ├── Portada presentación - opción A (clara).png # Portada variante clara
│   └── investigacion/              # Marco teórico, glosario técnico y reglas
│       ├── glosario-tecnico.md     # Catálogo con +32 términos IEEE/CWNP/Cisco
│       ├── marco-teorico.md        # Propagación RF, fórmulas FSPL/IDW y normativa
│       ├── contexto-para-ia.md     # Reglas de negocio y especificaciones de código
│       └── guia-usuario-basica.md  # Conceptos y preguntas frecuentes para usuarios
│
├── ejemplos/                       # Recursos y datos de muestra para pruebas
│   ├── Plantilla Maplify.xlsx      # Plantilla en blanco para nuevos relevamientos
│   ├── Relevamiento_WiFi_Limpio.xlsx # Dataset de mediciones reales de campo
│   ├── Excel de prueba (datos imaginarios).xlsx # Dataset de prueba adicional
│   ├── Plano.jfif.jpeg             # Plano base de referencia
│   ├── Puntos de medicion.jfif.jpeg # Imagen de referencia con puntos
│   └── Template.PNG                # Plantilla gráfica complementaria
│
└── fuente/                         # Código fuente y scripts de compilación
    ├── app.html                    # Código fuente de la aplicación Maplify
    ├── manual.html                 # Código fuente del manual interactivo
    ├── construir.py                # Script en Python para compilar a Single-File
    ├── vendor/                     # Librerías de terceros (SheetJS / xlsx)
    └── img/                        # Imágenes fuente para el manual
```

---

## 🛠️ Cómo Empezar

1. **Abrir el Manual:** Haz doble clic sobre `Manual.html` en tu navegador (Google Chrome o Microsoft Edge recomendado).
2. **Ejecutar Maplify:** Abre `Maplify.html` para iniciar la aplicación.
3. **Cargar Datos:**
   - Selecciona el plano arquitectónico desde `ejemplos/Plano.jfif.jpeg` (o uno propio).
   - Carga el archivo de mediciones desde `ejemplos/Relevamiento_WiFi_Limpio.xlsx` (o `ejemplos/Plantilla Maplify.xlsx`).
   - Ubica los puntos en el plano y genera el mapa de calor.
   - Explora las gráficas estadísticas comparativas y descarga el informe.

---

## ⚙️ Compilación desde el Código Fuente

Si realizas modificaciones en los archivos de la carpeta `fuente/`, puedes regenerar los archivos autocontenidos ejecutando el script de compilación:

```bash
python fuente/construir.py
```

Este script embebe `xlsx.full.min.js` dentro de `Maplify.html` y optimiza las referencias a imágenes de `fuente/img/` dentro de `Manual.html`.

---

## 👨‍💻 Autores

- **Nicolás Mora** ([@nmorab28](https://github.com/nmorab28)) y equipo de trabajo de Redes de Datos II — Universidad El Bosque.
