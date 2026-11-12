# Cuestionario Técnico: Auditoría de Cobertura, Radiofrecuencia y Site Survey en Redes WLAN Empresariales

**Institución:** Universidad El Bosque — Facultad de Ingeniería  
**Asignatura:** Redes de Datos II (Línea CCNA: RESA / FCERI)  
**Proyecto Final:** Maplify  
**Autores:** Daniela Ocando, Edwar Almeciga, Nicolás Mora  
**Docente:** Ing. Titular de Cátedra  
**Fecha de Entrega:** 15 de Noviembre de 2026  
**Formato del Reactivo:** Selección múltiple con única respuesta estilo **Cisco Networking Academy (CCNA Intermedio)** con justificación técnica y análisis de distractores.

---

## Pregunta 1 (CCNA Intermedio · Cisco CVD & IEEE 802.11 Roaming)

**Consulte la ilustración.** Un ingeniero de redes inalámbricas de la Universidad El Bosque analiza el diseño de cobertura en el pasillo principal del campus mediante la herramienta **Maplify**. Dos Access Points (AP-1 en canal 36 y AP-2 en canal 44 de la banda de 5 GHz) han sido desplegados para soportar telefonía de Voz sobre WiFi (VoWLAN). Un usuario conectado a una llamada de voz activa camina desde AP-1 hacia AP-2. 

Según las recomendaciones oficiales de **Cisco Enterprise Mobility Design Guide (CVD)** y el estándar IEEE 802.11, ¿cuál es el comportamiento esperado del cliente móvil en el área de transición y qué criterio de diseño de solapamiento garantiza que la llamada no sufra degradación ni cortes?

* **A.** El cliente iniciará el escaneo activo de canales cuando el RSSI de AP-1 caiga por debajo de -80 dBm, requiriendo un solapamiento del 50% entre celdas para evitar el efecto de cliente pegajoso (*sticky client*).
* **B.** El cliente mantendrá la asociación con AP-1 hasta perder completamente la señal (-90 dBm) debido a que ambos APs pertenecen al mismo ESSID, obligando a reubicar AP-2 en el mismo canal 36.
* **C.** El cliente comenzará el proceso de búsqueda y reasociación cuando el RSSI de AP-1 alcance el umbral de -67 dBm, requiriendo un solapamiento entre celdas del 15% al 20% con una relación señal a ruido (SNR) mínima de 25 dB.
* **D.** La llamada se mantendrá sin interrupciones únicamente si el cliente conmuta de 5 GHz a 2.4 GHz en el punto medio, porque la frecuencia de 2.4 GHz ofrece mayor inmunidad frente al desvanecimiento multicamino (*multipath fading*).

---

### Respuesta Correcta: C

#### Justificación Técnica y Análisis de Opciones (Cisco CVD & IEEE 802.11):
* **Opción C es CORRECTA:** De acuerdo con la guía de diseño de movilidad de Cisco (CVD) y las especificaciones de roaming de terminales corporativos (terminales VoIP Cisco 8821 y dispositivos móviles Apple/Android modernos), los clientes inician el escaneo de canales de fondo para itinerar (*roaming trigger*) cuando el RSSI de la celda asociada se degrada hasta **-67 dBm**. Para garantizar una transición fluida sin pérdida de paquetes (< 50 ms) ni afectación perceptible en el códec de voz, las celdas contiguas deben solaparse físicamente entre un **15% y un 20%** del área de cobertura en la frontera de -67 dBm, con un SNR $\ge 25\text{ dB}$.
* **Distractor A es INCORRECTO:** Un umbral de -80 dBm es sumamente tardío; a dicho nivel la tasa de modulación colapsa a BPSK, provocando pérdida masiva de tramas y caída de la llamada antes de intentar el roaming. Un solapamiento del 50% es excesivo y provoca desperdicio de tiempo de aire.
* **Distractor B es INCORRECTO:** Forzar a que AP-2 use el mismo canal 36 en celdas adyacentes generaría una severa Interferencia Cocanal (CCI), destruyendo el tiempo de aire por contienda CSMA/CA.
* **Distractor D es INCORRECTO:** Forzar roaming inter-banda (band steering inverso hacia 2.4 GHz) aumenta la latencia por renegociación y traslada al usuario a una banda mucho más congestionada y ruidosa.

