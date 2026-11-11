# Glosario Técnico de Redes Inalámbricas y Site Survey WiFi

**Proyecto:** Maplify — Sistema Web de Generación de Mapas de Calor para Site Survey WiFi  
**Institución:** Universidad El Bosque — Facultad de Ingeniería  
**Materia:** Redes de Datos II  
**Destinatarios:** Equipo de desarrollo (Ingeniería de Software / Redes) y Agentes de IA (Harness de Contexto)  

---

## Introducción

Este glosario técnico compila la terminología formal de telecomunicaciones, radiofrecuencia (RF) e ingeniería de redes inalámbricas aplicada a las auditorías de cobertura (*Site Survey*) y a la interpolación espacial de señales. Las definiciones han sido estandarizadas siguiendo las pautas de **IEEE (Institute of Electrical and Electronics Engineers)**, **CWNP (Certified Wireless Network Professional)**, **Cisco Validated Designs (CVD)** y la **UIT (Unión Internacional de Telecomunicaciones)**.

---

## Catálogo de Términos

### 1. RSSI (Received Signal Strength Indicator)
* **Definición técnica:** Parámetro relativo de medición de la potencia de una señal de radiofrecuencia recibida por una interfaz de red inalámbrica (NIC). Aunque el estándar IEEE 802.11 define el RSSI como un valor entero de 1 byte sin unidades estandarizadas entre fabricantes, en la práctica y en sistemas operativos modernos (Linux, Windows, Android) se mapea directamente a valores absolutos de potencia en dBm.
* **Unidad de medida:** Entero arbitrario (0–255 según estándar); comúnmente normalizado a **dBm**.
* **Rango típico en interiores:** $-30\text{ dBm}$ (muy cerca del AP) a $-90\text{ dBm}$ (límite de desasociación).
* **Relevancia para Maplify:** Es la variable escalar cuantitativa fundamental leída de las hojas de Excel para calcular e interpolar el mapa de cobertura.
* **Fuente:** IEEE Std 802.11-2020; CWNA Official Study Guide (Capítulo 3).

---

### 2. dBm (Decibel-milivatio)
* **Definición técnica:** Unidad logarítmica de potencia de radiofrecuencia referenciada a un milivatio ($1\text{ mW}$). Se expresa mediante la relación matemática:
  $$P_{\text{dBm}} = 10 \cdot \log_{10}\left(\frac{P_{\text{mW}}}{1\text{ mW}}\right)$$
  Permite manejar rangos dinámicos muy amplios sin usar decimales infinitesimales de vatios.
* **Unidad de medida:** dBm (decibel relativo a 1 mW).
* **Rango típico en interiores:**
  * Potencia de transmisión de AP: $+10\text{ dBm}$ a $+23\text{ dBm}$ ($10\text{ mW}$ a $200\text{ mW}$).
  * Señal recibida por cliente: $-35\text{ dBm}$ a $-85\text{ dBm}$.
* **Relevancia para Maplify:** Escala estándar en la que el usuario ingresa sus mediciones y sobre la cual opera el gradiente cromático del mapa de calor.
* **Fuente:** ITU-R V.574; CWDP Official Study Guide.

---

### 3. EIRP (Equivalent Isotropically Radiated Power / Potencia Isótropa Radiada Equivalente - PIRE)
* **Definición técnica:** Potencia total que emitiría una antena isotrópica ideal en su dirección de máxima ganancia para generar la misma intensidad de campo que la antena real del dispositivo. Se calcula sumando la potencia del transmisor ($P_{\text{tx}}$ en dBm), restando las pérdidas en conectores/cables ($L_{\text{cable}}$ en dB) y sumando la ganancia de la antena ($G_{\text{ant}}$ en dBi):
  $$\text{EIRP} = P_{\text{tx}} - L_{\text{cable}} + G_{\text{ant}}$$
