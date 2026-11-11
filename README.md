# Maplify 📶🗺️

**Maplify** es una herramienta web ligera y autónoma diseñada para la generación y visualización de mapas de cobertura de señal WiFi (*Site Survey*), desarrollada para la asignatura de **Redes de Datos II**.

Permite importar planos arquitectónicos y mediciones de intensidad de señal (dBm) desde hojas de cálculo de Excel para interpolar y proyectar mapas de calor sobre el plano del entorno auditado, facilitando el análisis de cobertura y toma de decisiones.

---

## 🚀 Características

- **100% Offline y Autocontenido:** No requiere conexión a internet, servidores locales ni instalación de dependencias externas.
- **Formato Single-File:** Tanto la aplicación (`Maplify.html`) como el manual (`Manual.html`) se compilan en archivos HTML únicos con librerías e imágenes embebidas en Base64.
- **Importación de Datos:** Lectura directa de coordenadas y niveles de señal (RSSI en dBm) desde hojas de cálculo (`.xlsx`).
- **Misión Guiada y Modo Libre:** Incluye un modo interactivo de aprendizaje paso a paso y un entorno libre para análisis personalizados.
- **Generación de Reportes Visuales:** Exportación de planos finales con mapas de calor superpuestos.

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
│   ├── Haz esto para empezar.txt   # Guía rápida de inicio
│   ├── Portada presentación.PNG   # Portada del proyecto
│   └── Site survey WiFi - Presentación.pptx # Presentación ejecutiva
│
├── ejemplos/                       # Recursos y datos de muestra para pruebas
│   ├── Excel de prueba (datos imaginarios).xlsx # Dataset de prueba con mediciones
│   ├── Plano.jfif.jpeg             # Plano base de referencia
│   ├── Puntos de medicion.jfif.jpeg # Imagen de referencia con puntos
│   └── Template.PNG                # Plantilla gráfica complementaria
│
└── fuente/                         # Código fuente y scripts de compilación
    ├── app.html                    # Código fuente de la aplicación
    ├── manual.html                 # Código fuente del manual
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
   - Carga el archivo de mediciones desde `ejemplos/Excel de prueba (datos imaginarios).xlsx`.
   - Genera el mapa de calor y analiza la cobertura.

---

## ⚙️ Compilación desde el Código Fuente

Si realizas modificaciones en los archivos de la carpeta `fuente/`, puedes regenerar los archivos autocontenidos ejecutando el script de compilación:

```bash
python fuente/construir.py
```

Este script embebe `xlsx.full.min.js` dentro de `Maplify.html` y convierte las imágenes de `fuente/img/` a Base64 dentro de `Manual.html`.

---

## 👨‍💻 Autor

- **Nicolás Mora** ([@nmorab28](https://github.com/nmorab28))