---

## Pregunta 2 (CCNA Intermedio · Gestión de Espectro, Contienda CSMA/CA y Calidad de Señal)

**Consulte la ilustración.** Durante una auditoría de espectro en el edificio de laboratorios de la Universidad El Bosque, el software **Maplify** detecta la distribución espectral en la banda de 2.4 GHz. La infraestructura institucional posee AP-Norte (Canal 1), AP-Centro (Canal 6) y AP-Biblioteca (Canal 11). Sin embargo, se identifican dos anomalías: un router autónomo no autorizado operando en el Canal 2, y un AP departamental adicional (AP-Sur) configurado indebidamente en el Canal 6. 

¿Qué efectos causan respectivamente el AP en Canal 2 y el AP-Sur en Canal 6 sobre el rendimiento de la red y qué principio de la capa MAC de IEEE 802.11 explica este comportamiento?

* **A.** El Canal 2 provoca colisiones no gestionadas en el aire mediante CSMA/CD, mientras que AP-Sur en Canal 6 duplica el rendimiento gracias a la agregación de enlaces por canal compartido.
* **B.** El Canal 2 ocasiona Interferencia de Canal Adyacente (ACI) destructiva elevando el piso de ruido y corrompiendo preámbulos, mientras que AP-Sur causa Interferencia Cocanal (CCI), donde el protocolo CSMA/CA obliga a ambos APs a compartir el tiempo de aire reduciendo la capacidad neta.
* **C.** Ambos escenarios representan Interferencia de Canal Adyacente (ACI), y se corrigen automáticamente activando la modulación 1024-QAM de Wi-Fi 6 en todos los dispositivos clientes.
* **D.** Ninguna de las situaciones afecta la red, puesto que el espectro de 2.4 GHz cuenta con 14 canales independientes y el espaciado de 5 MHz entre portadoras adyacentes es suficiente para aislar las transmisiones.

---

### Respuesta Correcta: B

#### Justificación Técnica y Análisis de Opciones (IEEE 802.11 & CWNA):
* **Opción B es CORRECTA:** En 2.4 GHz cada canal tiene 20-22 MHz de ancho, pero las frecuencias centrales distan solo 5 MHz. El Canal 2 se solapa parcialmente con el Canal 1 provocando **Interferencia de Canal Adyacente (ACI)**; dado que los receptores no pueden decodificar tramas de canales no coincidentes, la energía se interpreta como ruido electromagnético de fondo (elevando el *Noise Floor* y desplomando el SNR). Por otro lado, dos APs en el Canal 6 causan **Interferencia Cocanal (CCI)**; al operar bajo el mismo canal, el mecanismo de evaluación de canal libre (CCA) y el vector de asignación de red (NAV) de **CSMA/CA** fuerzan a que ambos APs compartan el tiempo de transmisión (*Airtime*), duplicando la latencia de contienda y reduciendo a la mitad el *throughput* disponible para cada celda.
* **Distractor A es INCORRECTO:** En 802.11 no existe CSMA/CD (Collision Detection), pues los transceptores de radio son Half-Duplex y no pueden detectar colisiones mientras transmiten.
* **Distractor C es INCORRECTO:** CCI y ACI son problemas físicos y de capa MAC; una modulación más densa como 1024-QAM requiere un SNR aún mayor (> 35 dB) y fallaría de inmediato en un entorno ruidoso.
* **Distractor D es INCORRECTO:** En 2.4 GHz solo existen tres canales no solapados (1, 6 y 11). Los canales contiguos a 5 MHz sufren un solapamiento del 70% al 80%.

---

## Pregunta 3 (CCNA Intermedio · Atenuación de Materiales Constructivos e Interpolación IDW)

**Consulte la ilustración.** En el módulo de Laboratorio de **Maplify**, un grupo de estudiantes cargó las mediciones de RSSI tomadas en dos ambientes universitarios: la Sala A (oficinas separadas por tabiques de drywall) y la Sala B (laboratorio aislado por un muro de concreto armado de 20 cm de espesor). El AP principal se ubica en la esquina superior izquierda de la Sala A. 