* **Unidad de medida:** dBm (o vatios).
* **Rango típico en interiores:** En Colombia (regulación CRC/MINTIC) y FCC se limita habitualmente a un máximo de $+30\text{ dBm}$ ($1\text{ W}$) a $+36\text{ dBm}$ ($4\text{ W}$) según la banda y uso.
* **Relevancia para Maplify:** Define el punto de origen de propagación y la potencia esperada al momento de evaluar el dimensionamiento y cumplimiento normativo de un AP.
* **Fuente:** UIT-R SM.329; Comisión de Regulación de Comunicaciones (CRC).

---

### 4. Path Loss (Pérdida por Trayectoria)
* **Definición técnica:** Atenuación media acumulada de la densidad de potencia de una onda electromagnética a medida que se propaga por el espacio desde la antena transmisora hasta la receptora, ocasionada por dispersión geométrica, absorción atmosférica y reflexión.
* **Unidad de medida:** Decibelios (dB).
* **Rango típico en interiores:** $40\text{ dB}$ (en el primer metro a 2.4 GHz) hasta $85\text{--}100\text{ dB}$ atravesando múltiples paredes a 20 metros.
* **Relevancia para Maplify:** Justifica teóricamente por qué los puntos más distantes del AP experimentan caídas drásticas de señal, y fundamenta el factor de decaimiento en la interpolación.
* **Fuente:** Rappaport, T. S. *Wireless Communications: Principles and Practice*; Cisco Mobility Design Guide.

---

### 5. Atenuación (Attenuation)
* **Definición técnica:** Reducción en la amplitud e intensidad de la señal electromagnética al penetrar o chocar contra medios materiales densos (paredes, puertas, cristales, estructuras metálicas, mobiliario y personas).
* **Unidad de medida:** Decibelios (dB).
* **Rango típico en interiores:**
  * Pared de drywall/yeso: $2\text{--}4\text{ dB}$
  * Pared de ladrillo tradicional: $6\text{--}10\text{ dB}$
  * Vidrio laminado/térmico: $8\text{--}14\text{ dB}$
  * Concreto reforzado: $12\text{--}25\text{ dB}$
  * Metal/Ascensores: $>30\text{ dB}$ (bloqueo casi total)
* **Relevancia para Maplify:** Explica las sombras de cobertura y caídas abruptas de señal entre áreas contiguas en el plano arquitectónico.
* **Fuente:** CWDP Study Guide; NIST Technical Note 1396.

---

### 6. SNR (Signal-to-Noise Ratio / Relación Señal a Ruido)
* **Definición técnica:** Diferencia logarítmica entre la potencia de la señal útil recibida y el nivel de ruido de fondo de radiofrecuencia (Noise Floor):
  $$\text{SNR}_{\text{dB}} = \text{Señal}_{\text{dBm}} - \text{Ruido}_{\text{dBm}}$$
  Es el factor determinante primordial de la tasa de modulación (MCS) y el rendimiento real de la capa física.
* **Unidad de medida:** Decibelios (dB).
* **Rango típico en interiores:**
  * $\ge 25\text{ dB}$: Excelente (permite modulaciones máximas como 256-QAM o 1024-QAM).
  * $20\text{--}24\text{ dB}$: Buena (voz sobre IP y video HD estables).
  * $15\text{--}19\text{ dB}$: Marginal (navegación básica, posible degradación).
  * $< 10\text{ dB}$: Inservible (pérdida de paquetes masiva y desasociación).
* **Relevancia para Maplify:** Permite al equipo complementar la lectura del RSSI para discernir si una señal de $-68\text{ dBm}$ es utilizable (si el piso de ruido está en $-95\text{ dBm}$, SNR = $27\text{ dB}$) o deficiente.
* **Fuente:** CWNA Certified Wireless Network Administrator Study Guide; IEEE 802.11.

---

### 7. Noise Floor (Piso de Ruido)
* **Definición técnica:** Suma total de toda la energía de radiofrecuencia espuria presente en el canal en un instante dado, generada por fuentes no-802.11 (microondas, Bluetooth, motores, fuentes conmutadas, radar) y el ruido térmico cuántico inherente a los circuitos receptores ($kTB$).
* **Unidad de medida:** dBm.
* **Rango típico en interiores:** $-90\text{ dBm}$ a $-100\text{ dBm}$ en entornos limpios; sube a $-80\text{ dBm}$ en entornos con severa contaminación electromagnética.
* **Relevancia para Maplify:** Parámetro base para calcular el límite inferior de cobertura efectiva útil en una instalación.
* **Fuente:** Cisco CleanAir Whitepaper; CWNA Study Guide.

