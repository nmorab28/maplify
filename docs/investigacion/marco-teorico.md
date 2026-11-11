# Marco Teórico: Auditoría de Cobertura Inalámbrica (Site Survey WiFi) e Interpolación Geoespacial de Radiofrecuencia

**Proyecto de Grado / Final:** Maplify — Sistema Web de Generación de Mapas de Calor para Site Survey WiFi  
**Institución:** Universidad El Bosque — Facultad de Ingeniería  
**Asignatura:** Redes de Datos II  
**Autores / Investigadores:** Nicolás Mora y equipo de trabajo  
**Fecha:** Noviembre de 2026  

---

## Resumen Ejecutivo

El presente marco teórico compila los principios fundamentales de física de ondas electromagnéticas, ingeniería de telecomunicaciones y modelado geoespacial requeridos para la comprensión, diseño e implementación del software **Maplify**. Se analizan las bases matemáticas de la propagación de radiofrecuencia en interiores, la evolución del estándar IEEE 802.11, la metodología estandarizada por organismos internacionales (CWNP, Cisco, Wi-Fi Alliance) para el levantamiento de sitio (*Site Survey*), y los algoritmos deterministas de interpolación espacial basados en la Inversa de la Distancia Ponderada (IDW) para la representación bidimensional de campos continuos de intensidad de señal (RSSI).

---

## 1. Fundamentos de Radiofrecuencia y Propagación en Espacios Confinados

### 1.1 Naturaleza de las Ondas Electromagnéticas y Magnitudes de Potencia

Las redes de área local inalámbricas (WLAN) operan mediante la radiación y recepción de ondas electromagnéticas generadas por la oscilación de corrientes de alta frecuencia en elementos radiantes (antenas). La potencia radiada por un transmisor inalámbrico disminuye drásticamente a medida que la onda se expande en el espacio tridimensional.

Dado que la potencia recibida en el extremo cliente es extremadamente pequeña comparada con la potencia emitida por el Punto de Acceso (AP), se emplea la escala logarítmica de decibelios referenciada a un milivatio (**dBm**). La conversión entre la escala lineal en milivatios ($P_{\text{mW}}$) y la escala logarítmica ($P_{\text{dBm}}$) se rige por:

$$P_{\text{dBm}} = 10 \cdot \log_{10}(P_{\text{mW}})$$

$$P_{\text{mW}} = 10^{\frac{P_{\text{dBm}}}{10}}$$

#### Ejemplos de correspondencia física:
* $+20\text{ dBm} = 100\text{ mW}$ (Potencia típica de transmisión de un AP empresarial).
* $0\text{ dBm} = 1\text{ mW}$.
* $-30\text{ dBm} = 0.001\text{ mW} = 1\text{ }\mu\text{W}$ (Señal muy fuerte, a menos de un metro del AP).
* $-67\text{ dBm} = 0.0000001995\text{ mW} \approx 0.2\text{ nW}$ (Límite estándar de diseño para voz y video).
* $-90\text{ dBm} = 0.000000001\text{ mW} = 1\text{ pW}$ (Límite de sensibilidad del receptor; borde de desconexión).

La relación de potencias relativas obedece a la **Regla del 3 y del 10**:
* Un incremento de $+3\text{ dB}$ duplica la potencia lineal ($2\times$).
* Una reducción de $-3\text{ dB}$ reduce la potencia lineal a la mitad ($0.5\times$).
* Un incremento de $+10\text{ dB}$ multiplica la potencia por diez ($10\times$).
* Una reducción de $-10\text{ dB}$ divide la potencia entre diez ($0.1\times$).

---

### 1.2 Modelos Matemáticos de Pérdida por Trayectoria (Path Loss)

#### A. Pérdida de Trayectoria en Espacio Libre (Free Space Path Loss - FSPL)
En condiciones ideales de espacio libre (vacío, sin obstáculos ni reflexiones), la densidad de potencia de una onda esférica decrece con el cuadrado de la distancia, según la ley del inverso del cuadrado. La ecuación fundamental de transmisión de Friis y la formulación estándar de la UIT-R P.525 definen el FSPL como:

$$\text{FSPL} = \left(\frac{4\pi d}{\lambda}\right)^2 = \left(\frac{4\pi d f}{c}\right)^2$$

Expresada en escala logarítmica (dB) en función de la distancia $d$ (en metros) y la frecuencia $f$ (en Hertz):

$$\text{FSPL}_{\text{dB}} = 20\log_{10}(d) + 20\log_{10}(f) - 147.55$$

Para propósitos de ingeniería de redes WiFi, usando la distancia $d$ en metros y la frecuencia $f$ en Megahertz (MHz):

$$\text{FSPL}_{\text{dB}} = 20\log_{10}(d_{\text{m}}) + 20\log_{10}(f_{\text{MHz}}) - 27.55$$

**Cálculo comparativo a 1 metro de distancia:**
* A $2.437\text{ GHz}$ (Canal 6, $2437\text{ MHz}$):
  $$\text{FSPL} = 20\log_{10}(1) + 20\log_{10}(2437) - 27.55 \approx 40.2\text{ dB}$$
* A $5.180\text{ GHz}$ (Canal 36, $5180\text{ MHz}$):
  $$\text{FSPL} = 20\log_{10}(1) + 20\log_{10}(5180) - 27.55 \approx 46.7\text{ dB}$$

Nótese que la banda de $5\text{ GHz}$ sufre aproximadamente $6.5\text{ dB}$ adicionales de atenuación en el primer metro respecto a $2.4\text{ GHz}$, lo que significa que la señal recibida es más de 4 veces inferior en potencia únicamente debido a la frecuencia portadora.

#### B. Modelo de Pérdida Log-Distancia (Log-Distance Path Loss Model)
En interiores, la propagación se desvía del espacio libre debido a la presencia de límites físicos. El modelo empírico log-distancia incorpora el exponente de atenuación de trayectoria ($n$):

$$PL(d) = PL(d_0) + 10 \cdot n \cdot \log_{10}\left(\frac{d}{d_0}\right) + X_\sigma$$

donde:
* $d_0$ es la distancia de referencia (usualmente $1\text{ m}$).
* $n$ es el exponente empírico de pérdida de trayectoria dependiente del entorno:
  * $n = 2.0$: Espacio libre.
  * $n = 1.6\text{--}1.8$: Pasillos largos (efecto guía de onda).
  * $n = 2.8\text{--}3.5$: Edificios de oficinas comerciales y aulas universitarias con divisiones estándar.
  * $n = 4.0\text{--}6.0$: Entornos industriales densos o edificaciones con muros macizos de concreto.
* $X_\sigma$ es una variable aleatoria gaussiana de media cero con desviación estándar $\sigma$ en dB, que modela el desvanecimiento lento por sombra (*shadowing* o efecto de pared).

#### C. Modelo de Atenuación de Interiores de la UIT (ITU Indoor Model / ITU-R P.1238)
La Recomendación UIT-R P.1238 formaliza las pérdidas en interiores considerando la penetración entre plantas o pisos:

$$L_{\text{total}} = 20\log_{10}(f) + N \cdot \log_{10}(d) + L_f(n) - 28$$

donde $N$ es el coeficiente de pérdida de potencia por distancia (típicamente $28\text{--}31$ en oficinas para $2.4\text{ GHz}$ y $5\text{ GHz}$) y $L_f(n)$ es el factor de penetración estructural entre pisos ($n$ pisos atravesados).

---

### 1.3 Interacción de las Ondas con Materiales Constructivos

Cuando una onda de radiofrecuencia impacta un obstáculo constructivo, la energía incidente se divide en tres componentes: onda reflejada, onda absorbida (disipada en calor) y onda transmitida (atenuada).

