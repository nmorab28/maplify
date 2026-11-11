# Contexto de Dominio y Reglas de Negocio para Agentes de IA

**Proyecto:** Maplify — Sistema Web de Generación de Mapas de Calor para Site Survey WiFi  
**Destinatarios:** Agentes de IA (Claude Code, Antigravity / Gemini CLI, Cursor, Codex) y Desarrolladores  
**Propósito:** Proveer un marco de verdad inequívoco sobre el dominio técnico de radiofrecuencia y la arquitectura de Maplify, eliminando alucinaciones conceptuales y garantizando coherencia en la generación o refactorización de código.

---

## 1. Glosario de Precisión Anti-Alucinación (20 Términos Clave)

Cuando un agente de IA genere código, comentarios, funciones o documentación, debe apegarse estrictamente a estas definiciones:

1. **RSSI:** Valor en dBm (número negativo). Jamás expresarlo como porcentaje en la lógica interna del algoritmo.
2. **dBm:** Decibel-milivatio. Escala logarítmica con signo negativo para recepción (ej. $-65\text{ dBm}$). Nunca usar dBm positivo para recepción en interiores.
3. **Punto de Medición (Data Point):** Tupla compuesta por identificador (`id`), coordenadas relativas normalizadas en el plano (`x, y` en rango $[0, 1]$ o en píxeles), y potencia recibida (`rssi` en dBm).
4. **IDW (Inverse Distance Weighting):** Algoritmo de interpolación donde el peso es $w = 1 / d^2$. No confundir con Kriging ni con interpolación bilineal.
5. **Radio de Cobertura / Influencia ($R_{\text{max}}$):** Distancia física o euclidiana máxima a partir de la cual una muestra deja de ponderar en un píxel del mapa.
6. **Umbral de Cobertura (Coverage Threshold):** Valor de corte (ej. $-80\text{ dBm}$). Puntos con valor inferior o no alcanzados por el radio de corte quedan sin pintar.
7. **BSSID:** Dirección MAC de la interfaz de radio del AP (cadena hexadecimal de 12 dígitos, separada por dos puntos).
8. **SSID:** Nombre de la red inalámbrica (cadena alfanumérica visible).
9. **Canal (Channel):** Entero que identifica la frecuencia central (en 2.4 GHz: 1 al 11/13; en 5 GHz: 36, 40, etc.).
10. **Atenuación:** Pérdida en dB (valor positivo que se resta a la potencia).
11. **Canvas HTML5:** Elemento del DOM donde se dibuja el mapa de calor a nivel de píxeles (`ctx.getImageData`, `ctx.putImageData` o arcos radiales).
12. **Single-File:** Aplicación empaquetada en un único archivo HTML (`Maplify.html`) sin dependencias de red externas ni imports remotos (`<script src="...">`).
13. **Escala del Plano:** Relación de conversión entre píxeles del lienzo y metros de la realidad ($\text{píxeles}/\text{metro}$).
14. **Laboratorio Libre (Free Lab):** Modo de Maplify donde el usuario puede arrastrar y reposicionar puntos libremente para ver el recálculo en tiempo real.
15. **Misión Guiada (Guided Mode):** Modo secuencial educativo obligatorio la primera vez, que orienta al usuario paso a paso en la carga y ubicación.
16. **Interferencia Cocanal (CCI):** Ocurre cuando dos redes operan en el mismo canal exacto.
17. **Canales No Solapados (2.4 GHz):** Exclusivamente los canales 1, 6 y 11.
18. **SheetJS (`XLSX`):** Librería en JavaScript vanilla utilizada para parsear el binario de Excel (`.xlsx`) en memoria del cliente sin servidor.
19. **Normalización de Coordenadas:** Transformación matemática entre el sistema de coordenadas del evento del ratón (`clientX, clientY`), el tamaño intrínseco de la imagen y el tamaño visual del canvas.
20. **Tasa de Refresco del Mapa:** El redibujado en Canvas debe optimizarse para no bloquear el hilo principal (Main Thread) del navegador en drag & drop.

---

## 2. Reglas de Dominio y Validación de Datos

### 2.1 Validación de Señal (RSSI en dBm)
* **Rango físico aceptable:** $[-95\text{ dBm}, -15\text{ dBm}]$.
  * Valores $> 0\text{ dBm}$ son físicamente imposibles para recepción WiFi en interiores $\to$ **Rechazar con error**.
  * Valores entre $[0\text{ dBm}, -15\text{ dBm}]$ indican proximidad peligrosa o error de sonda $\to$ **Advertir / Limitar**.
  * Valores $< -95\text{ dBm}$ caen bajo el piso de ruido térmico $\to$ Tratar como **"Sin señal"**.
* Si el archivo Excel contiene valores positivos (ej. $65$ en lugar de $-65$ por omisión del signo menos), la función normalizadora debe detectar si la columna es de RSSI y transformar automáticamente a negativo:
  ```javascript
  function normalizarRssi(valor) {
    let num = parseFloat(valor);
    if (isNaN(num)) return null;
    if (num > 0 && num <= 100) num = -num; // Corrección automática de signo
    if (num < -100 || num > -10) return null; // Fuera de rango físico
    return num;
  }
  ```

---

### 2.2 Especificación Exacta de la Interpolación IDW
La función matemática de interpolación en `app.html` debe cumplir rigurosamente:

$$\hat{z}(x, y) = \frac{\sum_{i=1}^{n} \frac{z_i}{d_i^2 + \epsilon}}{\sum_{i=1}^{n} \frac{1}{d_i^2 + \epsilon}}$$