---

### 8. SSID (Service Set Identifier)
* **Definición técnica:** Cadena alfanumérica de hasta 32 octetos (bytes) incluida en las tramas Beacon y Probe Response que sirve como nombre lógico legible de la red inalámbrica para los usuarios.
* **Unidad de medida:** Cadena de caracteres UTF-8 (1 a 32 bytes).
* **Relevancia para Maplify:** Permite filtrar en las tablas de auditoría y agrupar mediciones pertenecientes a la red institucional bajo estudio (ej. "Edificio_Ingenieria") diferenciándolas de redes ajenas.
* **Fuente:** IEEE Std 802.11-2020.

---

### 9. BSSID (Basic Service Set Identifier)
* **Definición técnica:** Dirección MAC de 48 bits (6 pares hexadecimales) de la radio física específica de un Access Point que emite un BSS determinado. Un mismo AP físico con múltiples radios y SSIDs (VLANs) posee múltiples BSSIDs derivados.
* **Unidad de medida:** Notación MAC hexadecimal (`XX:XX:XX:XX:XX:XX`).
* **Relevancia para Maplify:** Es el identificador unívoco real de la fuente transmisora en las muestras tomadas en campo con herramientas como WiFi Analyzer o NetSpot.
* **Fuente:** IEEE Std 802.11-2020; CWNA Study Guide.

---

### 10. Bandas de Frecuencia WiFi (2.4 GHz, 5 GHz, 6 GHz)
* **Definición técnica:** Segmentos del espectro electromagnético sin licencia asignados para sistemas de comunicaciones inalámbricas de banda ancha:
  * **2.4 GHz ISM:** $2.400\text{--}2.4835\text{ GHz}$. Mayor alcance físico y penetración de muros, pero alta congestión y solo 3 canales no solapados.
  * **5 GHz UNII (UNII-1 a UNII-3):** $5.150\text{--}5.850\text{ GHz}$. Mayor espectro disponible (hasta 25 canales de 20 MHz), menor interferencia y mayor velocidad, con menor penetración de muros.
  * **6 GHz (Wi-Fi 6E / Wi-Fi 7):** $5.925\text{--}7.125\text{ GHz}$ (hasta 1200 MHz de espectro limpio, libre de dispositivos legacy).
* **Unidad de medida:** Gigahertz (GHz) / Megahertz (MHz).
* **Relevancia para Maplify:** Los mapas de calor deben distinguir la banda medida, ya que la atenuación a 5 GHz es sustancialmente mayor que a 2.4 GHz en una misma distancia.
* **Fuente:** IEEE 802.11ax/be; Wi-Fi Alliance; Resoluciones ANE (Agencia Nacional del Espectro Colombia).

---

### 11. Ancho de Canal (Channel Width)
* **Definición técnica:** Amplitud del espectro de frecuencia dedicado a un canal de comunicación individual. El estándar base utiliza $20\text{ MHz}$, pudiendo combinarse mediante Channel Bonding en bloques contiguos de $40\text{ MHz}$, $80\text{ MHz}$, $160\text{ MHz}$ o hasta $320\text{ MHz}$ (Wi-Fi 7).
* **Unidad de medida:** Megahertz (MHz).
* **Relevancia para Maplify:** A mayor ancho de canal, el piso de ruido aumenta físicamente en $+3\text{ dB}$ por cada duplicación ($20\to 40\to 80\text{ MHz}$), reduciendo la sensibilidad del receptor y el radio efectivo de cobertura.
* **Fuente:** IEEE Std 802.11n/ac/ax/be.

---