| Material Constructivo | Espesor Típico | Atenuación en 2.4 GHz (dB) | Atenuación en 5 GHz (dB) | Impacto Práctico en Cobertura |
|---|---|---|---|---|
| **Tabique de yeso / Drywall** | $10\text{ cm}$ | $2\text{--}3\text{ dB}$ | $3\text{--}5\text{ dB}$ | Mínimo; la señal atraviesa 2 a 3 muros sin caer de umbral. |
| **Vidrio claro convencional** | $6\text{ mm}$ | $2\text{--}3\text{ dB}$ | $4\text{--}6\text{ dB}$ | Bajo; permite cobertura fluida entre oficinas con mamparas. |
| **Vidrio tintado / Térmico (Low-E)** | $12\text{ mm}$ | $6\text{--}10\text{ dB}$ | $10\text{--}15\text{ dB}$ | Medio a alto; el óxido metálico refleja la señal fuertemente. |
| **Madera maciza / Puerta pesada** | $4\text{--}5\text{ cm}$ | $3\text{--}5\text{ dB}$ | $6\text{--}8\text{ dB}$ | Moderado. |
| **Ladrillo hueco tradicional** | $15\text{ cm}$ | $5\text{--}8\text{ dB}$ | $9\text{--}13\text{ dB}$ | Significativo; requiere planificación de celdas por estancia. |
| **Concreto / Hormigón reforzado** | $20\text{ cm}$ | $12\text{--}18\text{ dB}$ | $18\text{--}28\text{ dB}$ | Muy severo; reduce drásticamente el radio de celda. |
| **Estructuras metálicas / Ascensores** | Variable | $> 30\text{ dB}$ | $> 35\text{ dB}$ | Bloqueo absoluto (Jaula de Faraday); sombra total. |
| **Cuerpo humano / Multitudes** | 1 persona | $2\text{--}4\text{ dB}$ | $3\text{--}6\text{ dB}$ | Crítico en auditorios; la atenuación aumenta con la densidad. |

*Fuentes: NIST Technical Note 1396; Cisco Systems WLAN Design Guide; CWDP Certified Wireless Design Professional.*

---

## 2. El Estándar IEEE 802.11 y Generaciones WiFi

### 2.1 Evolución Histórica y Parámetros Técnicos

La familia de normas IEEE 802.11 gobierna las especificaciones de Capa Física (PHY) y de Control de Acceso al Medio (MAC) para redes locales inalámbricas.

| Generación | Enmienda IEEE | Año de Aprobación | Bandas de Operación | Modulación Máxima | Anchos de Canal (MHz) | Rendimiento Físico Teórico Máximo |
|---|---|---|---|---|---|---|
| **Wi-Fi 1** | 802.11b | 1999 | $2.4\text{ GHz}$ | DSSS / CCK | 20 | $11\text{ Mbps}$ |
| **Wi-Fi 2** | 802.11a | 1999 | $5\text{ GHz}$ | OFDM (64-QAM) | 20 | $54\text{ Mbps}$ |
| **Wi-Fi 3** | 802.11g | 2003 | $2.4\text{ GHz}$ | ERP-OFDM (64-QAM) | 20 | $54\text{ Mbps}$ |
| **Wi-Fi 4** | 802.11n | 2009 | $2.4 / 5\text{ GHz}$ | HT-OFDM (64-QAM, MIMO 4x4) | 20, 40 | $600\text{ Mbps}$ |
| **Wi-Fi 5** | 802.11ac | 2013 | $5\text{ GHz}$ | VHT-OFDM (256-QAM, MU-MIMO 8x8) | 20, 40, 80, 160 | $6.93\text{ Gbps}$ |
| **Wi-Fi 6 / 6E** | 802.11ax | 2021 | $2.4 / 5 / 6\text{ GHz}$ | OFDMA (1024-QAM, Target Wake Time) | 20, 40, 80, 160 | $9.6\text{ Gbps}$ |
| **Wi-Fi 7** | 802.11be | 2024 | $2.4 / 5 / 6\text{ GHz}$ | 4096-QAM, MLO (Multi-Link Operation) | 20 hasta 320 | $46.1\text{ Gbps}$ |

---

### 2.2 Gestión del Espectro y Distribución de Canales