Al procesar la interpolación mediante el algoritmo de **Inversa de la Distancia Ponderada (IDW con potencia p = 2)**, los estudiantes observan que el punto P4 marca -82 dBm (crítico) y que el área correspondiente a P5 se mantiene completamente en blanco sin color. 

¿Cuál es la causa técnica de la fuerte atenuación en la Sala B y por qué el algoritmo IDW deja la zona P5 sin renderizar?

* **A.** El muro de concreto atenúa la señal en solo 2 dB, pero el algoritmo IDW se detiene porque detectó una división por cero en las coordenadas de P4.
* **B.** La Sala B sufre interferencia destructiva por refracción atmosférica, y la zona P5 queda en blanco porque la aplicación exige un mínimo de 50 puntos para calcular matrices espaciales.
* **C.** El muro de concreto armado introduce una pérdida de inserción severa (12 dB a 18 dB en 2.4 GHz y hasta 25 dB en 5 GHz), mientras que el algoritmo IDW implementa un radio de corte máximo (R_max) que delimita la interpolación a la vecindad de datos medidos para no extrapolar valores falsos en zonas ciegas.
* **D.** El tabique de drywall absorbe más energía que el concreto armado debido a su densidad mineral, y la zona P5 se omitió porque el RSSI superó el valor máximo permitido de 0 dBm.

---

### Respuesta Correcta: C

#### Justificación Técnica y Análisis de Opciones (NIST & Geoestadística IDW):
* **Opción C es CORRECTA:** Según los reportes de atenuación electromagnética de NIST (Technical Note 1396) y las guías de CWDP, el concreto armado con varillas de acero provoca una pérdida masiva por absorción y reflexión de **12 a 18 dB en 2.4 GHz** y de **18 a 28 dB en 5 GHz** (comparado con apenas 2 a 3 dB de un tabique de drywall). Por ello, la señal colapsa a -82 dBm al ingresar a la Sala B. En cuanto al modelado matemático de Maplify, el algoritmo IDW utiliza una función con soporte compacto o **radio de influencia ($R_{\text{max}}$)**: si un píxel en las inmediaciones de P5 se encuentra a una distancia superior a $R_{\text{max}}$ de cualquier punto medido, su ponderador es nulo ($w=0$), manteniendo el canal alfa en cero (transparente) para evitar falsear o inventar cobertura en áreas no auditadas.
* **Distractor A es INCORRECTO:** Un muro de concreto jamás atenúa solo 2 dB (esa cifra corresponde a drywall o vidrio simple), y el algoritmo IDW previene división por cero mediante un factor épsilon $\epsilon = 0.0001$.
* **Distractor B es INCORRECTO:** La refracción atmosférica es despreciable en recintos confinados a distancias de 10 metros, e IDW opera píxel a píxel sin exigir 50 muestras.
* **Distractor D es INCORRECTO:** El yeso posee una densidad dieléctrica mucho menor que el concreto reforzado, por lo que su atenuación es significativamente más baja.

---

## Pregunta 4 (CCNA Intermedio · Presupuesto de Enlace, Cálculo de PIRE/EIRP y Regulación ANE/CRC)

Un ingeniero de redes configura un Access Point corporativo para iluminar la plazoleta central de la Universidad El Bosque. La tarjeta de radio del AP se ajusta a una potencia de transmisión conducida de **+17 dBm**. El AP se conecta a una antena sectorial externa mediante un cable coaxial de baja pérdida con conectores que introducen una pérdida total combinada de **2 dB**. La antena sectorial posee una ganancia directiva de **+8 dBi** en el lóbulo principal.

Considerando la fórmula de Potencia Isótropa Radiada Equivalente (PIRE / EIRP) y las regulaciones del Ministerio de Tecnologías de la Información y las Comunicaciones (MinTIC / ANE Resolución 105 de 2020) en Colombia para la banda de 2.4 GHz, ¿cuál es la PIRE emitida por el sistema y cumple con la normativa nacional?