### 12. MCS (Modulation and Coding Scheme)
* **Definición técnica:** Índice numérico que estandariza la combinación específica de modulación digital (ej. BPSK, QPSK, 16-QAM, 64-QAM, 256-QAM, 1024-QAM, 4096-QAM), tasa de codificación de corrección de errores hacia adelante (FEC) y número de flujos espaciales (MIMO).
* **Unidad de medida:** Entero adimensional (MCS 0 a MCS 15 en 802.11be).
* **Relevancia para Maplify:** El mapa de calor de RSSI se traduce directamente en la capacidad del cliente para negociar un índice MCS alto o bajo.
* **Fuente:** IEEE 802.11-2020; Ekahau RF Design Guide.

---

### 13. Throughput (Tasa de Transferencia Real)
* **Definición técnica:** Tasa neta de bits de datos útiles de capa de aplicación que se transmiten exitosamente por segundo a través del medio de transmisión inalámbrico, descontando encabezados de tramas, preámbulos, acuses de recibo (ACKs), retransmisiones y tiempos de contienda CSMA/CA.
* **Unidad de medida:** Megabits por segundo (Mbps) o Gigabits por segundo (Gbps).
* **Rango típico en interiores:** Generalmente oscila entre el 50% y el 65% de la velocidad de señalización de la capa física (PHY Data Rate).
* **Relevancia para Maplify:** Parámetro de rendimiento perceptible por el usuario final, íntimamente correlacionado con el RSSI medido.
* **Fuente:** CWDP Study Guide; Aruba Validated Reference Design.

---

### 14. Latencia (Latency) y Jitter
* **Definición técnica:** Tiempo transcurrido en el viaje de ida y vuelta (RTT) de un paquete de datos entre el cliente inalámbrico y la puerta de enlace o servidor. El Jitter es la variabilidad estadística de dicha latencia en el tiempo.
* **Unidad de medida:** Milisegundos (ms).
* **Rango típico en WiFi empresarial:** $< 10\text{ ms}$ a la puerta de enlace local en condiciones óptimas; $> 100\text{ ms}$ en zonas marginales de borde de celda o con interferencia severa.
* **Relevancia para Maplify:** Permite sustentar en el marco teórico por qué un RSSI inferior a $-75\text{ dBm}$ provoca retardos notables en aplicaciones en tiempo real (llamadas VoIP o videoconferencias).
* **Fuente:** Cisco Enterprise Mobility Design Guide.

---

### 15. Celda de Cobertura (Coverage Cell) y Área de Cobertura
* **Definición técnica:** Región geográfica tridimensional alrededor de un Access Point donde el nivel de potencia recibida (RSSI) de sus tramas baliza (Beacons) y la relación SNR se mantienen por encima de un umbral predefinido de diseño (ej. $\ge -67\text{ dBm}$).
* **Unidad de medida:** Metros cuadrados ($m^2$) o radio en metros ($m$).
* **Relevancia para Maplify:** Corresponde a los círculos o gradientes coloreados que se proyectan en el lienzo sobre el plano arquitectónico.
* **Fuente:** CWDP Study Guide; Hamina Wireless Design Handbook.

---

### 16. AP (Access Point / Punto de Acceso)
* **Definición técnica:** Dispositivo de capa 2 del modelo OSI que conecta terminales inalámbricos (STA) a una red de distribución cableada mediante la conversión y transmisión de tramas 802.11 a tramas 802.3 Ethernet y viceversa.
* **Relevancia para Maplify:** Es el origen físico y centro emisor de la infraestructura analizada en el levantamiento.
* **Fuente:** IEEE 802.11-2020.

---

### 17. BSS (Basic Service Set) y ESS (Extended Service Set)
* **Definición técnica:**
  * **BSS:** Bloque constructivo básico de una red IEEE 802.11 compuesto por un único AP y todas las estaciones inalámbricas asociadas a él.
  * **ESS:** Conjunto de dos o más BSS interconectados mediante un sistema de distribución (DS) común, compartiendo el mismo SSID y permitiendo la movilidad transparente (*roaming*) de los clientes.
* **Relevancia para Maplify:** Contextualiza si el Site Survey se realiza a un único punto aislado (BSS) o a una topología universitaria distribuida (ESS).
* **Fuente:** IEEE 802.11-2020; CWNA Study Guide.