#### A. Banda de 2.4 GHz (ISM: 2400 – 2483.5 MHz)
En la banda de $2.4\text{ GHz}$, el espectro total disponible es de solo $83.5\text{ MHz}$. Cada canal estándar tiene un ancho espectral de $20\text{ MHz}$ (con faldones que se extienden hasta $22\text{ MHz}$), pero las frecuencias centrales están espaciadas a solo $5\text{ MHz}$ de distancia (del canal 1 al canal 13/14).

Por este motivo, para evitar la **Interferencia de Canal Adyacente (ACI)**, el diseño de ingeniería exige utilizar exclusivamente el esquema de **tres canales ortogonales (no solapados)**:
* **Canal 1:** $2412\text{ MHz}$ (abarca $2401\text{--}2423\text{ MHz}$).
* **Canal 6:** $2437\text{ MHz}$ (abarca $2426\text{--}2448\text{ MHz}$).
* **Canal 11:** $2462\text{ MHz}$ (abarca $2451\text{--}2473\text{ MHz}$).

El uso indebido de canales intermedios (como el 2, 3, 4 o 9) contamina dos celdas limpias a la vez, deteriorando el rendimiento global por ruido no sincronizado.

#### B. Banda de 5 GHz (UNII: 5150 – 5850 MHz)
Ofrece hasta 25 canales ortogonales de $20\text{ MHz}$ sin solapamiento:
* **UNII-1 (Canales 36, 40, 44, 48):** $5150\text{--}5250\text{ MHz}$ (Uso prioritario en interiores).
* **UNII-2A / DFS (Canales 52, 56, 60, 64):** $5250\text{--}5350\text{ MHz}$ (Sujeto a detección de radar meteorológico).
* **UNII-2C Extendida / DFS (Canales 100 al 144):** $5470\text{--}5725\text{ MHz}$.
* **UNII-3 (Canales 149, 153, 157, 161, 165):** $5725\text{--}5850\text{ MHz}$.

---

### 2.3 Mecanismo de Acceso al Medio CSMA/CA y Contienda

A diferencia de las redes cableadas Ethernet (IEEE 802.3) que usan detección de colisiones (CSMA/CD), los transceptores de radiofrecuencia son **Half-Duplex**: la potencia de su propia transmisión satura de inmediato el receptor, impidiendo detectar colisiones en el aire de forma simultánea.

Por ello, 802.11 implementa **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)**:
1. **Detección de Portadora Física (Clear Channel Assessment - CCA):** La radio evalúa la energía de RF en el canal. Si detecta preámbulos WiFi a $\ge -82\text{ dBm}$ o energía no-WiFi a $\ge -62\text{ dBm}$, declara el canal ocupado.
2. **Detección de Portadora Virtual (Network Allocation Vector - NAV):** Campos de duración incluidos en las cabeceras de las tramas indican a las estaciones cuánto tiempo deben permanecer en silencio.
3. **Random Backoff:** Si el medio está ocupado, las estaciones eligen un número aleatorio de ranuras de tiempo (*slot times*) en una ventana de contienda ($CW_{\text{min}}$ a $CW_{\text{max}}$) y decrementan el contador solo cuando el medio se encuentra desocupado durante un espacio inter-trama (DIFS/AIFS).

**Consecuencia para el Site Survey:** Cuando múltiples APs operan en el mismo canal (**Interferencia Cocanal - CCI**), no colisionan caóticamente; en su lugar, se escuchan mutuamente y se turnan el tiempo de transmisión (*Airtime*). Por ende, el rendimiento real cae a la fracción del número de APs contendientes.

---

## 3. Metodología de Site Survey (Levantamiento de Sitio)

### 3.1 Taxonomía de Levantamientos

Siguiendo el estándar de la **CWNP (Certified Wireless Network Professionals)** y las guías de diseño de **Cisco (CVD)**, se reconocen tres tipos de levantamiento de sitio:

```
┌─────────────────────────────────────────────────────────────┐
│                  METODOLOGÍAS DE SITE SURVEY                │
├─────────────────┬─────────────────────────┬─────────────────┤
│   PREDICTIVO    │         PASIVO          │     ACTIVO      │
├─────────────────┼─────────────────────────┼─────────────────┤
│ Simulación CAD  │ Escucha de Beacons/ACKs │ Asociación a AP │
│ Trazado rayos   │ Todos los SSIDs/BSSIDs  │ Ping / iPerf    │
│ Sin hardware RF │ RSSI, SNR, Canales, CCI │ Throughput real │
│ Fase de diseño  │ Auditoría de cobertura  │ Validación SLA  │
└─────────────────┴─────────────────────────┴─────────────────┘
```

1. **Site Survey Predictivo (Virtual / Simulado):**
   * Se ejecuta mediante software de modelado 3D (ej. Ekahau AI Pro, Hamina Wireless).
   * Se importan planos vectoriales, se definen las propiedades dieléctricas de las paredes y se ubican APs virtuales según patrones de radiación de antenas.
   * **Objetivo:** Estimar la cantidad y posición preliminar de APs antes de la compra o construcción.
2. **Site Survey Pasivo (Passive Survey):**
   * El auditor camina por las instalaciones con una tarjeta de red (NIC) en modo monitor.
   * El adaptador no se asocia a ninguna red; barre cíclicamente los canales escuchando tramas baliza (*Beacons*) y respuestas de sondeo (*Probe Responses*).
   * **Datos recopilados:** RSSI de cada BSSID detectado, canal, SSID, SNR, piso de ruido y tasa de beacons.
   * **Objetivo:** Mapear la huella electromagnética real de todo el espectro presente.
3. **Site Survey Activo (Active Survey):**
   * El adaptador se asocia a un SSID y BSSID particular.
   * Se transmiten paquetes de prueba bidireccionales continuos hacia un servidor de prueba (iPerf o sonda de red).
   * **Datos recopilados:** Tasa de datos negociada (MCS), pérdida porcentual de paquetes, latencia de ida y vuelta (RTT) y jitter.
   * **Objetivo:** Evaluar la experiencia de usuario real de un cliente conectado.

---

### 3.2 Criterios y Umbrales de Calidad de Señal

Para un diseño moderno que soporte aplicaciones empresariales (datos de alta velocidad, streaming 4K y llamadas de Voz sobre WiFi / Roaming continuo), los umbrales estandarizados de la industria son:

| Rango de RSSI (dBm) | Calidad de Señal | Experiencia de Usuario | Modulación Esperada (MCS) |
|---|---|---|---|
| **$\ge -50\text{ dBm}$** | Excelente / Máxima | Velocidad teórica máxima; latencia $< 2\text{ ms}$; sin retransmisiones. | Modulaciones máximas (1024-QAM / 4096-QAM). |
| **$-51\text{ a } -60\text{ dBm}$** | Muy Buena | Rendimiento óptimo para transferencia masiva de archivos y videoconferencia fluida. | 256-QAM / 1024-QAM. |
| **$-61\text{ a } -70\text{ dBm}$** | Aceptable / Adecuada | Navegación web estándar y streaming en buffer. Límite de diseño para voz corporativa ($-67\text{ dBm}$). | 64-QAM / 16-QAM. |
| **$-71\text{ a } -80\text{ dBm}$** | Débil / Marginal | Lentitud perceptible; degradación en llamadas de audio; retransmisiones elevadas. | QPSK / BPSK. |
| **$< -80\text{ dBm}$** | Sin Cobertura Útil / Crítica | Desconexión frecuente; pérdida masiva de tramas; imposibilidad de asociar. | Desasociación por timeout. |

#### El Criterio de Roaming Transparente ($-67\text{ dBm}$ / $20\%\text{ Overlap}$)
La recomendación universal de **Cisco CVD** y **Apple iOS Roaming Specification** establece que un cliente móvil inicia el escaneo de canales para buscar un mejor AP cuando su señal actual cae por debajo de $-67\text{ dBm}$. Por ende:
* En los límites de cada celda, la señal no debe caer de $-67\text{ dBm}$ antes de que la celda vecina entregue también al menos $-67\text{ dBm}$.
* El solapamiento físico (*overlap*) entre celdas vecinas debe ubicarse entre el $15\%$ y el $20\%$ del área de cobertura en pasillos y zonas de tránsito.