* **Potencia:** $p = 2$ (cuadrático, emulando la física de dispersión $1/d^2$).
* **Épsilon ($\epsilon$):** Se agrega un valor mínimo $\epsilon = 0.0001$ en el denominador para prevenir división por cero cuando la coordenada evaluada $(x, y)$ coincide exactamente con un punto de medición $(x_i, y_i)$.
* **Radio de Corte ($R_{\text{corte}}$):** No calcular píxeles cuya distancia al punto de medición más cercano supere el umbral máximo de cobertura (configurable, por defecto $150\text{--}250\text{ px}$ o $4\text{--}6\text{ metros}$ escalados). Los píxeles fuera de rango mantienen canal alfa $= 0$.

---

### 2.3 Rampa Cromática Oficial de Maplify
Para mantener coherencia entre la visualización en pantalla, la leyenda y el manual, el gradiente debe respetar la siguiente correspondencia de colorimetría:

| Rango de RSSI (dBm) | Categoría Técnica | Color Hex | Color RGB | Opacidad (Alpha) |
|---|---|---|---|---|
| **$\ge -50\text{ dBm}$** | Excelente | `#1b5e20` (Verde oscuro) | `rgb(27, 94, 32)` | $0.65$ |
| **$-51\text{ a } -60\text{ dBm}$** | Buena | `#4caf50` (Verde medio) | `rgb(76, 175, 80)` | $0.65$ |
| **$-61\text{ a } -70\text{ dBm}$** | Aceptable | `#ffeb3b` (Amarillo) | `rgb(255, 235, 59)` | $0.65$ |
| **$-71\text{ a } -80\text{ dBm}$** | Débil | `#ff9800` (Naranja) | `rgb(255, 152, 0)` | $0.65$ |
| **$< -80\text{ dBm}$** | Muy débil / Borde | `#f44336` (Rojo) | `rgb(244, 67, 54)` | $0.65$ |
| **Sin cobertura / Lejos** | Fuera de rango | Transparente | `rgba(0, 0, 0, 0)` | $0.00$ |

---

### 2.4 Requerimientos del Parser de Excel
* Debe leer libros `.xlsx` usando `XLSX.read(data, {type: 'array'})`.
* Debe buscar una hoja llamada `"Mediciones"`, `"Relevamiento"` o procesar la primera hoja activa.
* Las columnas esperadas se detectan con coincidencia flexible insensible a mayúsculas/minúsculas y tildes:
  * **Identificador del punto:** `Punto`, `ID`, `Nombre`, `Muestra`.
  * **Nivel de señal:** `Señal`, `Senal`, `RSSI`, `dBm`, `Potencia`.
  * **Nombre de red (opcional):** `SSID`, `Red`, `Nombre Red`.
  * **Canal (opcional):** `Canal`, `Channel`.
* Si un punto en el Excel no tiene valor numérico válido de RSSI, se debe omitir el punto e informar al usuario en el panel de alertas sin romper la aplicación.

---

## 3. Restricciones Arquitecturales Inquebrantables

Cualquier agente que proponga o implemente cambios en el repositorio debe respetar los siguientes principios:

1. **Cero Dependencias Externas (Zero External Dependencies):**
   * No usar Node.js en runtime, npm, Vite, Webpack, React, Vue ni Tailwind.
   * La aplicación es **HTML5, CSS y JavaScript Vanilla puro**.
   * La única biblioteca permitida es **SheetJS** (`xlsx.full.min.js`), la cual debe residir localmente en `fuente/vendor/` y ser embebida por el script de compilación.
2. **Entregable en la Raíz Generado por Python:**
   * Nunca editar directamente `Maplify.html` ni `Manual.html`.
   * Los cambios se realizan en `fuente/app.html` o `fuente/manual.html`.
   * Para regenerar los entregables se ejecuta obligatoriamente:
     ```bash
     python fuente/construir.py
     ```
3. **Estilo de Código:**
   * CSS embebido dentro de etiquetas `<style>` en el mismo archivo.
   * Nombres de funciones y variables en `camelCase`.
   * Constantes en `UPPER_SNAKE_CASE`.
   * Comentarios y textos de interfaz en **español latinoamericano claro y accesible**.

---

## 4. Matriz de Casos Borde y Manejo de Errores

| Caso Borde | Causa Típica | Comportamiento Esperado del Sistema |
|---|---|---|
| **Menos de 3 puntos de medición** | El usuario subió un Excel incompleto o de prueba mínima. | Permitir ubicar los puntos pero mostrar un aviso didáctico: *"Se requieren al menos 3 puntos distribuidos para una interpolación representativa"*. |
| **Puntos superpuestos en la misma coordenada** | Doble clic por error del usuario en el lienzo. | Desplazar el nuevo punto $10\text{ px}$ hacia la derecha/abajo para permitir su selección y arrastre individual. |
| **Imagen de plano con dimensiones masivas (> 4K / 8K)** | Foto tomada directamente con teléfono móvil moderno. | El canvas debe escalar la imagen proporcionalmente manteniendo la relación de aspecto sin sobrepasar un ancho/alto máximo de renderizado de $2000\text{ px}$ para evitar congelamiento de memoria. |
| **Excel con valores de texto o nulos en dBm** | Celdas con `"N/A"`, `"Sin red"` o vacías. | Descartar la muestra no válida y notificar: *"Se omitió el punto X por no contener un valor numérico de señal"*. |
| **Plano no cargado pero Excel importado** | Secuencia de pasos alterada por el usuario en modo libre. | Bloquear la fase de ubicación en el canvas hasta que exista una imagen de plano válida en memoria. |