---

### 18. Site Survey WiFi (Levantamiento de Sitio)
* **Definición técnica:** Metodología sistemática de ingeniería consistente en la inspección física, medición de radiofrecuencia, detección de fuentes de interferencia y análisis computacional de propagación en una instalación para garantizar que el despliegue de una red WLAN cumpla con los requerimientos de cobertura, capacidad y calidad de servicio (SLA).
* **Relevancia para Maplify:** Es el objeto de estudio y propósito general de la aplicación desarrollada.
* **Fuente:** Ekahau Certified Survey Engineer Manual; Cisco CVD.

---

### 19. Heat Map (Mapa de Calor de Radiofrecuencia)
* **Definición técnica:** Representación cartográfica en dos dimensiones superpuesta sobre el plano arquitectónico de un recinto, donde los valores continuos de intensidad de señal (o métricas derivadas como SNR o Throughput) se codifican mediante una escala de colorimetría gradual (*Color Ramp* o mapa cromático).
* **Relevancia para Maplify:** Es la visualización gráfica central generada en el canvas HTML5 de la aplicación.
* **Fuente:** Hamina Wireless; Ekahau.

---

### 20. RSSI Threshold (Umbral de Señal / Límite de Cobertura)
* **Definición técnica:** Valor de corte en dBm por debajo del cual una señal se considera insuficiente para sostener una comunicación confiable, instruyendo al software a delimitar la visualización o advertir una falla de cobertura.
* **Unidad de medida:** dBm.
* **Valor típico:** $-75\text{ dBm}$ o $-80\text{ dBm}$ en entornos corporativos.
* **Relevancia para Maplify:** Define el valor configurable en la app a partir del cual el lienzo no proyecta color o marca la zona como "Sin cobertura útil".
* **Fuente:** Cisco Enterprise Wireless Design Guide.

---

### 21. Interpolación IDW (Inverse Distance Weighting / Ponderación por Inversa de la Distancia)
* **Definición técnica:** Algoritmo matemático determinista de interpolación espacial geoestadística basado en la Primera Ley de la Geografía de Waldo Tobler (*"todas las cosas están relacionadas entre sí, pero las cosas cercanas están más relacionadas que las distantes"*). Estima el valor desconocido $Z(u)$ en un punto arbitrario $u$ mediante la media ponderada de las muestras conocidas $Z(u_i)$, donde el peso $w_i$ es inversamente proporcional a la distancia elevada a una potencia $p$:
  $$Z(u) = \frac{\sum_{i=1}^{n} w_i(u) \cdot Z(u_i)}{\sum_{i=1}^{n} w_i(u)}, \quad \text{con } w_i(u) = \frac{1}{d(u, u_i)^p}$$
* **Relevancia para Maplify:** Es el motor algorítmico implementado en JavaScript vanilla en `app.html` para calcular los píxeles del mapa de calor a partir de los puntos medidos.
* **Fuente:** Shepard, D. (1968). *A two-dimensional interpolation function for irregularly-spaced data*; Isaaks & Srivastava, *Applied Geostatistics*.

---

### 22. Free Space Path Loss (FSPL / Pérdida en Espacio Libre)
* **Definición técnica:** Modelo matemático teórico que calcula la atenuación de una señal electromagnética al viajar por el vacío ideal sin obstáculos físicos, reflexiones ni absorción atmosférica:
  $$\text{FSPL}_{\text{dB}} = 20\log_{10}(d) + 20\log_{10}(f) + 20\log_{10}\left(\frac{4\pi}{c}\right)$$
  En unidades prácticas ($d$ en km y $f$ en MHz):
  $$\text{FSPL}_{\text{dB}} = 20\log_{10}(d_{\text{km}}) + 20\log_{10}(f_{\text{MHz}}) + 32.44$$
* **Unidad de medida:** Decibelios (dB).
* **Relevancia para Maplify:** Referencia teórica mínima para comparar los datos empíricos obtenidos en las mediciones de la universidad.
* **Fuente:** ITU-R P.525-4; Balanis, C. A. *Antenna Theory*.

---