---

## 4. Mapas de Calor y Algoritmos de Interpolación Espacial

### 4.1 Concepto de Mapa de Calor de Radiofrecuencia

Un mapa de calor de cobertura WiFi es un modelo raster continuo bidimensional $f(x, y) \to \text{RSSI}$ proyectado sobre el espacio planar de un mapa arquitectónico. Dado que es físicamente inviable tomar mediciones en cada centímetro cuadrado de un edificio, se recopilan $N$ muestras discretas y dispersas en puntos de coordenadas conocidas $(x_i, y_i)$ y se utiliza **interpolación espacial geoestadística** para estimar la señal en todas las coordenadas no muestreadas.

---

### 4.2 Interpolación por Inversa de la Distancia Ponderada (IDW)

El algoritmo de **Inversa de la Distancia Ponderada (IDW / Inverse Distance Weighting)** es el método determinista más extendido en aplicaciones de site survey ligeras debido a su balance óptimo entre precisión predictiva, estabilidad matemática y bajo costo computacional en navegadores web.

#### Formulación Matemática
Dado un conjunto de $N$ puntos de control conocidos con coordenadas $(x_i, y_i)$ y valores de señal $z_i = \text{RSSI}(x_i, y_i)$, el valor estimado $\hat{z}$ en cualquier punto arbitrario $(x, y)$ se calcula mediante una combinación lineal ponderada:

$$\hat{z}(x, y) = \frac{\sum_{i=1}^{N} w_i(x, y) \cdot z_i}{\sum_{i=1}^{N} w_i(x, y)}$$

donde el peso $w_i(x, y)$ asignado a la muestra $i$-ésima es el inverso de la distancia euclidiana elevado a una potencia $p$:

$$w_i(x, y) = \frac{1}{\left(d_i(x, y)\right)^p}$$

$$d_i(x, y) = \sqrt{(x - x_i)^2 + (y - y_i)^2}$$

#### Propiedades y Parámetros del IDW:
1. **Parámetro de Potencia ($p$):**
   * Controla la tasa de decaimiento del peso con la distancia.
   * Con $p = 1$, la interpolación es suave y los puntos lejanos ejercen influencia considerable.
   * Con $p = 2$ (**IDW estándar cuadrático**), la tasa de decaimiento coincide conceptualmente con la ley física de propagación de la potencia en espacio libre ($1/d^2$), otorgando un comportamiento físico verosímil.
   * Con $p \ge 3$, el valor interpolado colapsa rápidamente hacia el vecino más cercano (*Nearest Neighbor*).
2. **Propiedad de Exactitud:** Si $(x, y) = (x_i, y_i)$, la distancia $d_i = 0$. Matemáticamente se evalúa:
   $$\lim_{(x, y) \to (x_i, y_i)} \hat{z}(x, y) = z_i$$
   El algoritmo honra exactamente los datos muestreados en los puntos de control, sin distorsión ni sesgo.
3. **Radio de Influencia (Corte por Distancia $R_{\text{max}}$):**
   En radiofrecuencia indoor, una medición tomada a más de $15\text{--}20\text{ metros}$ separada por paredes no debe influir en una celda remota. Por ende, se implementa una función de soporte compacto:
   $$w_i(x, y) = \begin{cases} \frac{1}{d_i^p} & \text{si } d_i \le R_{\text{max}} \\ 0 & \text{si } d_i > R_{\text{max}} \end{cases}$$
   Si todas las distancias superan $R_{\text{max}}$, el píxel se deja transparente o blanco, denotando *"zona no auditada / fuera de rango"*.

---

### 4.3 Comparación de Métodos de Interpolación Espacial