* **A.** PIRE = 27 dBm (500 mW); no cumple con la regulación colombiana porque la ANE restringe la emisión en interiores y exteriores a un máximo estricto de 20 dBm (100 mW).
* **B.** PIRE = 11 dBm (12.5 mW); cumple con la regulación, pero genera una potencia insuficiente para que los clientes negocien modulación por encima de BPSK a más de 2 metros.
* **C.** PIRE = +23 dBm (equivalente a 200 mW); el sistema CUMPLE con la normativa nacional, ya que la Resolución ANE 105 permite una potencia pico máxima conducida de hasta +30 dBm (1 W) y una PIRE máxima de hasta +36 dBm (4 W) en la banda de 2.4 GHz para sistemas punto a multipunto.
* **D.** PIRE = +38 dBm (6300 mW); no cumple la normativa, debido a que la ganancia de la antena multiplica logarítmicamente la atenuación del cable provocando saturación en el receptor.

---

### Respuesta Correcta: C

#### Justificación Técnica y Análisis de Opciones (ITU-R & ANE Colombia):
* **Opción C es CORRECTA:** La Potencia Isótropa Radiada Equivalente (EIRP / PIRE) se calcula mediante el balance logarítmico:
  $$\text{PIRE} = P_{\text{tx}} - L_{\text{cable}} + G_{\text{ant}} = 17\text{ dBm} - 2\text{ dB} + 8\text{ dBi} = +23\text{ dBm}$$
  Para convertir dBm a milivatios lineales:
  $$P_{\text{mW}} = 10^{\frac{23}{10}} = 10^{2.3} \approx 199.53\text{ mW} \approx 200\text{ mW}$$
  En Colombia, el Cuadro Nacional de Atribución de Bandas de Frecuencias (CNABF) y la Resolución ANE 105 de 2020 establecen para la banda de 2.4 GHz (2400 – 2483.5 MHz) un límite de potencia en el transmisor de hasta 1 W (30 dBm) con ganancia de antena de hasta 6 dBi (PIRE máxima de 36 dBm / 4 W). Al emitir 23 dBm (200 mW), el despliegue se encuentra ampliamente dentro del marco legal permitido.
* **Distractor A es INCORRECTO:** La suma matemática da 23 dBm, no 27 dBm. Además, el límite de 20 dBm (100 mW) corresponde a la regulación europea ETSI, no a la norma colombiana/FCC.
* **Distractor B es INCORRECTO:** Restó erróneamente la ganancia de la antena ($17 - 2 - 8 = 7\text{ dBm}$ o cálculo erróneo de 11 dBm). Las antenas aportan ganancia pasiva al enfocar la energía.
* **Distractor D es INCORRECTO:** Realizó un cálculo inflado incongruente con la fórmula lineal de decibelios.

---

## Pregunta 5 (CCNA Intermedio · Metodología de Site Survey Pasivo vs. Activo y Métricas de Rendimiento)

Durante las pruebas de aceptación de la red WiFi en el nuevo auditorio de la Universidad El Bosque, los estudiantes reportan que la herramienta **Maplify** muestra un mapa de calor con niveles de señal de -58 dBm (color verde claro, categorizado como "Muy Bueno") en todo el recinto. Sin embargo, al realizar videoconferencias en Teams con 120 usuarios simultáneos, se presentan congelamientos continuos y audio robotizado. El equipo de infraestructura decide realizar un levantamiento complementario.

¿Qué tipo de Site Survey se ejecutó inicialmente con Maplify, qué tipo de levantamiento se debe realizar ahora para diagnosticar la causa raíz del problema, y qué métricas técnicas revelarán el cuello de botella?

* **A.** Se ejecutó un Site Survey Predictivo; se debe cambiar a un Site Survey por Simulación CAD midiendo únicamente el ancho de banda del switch de acceso mediante SNMP.
* **B.** Se ejecutó un Site Survey Pasivo (basado únicamente en la potencia RSSI de las tramas baliza); se debe realizar un Site Survey Activo asociando clientes de prueba al BSSID corporativo para medir la utilización del tiempo de aire, jitter, pérdida de paquetes y rendimiento real (Throughput con iPerf) bajo carga multiusuario.
* **C.** Se ejecutó un Site Survey Activo; se debe ejecutar un Site Survey Pasivo porque las tramas Beacon contienen la información de modulación y codificación (MCS) que resuelve la sobrecarga de usuarios.
* **D.** El problema es exclusivamente de cableado estructurado Cat 5e; ningún Site Survey puede evaluar el rendimiento inalámbrico si los clientes ya reciben una señal de -58 dBm.