### 23. Log-Distance Path Loss Model (Modelo de Pérdida Log-Distancia)
* **Definición técnica:** Extensión empírica del modelo FSPL para entornos reales interiores y exteriores. Modela la pérdida de trayectoria en función de la distancia mediante un exponente de atenuación de trayectoria ($n$ o $\gamma$):
  $$PL(d) = PL(d_0) + 10 \cdot n \cdot \log_{10}\left(\frac{d}{d_0}\right) + X_\sigma$$
  donde $d_0$ es una distancia de referencia (ej. $1\text{ m}$), $n$ depende de los obstáculos del recinto, y $X_\sigma$ representa el desvanecimiento lento por sombra (*shadowing*).
* **Unidad de medida:** Decibelios (dB).
* **Rango del exponente $n$:** $n=2$ (espacio libre), $n=2.7\text{--}3.5$ (oficinas con divisiones suaves), $n=4\text{--}6$ (edificios de concreto denso o naves industriales).
* **Relevancia para Maplify:** Justifica matemáticamente por qué la potencia $p=2$ del algoritmo IDW emula eficazmente la disipación física de la onda.
* **Fuente:** Rappaport, T. S. *Wireless Communications*; IEEE Transactions on Antennas and Propagation.

---

### 24. Zona de Fresnel (Fresnel Zone)
* **Definición técnica:** Volumen elipsoidal tridimensional concéntrico alrededor de la línea de vista directa (LoS) entre las antenas transmisora y receptora. Los obstáculos ubicados dentro de la primera zona de Fresnel introducen desfases en las ondas secundarias, provocando interferencia destructiva.
* **Unidad de medida:** Radio en metros ($r_1$ en el punto medio).
* **Relevancia para Maplify:** Explica por qué techos bajos, lámparas o mamparas intermedias degradan el RSSI aunque exista visibilidad visual parcial.
* **Fuente:** ITU-R P.530; CWNA Study Guide.

---

### 25. Multipath (Propagación Multitrayecto)
* **Definición técnica:** Fenómeno físico en el cual una misma señal de radio transmitida alcanza la antena receptora a través de múltiples caminos de longitud y tiempo variables, debido a fenómenos de reflexión, difracción y dispersión en paredes, pisos y techos.
* **Relevancia para Maplify:** En tecnologías antiguas causaba degradación; en estándares modernos 802.11n/ac/ax/be se aprovecha mediante antenas MIMO para aumentar la tasa de datos y estabilidad.
* **Fuente:** IEEE 802.11-2020; Saunders, S. *Antennas and Propagation for Wireless Communication Systems*.

---

### 26. Fading (Desvanecimiento) y Shadowing
* **Definición técnica:**
  * **Fast Fading (Desvanecimiento rápido de Rayleigh/Rician):** Fluctuaciones drásticas de fase y amplitud en distancias del orden de fracciones de longitud de onda ($\sim 6\text{--}12\text{ cm}$).
  * **Slow Fading (Shadowing / Desvanecimiento lento):** Caídas globales de potencia debidas a la interposición de grandes obstáculos en el trayecto.
* **Relevancia para Maplify:** Demuestra por qué dos mediciones tomadas a escasos 15 centímetros de distancia pueden variar ligeramente ($\pm 3\text{ dBm}$), sustentando la necesidad de promediar muestras en los puntos del Excel.
* **Fuente:** Goldsmith, A. *Wireless Communications*; Cambridge University Press.

---

### 27. Roaming (Itinerancia) y Umbral de Roaming
* **Definición técnica:** Proceso por el cual una estación cliente decide de manera autónoma desasociarse de un AP cuya señal se debilita para reasociarse a otro AP del mismo ESS que ofrezca un RSSI y SNR superiores, sin interrumpir sesiones de red.
* **Rango típico de activación:** $-67\text{ dBm}$ a $-72\text{ dBm}$ (dependiendo del driver del cliente, ej. algoritmo de roaming agresivo de Intel o Apple).
* **Relevancia para Maplify:** Para asegurar roaming transparente en los pasillos de la universidad, el mapa de calor debe evidenciar solapamiento entre celdas contiguas con un nivel mínimo de $-67\text{ dBm}$.
* **Fuente:** Cisco Enterprise Mobility Design Guide; Apple Support (macOS/iOS Wireless Roaming Reference).