| Algoritmo | Complejidad Computacional | Ventajas Principales | Desventajas / Limitaciones | Idoneidad para Maplify |
|---|---|---|---|---|
| **IDW (Inverse Distance Weighting)** | $O(N)$ por píxel | Determinista, exacto en los puntos, rápido en JavaScript, reproduce el decaimiento $1/d^2$. | Puede generar efecto de "ojo de buey" (*bull's eye*) alrededor de puntos aislados. | **Excelente (Método elegido)**: Se ejecuta en tiempo real en canvas sin librerías pesadas. |
| **Kriging (Ordinario / Universal)** | $O(N^3)$ global por inversión de matrices | Proporciona estimación de varianza e incertidumbre; modela tendencias geoestadísticas espaciales. | Exige cálculo previo de semivariograma; alto consumo de CPU y memoria; inviable en JS básico. | No recomendado para aplicaciones autocontenidas de navegador. |
| **Nearest Neighbor (Polígonos de Voronoi)** | $O(N)$ por píxel | Ultrarrápido; no inventa datos intermedios. | Representación escalonada y facetada; no refleja gradientes suaves de radiofrecuencia. | Deficiente para visualización de cobertura. |
| **Spline / Thin Plate** | $O(N^3)$ | Superficie suave y continua con derivadas continuas. | Puede predecir valores mayores al máximo o menores al mínimo observado (oscilaciones espurias). | Regular; puede extrapolar dBm imposibles. |

---

### 4.4 Colorimetría y Mapeo Gradual de Señal

Para facilitar la interpretación intuitiva, los valores cuantitativos de RSSI interpolados en dBm se mapean a una rampa cromática de cuatro o cinco tonos normalizados:

```
Mejor Señal ◄────────────────────────────────────────► Peor Señal
[-30 a -50 dBm]    [-51 a -65 dBm]    [-66 a -75 dBm]    [< -75 dBm]
 Verde Oscuro        Verde Claro          Amarillo           Rojo
  (Excelente)           (Bueno)          (Aceptable)       (Crítico)
```

En la renderización sobre Canvas HTML5, el valor interpolado $\hat{z}$ se evalúa mediante interpolación lineal de los componentes RGB con un canal alfa de opacidad ($60\%\text{--}75\%$) que permite visualizar nítidamente las líneas de las paredes del plano arquitectónico subyacente.

---

## 5. Marco Regulatorio y Gestión del Espectro Radioeléctrico

### 5.1 Normativa Internacional (UIT) y Regional (FCC / ETSI)

La **Unión Internacional de Telecomunicaciones (UIT)** a través de sus Conferencias Mundiales de Radiocomunicaciones (CMR) categoriza el espectro inalámbrico. Las redes WLAN operan en bandas de radiocomunicación exentas de licencia individual (*License-Exempt* o de uso no privativo), supeditadas al principio de **no causar interferencias perjudiciales a servicios primarios** y **no reclamar protección frente a interferencias de otros servicios autorizados**.

* **FCC (Estados Unidos / Región 2):**
  * Permite canales 1 al 11 en $2.4\text{ GHz}$.
  * Potencia máxima conducida al transmisor: hasta $1000\text{ mW}$ ($30\text{ dBm}$), con un EIRP máximo de $4000\text{ mW}$ ($36\text{ dBm}$) con antena omnidireccional de $6\text{ dBi}$.
* **ETSI (Europa / Región 1):**
  * Permite canales 1 al 13 en $2.4\text{ GHz}$.
  * Límite estricto de EIRP a $100\text{ mW}$ ($20\text{ dBm}$) en $2.4\text{ GHz}$ y $200\text{ mW}$ ($23\text{ dBm}$) en $5\text{ GHz}$ (UNII-1).

---

### 5.2 Normativa Nacional en Colombia (MINTIC, CRC y ANE)

En la República de Colombia, la administración y control del espectro radioeléctrico está regulada por la **Agencia Nacional del Espectro (ANE)** y la **Comisión de Regulación de Comunicaciones (CRC)**:

1. **Resolución ANE 105 de 2020 (y actualizaciones 737 de 2021):**
   * Clasifica las bandas de $2400\text{--}2483.5\text{ MHz}$, $5150\text{--}5250\text{ MHz}$, $5250\text{--}5350\text{ MHz}$, $5470\text{--}5725\text{ MHz}$ y $5725\text{--}5850\text{ MHz}$ como **bandas de uso libre** para aplicaciones de sistemas de acceso inalámbrico (WAS) y redes radioeléctricas de área local (RLAN).
   * **Potencia máxima permitida en interiores:**
     * En $2.4\text{ GHz}$: Potencia pico máxima de salida del transmisor de $1\text{ W}$ ($30\text{ dBm}$) con ganancia de antena directiva de hasta $6\text{ dBi}$ (PIRE máxima de $36\text{ dBm}$).
     * En $5\text{ GHz}$ (banda baja 5150–5250 MHz): PIRE máxima restringida a $200\text{ mW}$ ($23\text{ dBm}$) con densidad espectral de potencia controlada para uso estrictamente en interiores.
2. **Apertura de la Banda de 6 GHz en Colombia (Resolución ANE 737 de 2021):**
   * Colombia habilitó los $1200\text{ MHz}$ completos de la banda de $6\text{ GHz}$ ($5925\text{--}7125\text{ MHz}$) para operación de baja potencia en interiores (LPI - Low Power Indoor) con PIRE máxima de $30\text{ dBm}$ ($1\text{ W}$), posicionando al país a la vanguardia de la adopción de **Wi-Fi 6E y Wi-Fi 7**.

---

## 6. Referencias Bibliográficas

1. **IEEE Standards Association.** (2021). *IEEE Std 802.11-2020: IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems - Local and Metropolitan Area Networks—Specific Requirements - Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications*. IEEE. https://doi.org/10.1109/IEEESTD.2021.9363693
2. **Coleman, D. X., & Westcott, D. D.** (2021). *CWNA Certified Wireless Network Administrator Study Guide: Exam CWNA-108* (6th ed.). Sybex / John Wiley & Sons.
3. **Jackman, S. M., Swartz, M., Smith, B. E., & Carter, M. E.** (2014). *CWDP Certified Wireless Design Professional Official Study Guide: Exam PW0-250*. John Wiley & Sons.
4. **Cisco Systems Inc.** (2020). *Enterprise Mobility 8.5 Design Guide: Cisco Validated Design (CVD)*. Cisco Systems Official Documentation.
5. **Rappaport, T. S.** (2002). *Wireless Communications: Principles and Practice* (2nd ed.). Prentice Hall Communications Engineering and Emerging Technologies Series.
6. **International Telecommunication Union (ITU-R).** (2019). *Recommendation ITU-R P.1238-10: Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz*. ITU Radiocommunication Sector.
7. **International Telecommunication Union (ITU-R).** (2019). *Recommendation ITU-R P.525-4: Calculation of free-space attenuation*. ITU Radiocommunication Sector.
8. **Shepard, D.** (1968). A two-dimensional interpolation function for irregularly-spaced data. *Proceedings of the 1968 23rd ACM National Conference*, 517–524. https://doi.org/10.1145/800186.810616
9. **Gast, M. S.** (2005). *802.11 Wireless Networks: The Definitive Guide* (2nd ed.). O'Reilly Media.
10. **Ekahau Inc.** (2023). *Wi-Fi Site Survey Guidelines: Best Practices for Pre- and Post-Deployment Surveys*. Ekahau Technical White Papers.
11. **Agencia Nacional del Espectro (ANE).** (2021). *Resolución 737 de 2021: Por la cual se actualiza el Cuadro Nacional de Atribución de Bandas de Frecuencias (CNABF) y se adoptan medidas para el uso libre de la banda de 6 GHz en Colombia*. Ministerio de Tecnologías de la Información y las Comunicaciones (MinTIC), República de Colombia.
12. **National Institute of Standards and Technology (NIST).** (1997). *Electromagnetic Signal Attenuation in Construction Materials* (NIST Technical Note 1396). U.S. Department of Commerce.