---

### Respuesta Correcta: B

#### Justificación Técnica y Análisis de Opciones (CWDP & Cisco CVD):
* **Opción B es CORRECTA:** Un **Site Survey Pasivo** (como el levantamiento base importado en hojas de Excel hacia Maplify) recopila únicamente métricas de RF del medio físico escuchando Beacons (RSSI, canal, SSID, BSSID). Una señal de -58 dBm garantiza que existe potencia electromagnética suficiente, pero **no mide la contienda, la capacidad del canal ni el tráfico real**. Con 120 terminales en un mismo AP, la colisión de ranuras temporales de CSMA/CA satura el canal (Airtime Utilization > 80%), disparando el *jitter* y la pérdida de paquetes. Para diagnosticar esto, se debe ejecutar un **Site Survey Activo** donde el terminal auditor se asocie a la red y transmita tráfico UDP/TCP hacia un servidor local (iPerf) para medir el Throughput real, latencia de ida y vuelta (RTT) y tasas MCS efectivas.
* **Distractor A es INCORRECTO:** No fue predictivo, ya que se tomaron mediciones de campo físicas con Excel.
* **Distractor C es INCORRECTO:** El survey pasivo no puede medir el impacto del tráfico concurrente de capa de aplicación ni la contienda de usuarios reales.
* **Distractor D es INCORRECTO:** En entornos de alta densidad (High-Density WLANs), la congestión de tiempo de aire y la contienda MAC son típicamente el cuello de botella primordial antes que el enlace de subida Ethernet.

---

## Referencias Bibliográficas (Estándar IEEE)

1. **IEEE Standards Association**, "IEEE Std 802.11-2020: IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems - Local and Metropolitan Area Networks—Specific Requirements - Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications," IEEE, Piscataway, NJ, Feb. 2021. doi: 10.1109/IEEESTD.2021.9363693.
2. **Cisco Systems Inc.**, "Enterprise Mobility 8.5 Design Guide: Cisco Validated Design (CVD)," Cisco Systems Enterprise Document, San Jose, CA, 2020.
3. **D. X. Coleman and D. D. Westcott**, *CWNA Certified Wireless Network Administrator Study Guide: Exam CWNA-108*, 6th ed., Indianapolis, IN: Sybex / John Wiley & Sons, 2021.
4. **S. M. Jackman, M. Swartz, B. E. Smith, and M. E. Carter**, *CWDP Certified Wireless Design Professional Official Study Guide: Exam PW0-250*, Indianapolis, IN: John Wiley & Sons, 2014.
5. **T. S. Rappaport**, *Wireless Communications: Principles and Practice*, 2nd ed., Upper Saddle River, NJ: Prentice Hall PTR, 2002.
6. **International Telecommunication Union (ITU-R)**, "Recommendation ITU-R P.1238-10: Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz," ITU Radiocommunication Sector, Geneva, Switzerland, Aug. 2019.
7. **International Telecommunication Union (ITU-R)**, "Recommendation ITU-R P.525-4: Calculation of free-space attenuation," ITU Radiocommunication Sector, Geneva, Switzerland, Aug. 2019.
8. **D. Shepard**, "A two-dimensional interpolation function for irregularly-spaced data," in *Proc. 1968 23rd ACM Nat. Conf.*, 1968, pp. 517–524. doi: 10.1145/800186.810616.
9. **M. S. Gast**, *802.11 Wireless Networks: The Definitive Guide*, 2nd ed., Sebastopol, CA: O'Reilly Media, 2005.
10. **Ekahau Inc.**, "Wi-Fi Site Survey Guidelines: Best Practices for Pre- and Post-Deployment Surveys," Ekahau Technical White Papers, Reston, VA, 2023.
11. **Agencia Nacional del Espectro (ANE)**, "Resolución 105 de 2020 y Resolución 737 de 2021: Actualización del Cuadro Nacional de Atribución de Bandas de Frecuencias (CNABF) y uso libre del espectro en Colombia," MinTIC, Bogotá D.C., Colombia, 2021.
12. **National Institute of Standards and Technology (NIST)**, "Electromagnetic Signal Attenuation in Construction Materials," NIST Technical Note 1396, U.S. Dept. of Commerce, Boulder, CO, 1997.