---

### 28. Co-Channel Interference (CCI / Interferencia Cocanal)
* **Definición técnica:** Fenómeno de contienda y congestión que ocurre cuando dos o más Access Points cercanos operan en la misma frecuencia de canal dentro del rango de escucha mutua de sus tramas baliza o de sus clientes asociados. Al usar CSMA/CA, los APs no transmiten simultáneamente, compartiendo el tiempo de aire y reduciendo la capacidad neta a la mitad o más.
* **Relevancia para Maplify:** Justifica la pestaña y vista de análisis de canales en `app.html` para auditar la reutilización de frecuencias en el local.
* **Fuente:** CWDP Study Guide; Aruba Networks VRD.

---

### 29. Adjacent Channel Interference (ACI / Interferencia de Canal Adyacente)
* **Definición técnica:** Ruido e interferencia de espectro destructivo provocado por transmisiones en canales que se superponen parcialmente en sus máscaras de emisión espectral (por ejemplo, usar canales 1 y 2 simultáneamente en 2.4 GHz).
* **Relevancia para Maplify:** Fundamenta la regla de oro enseñada en el proyecto: en la banda de 2.4 GHz solo deben usarse los canales no solapados 1, 6 y 11.
* **Fuente:** IEEE 802.11; Cisco Spectrum Expert Handbook.

---

### 30. CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
* **Definición técnica:** Protocolo de acceso al medio compartido de la subcapa MAC de IEEE 802.11. Debido a que las radios no pueden transmitir y escuchar colisiones al mismo tiempo en el aire (Half-Duplex), las estaciones realizan detección física (CCA) y virtual (NAV) de energía antes de transmitir, aplicando un tiempo de espera aleatorio (*Random Backoff*).
* **Relevancia para Maplify:** Explica a los estudiantes por qué el tiempo de aire es un recurso finito y por qué una zona con muchas redes compartiendo canal produce lentitud extrema independientemente del RSSI.
* **Fuente:** IEEE Std 802.11-2020.

---

### 31. Modulación QAM (Quadrature Amplitude Modulation)
* **Definición técnica:** Esquema de modulación digital en el cual se varían simultáneamente tanto la amplitud como la fase de dos ondas portadoras sinusoidales en cuadratura (desfasadas $90^\circ$). Permite codificar múltiples bits por símbolo (ej. 64-QAM transporta 6 bits/símbolo; 1024-QAM en Wi-Fi 6 transporta 10 bits/símbolo; 4096-QAM en Wi-Fi 7 transporta 12 bits/símbolo).
* **Relevancia para Maplify:** Para mantener modulaciones densas como 1024-QAM se exige un SNR muy elevado ($\ge 35\text{ dB}$) y un RSSI superior a $-55\text{ dBm}$.
* **Fuente:** Proakis, J. G. *Digital Communications*; IEEE 802.11ax/be.

---

### 32. Levantamiento Pasivo, Activo y Predictivo
* **Definición técnica:**
  * **Pasivo (Passive Survey):** El adaptador inalámbrico escucha pasivamente tramas Beacon y Probe Response en todos los canales sin asociarse a ningún AP, registrando todos los SSIDs, BSSIDs, canales y niveles de RSSI.
  * **Activo (Active Survey):** El adaptador se asocia a un AP específico e interactúa enviando paquetes de prueba (Ping, iPerf) midiendo latencia, jitter, pérdida de paquetes y rendimiento real.
  * **Predictivo (Predictive Survey):** Simulación por software que estima la cobertura modelando la atenuación de muros en un motor de trazado de rayos (*Ray Tracing*) sin mediciones físicas en sitio.
* **Relevancia para Maplify:** Maplify procesa mediciones de un **Site Survey Pasivo o Activo simplificado**, convirtiendo datos tabulados en una representación continua.
* **Fuente:** Ekahau Site Survey Guidelines; Cisco CVD.
