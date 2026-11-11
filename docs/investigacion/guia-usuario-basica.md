# Guía Básica de Maplify: Entendiendo tu Señal WiFi sin Complicaciones

**Proyecto:** Maplify — Mapas de Señal WiFi  
**Universidad El Bosque** — Redes de Datos II  
**Dirigido a:** Usuarios, dueños de locales, administradores de oficinas y cualquier persona que quiera entender cómo funciona el WiFi sin tecnicismos difíciles.

---

## ¡Bienvenido a Maplify! 📶🗺️

¿Alguna vez te ha pasado que caminas por tu casa, oficina o local comercial y de repente el video de YouTube se detiene, la llamada de WhatsApp se entrecorta o las páginas web dejan de cargar? 

El problema casi nunca es el internet que pagas, sino **cómo viaja la señal inalámbrica en tu espacio**.

Esta guía fue creada para que entiendas de forma muy fácil qué hace **Maplify**, qué significan los colores de tu mapa y cómo tomar mejores decisiones para que el WiFi funcione perfecto en todos los rincones.

---

## 1. Conceptos Básicos Explicados con Manzanas 🍎

### ¿Qué es realmente el WiFi?
Imagina que el WiFi es como una **estación de radio FM**, pero en miniatura:
* El módem o router es como un locutor hablando por un altavoz.
* Tu celular o portátil es el radio receptor que intenta escucharlo.
* Si estás en la misma habitación, escuchas al locutor con total claridad. Pero si te vas al fondo del pasillo, cierras dos puertas de madera y te pones detrás de una pared de concreto, la voz del locutor se escuchará apagada, lejana o con estática.

---

### ¿Qué es la "fuerza de señal" y por qué importa?
La fuerza de señal es qué tan fuerte y clara le llega la voz del router a tu celular:
* Cuando la señal es fuerte, tu teléfono puede transferir datos a toda velocidad sin esfuerzo.
* Cuando la señal es débil, el celular tiene que pedirle al router que repita las cosas varias veces (*"¿puedes repetir lo que dijiste?"*). Eso hace que las páginas tarden en abrir y los videos se queden cargando en círculos.

---

### ¿Qué es esa cosa llamada "dBm"?
En Maplify verás números acompañados de las letras **dBm** (como `-45 dBm`, `-67 dBm` o `-82 dBm`). No te asustes por el nombre:
* **Todos son números negativos con un signo menos ($-$).**
* **La regla de oro:** Entre más **cerca de cero** esté el número, **más potente es tu señal**.
* **Ejemplo rápido:**
  * Una señal de **`-40 dBm`** es **excelente** (estás casi al lado del router).
  * Una señal de **`-85 dBm`** es **muy mala** (estás tan lejos que la señal casi desaparece).
  * ¡Recuerda que en números negativos, el $-40$ es más grande que el $-85$!

---

### ¿Qué es un "Punto de Acceso" (Access Point o AP)?
Es simplemente la **cajita con antenas** (o ese disco blanco circular que suele estar pegado en el techo de las universidades y centros comerciales). Su único trabajo es emitir la señal WiFi y comunicarse con tus dispositivos.

---

## 2. ¿Qué es un Mapa de Calor? 🌡️

Un mapa de calor de WiFi funciona exactamente igual que el **mapa del clima** que ves en las noticias de televisión:
* En el clima, las zonas calientes se pintan de un color y las zonas frías de otro.
* En **Maplify**, en lugar de temperatura, pintamos **qué tan buena es la señal WiFi** sobre el plano de tu local o edificio.

De un solo vistazo, puedes ver en qué mesas hay excelente conexión y en qué pasillos la señal se "muere".

---

## 3. El Semáforo de Colores de Maplify 🚦

Cuando cargues tus mediciones y oprimas **"Generar mapa"**, el plano se pintará con esta escala de colores:

| Color | ¿Qué significa en la vida real? | ¿Qué puedes hacer allí? | Rango de dBm |
|---|---|---|---|
| 🟢 **Verde Oscuro** | **Excelente / Inmejorable** | Videollamadas 4K, juegos en línea, descargas pesadas al instante. | Mejor que $-50\text{ dBm}$ |
| 🟢 **Verde Claro** | **Muy Buena** | Trabajar en la oficina, ver películas en alta definición sin pausas. | $-51\text{ a } -60\text{ dBm}$ |
| 🟡 **Amarillo** | **Aceptable / Justa** | Navegar en páginas web, redes sociales y música. A veces puede tardar un poco. | $-61\text{ a } -70\text{ dBm}$ |
| 🟠 **Naranja** | **Débil / Inestable** | Los mensajes de texto salen, pero los videos se traban y las llamadas se cortan. | $-71\text{ a } -80\text{ dBm}$ |
| 🔴 **Rojo** | **Zona Crítica / Mala** | El celular se desconecta a cada rato o gasta mucha batería intentando conectarse. | Peor que $-80\text{ dBm}$ |
| ⚪ **Sin Color / Blanco** | **Zona Lejana o No Medida** | No tomaste ninguna medición cerca o la señal no alcanza a llegar allí. | Fuera de rango |

---

## 4. ¿Por qué algunas partes del plano quedan en blanco?

Si notas que algunas esquinas o habitaciones de tu plano quedan sin ningún color:
1. **El programa no adivina:** Maplify es serio con los datos. Si en una habitación no tomaste ninguna medida con el celular, el programa prefiere dejarla en blanco antes que inventar datos falsos.
2. **Límite de distancia:** La señal WiFi de un punto medido solo se proyecta unos $4$ o $5$ metros a la redonda. Si una esquina está demasiado lejos de cualquier punto que mediste, se queda sin pintar.

---

## 5. Preguntas Frecuentes (FAQ) 💬

### 1. ¿Cómo se toman las mediciones de los puntos?
Basta con descargar una aplicación gratuita de escaneo WiFi en tu celular (como *WiFi Analyzer* en Android o usando una computadora portátil). Te paras físicamente en un lugar (por ejemplo: *"Mesa 1"*), anotas en un papel o en Excel el número que dice en la pantalla (ejemplo: `-58`) y repites el proceso en otros lugares del local.

### 2. ¿Cuántos puntos de medición debo tomar?
Para un local mediano o un aula de clases, recomendamos entre **8 y 15 puntos** bien distribuidos (algunos cerca del router, otros en el centro y otros en las esquinas más alejadas).

### 3. ¿El programa necesita internet para funcionar?
**No, cero internet.** Maplify funciona 100% desconectado en tu computador. Puedes abrirlo en una finca, sótano o lugar sin red y funcionará exactamente igual.

### 4. ¿Qué cosas dañan más la señal en un local?
Los enemigos número uno del WiFi son:
* **Paredes de concreto macizo y columnas:** Bloquean gran parte de la señal.
* **Espejos grandes y vidrios gruesos:** Hacen rebotar la señal como si fuera luz.
* **Estructuras metálicas y ascensores:** Crean una barrera casi infranqueable.
* **Hornos microondas y teléfonos inalámbricos viejos:** Cuando se encienden, generan interferencias invisibles en la banda de 2.4 GHz.

### 5. ¿Por qué mi celular marca "lleno de barritas" pero internet va lento?
Porque las barritas solo indican qué tan fuerte escuchas al router (la señal física), pero si hay **demasiadas redes alrededor usando el mismo canal** (interferencia cocanal), es como estar en una fiesta donde 20 personas gritan al mismo tiempo: escuchas mucho ruido, pero no entiendes ninguna palabra.

### 6. ¿Qué diferencia hay entre la "Misión guiada" y el "Laboratorio libre"?
* La **Misión guiada** es un tutorial interactivo paso a paso para que aprendas el método sin temor a equivocarte.
* El **Laboratorio libre** es el modo profesional donde puedes subir tus propios planos reales, tus archivos de Excel, mover los puntos arrastrándolos con el ratón y guardar la imagen final.

### 7. ¿Cómo guardo el mapa una vez que lo termine?
En el paso final de Maplify hay un botón llamado **"Descargar imagen (PNG)"**. Al oprimirlo, se guardará en tu carpeta de *Descargas* una imagen lista para imprimir o pegar en un informe.

### 8. Si veo mucho color rojo en mi mapa, ¿qué debo hacer?
Tienes tres opciones prácticas:
* Mover el router a un lugar más alto y despejado (nunca en el suelo ni dentro de un mueble de madera cerrado).
* Colocar un segundo Punto de Acceso (AP) conectado por cable de red hacia esa zona roja.
* Cambiar la frecuencia de tus equipos a la banda de **5 GHz**, que suele estar mucho más despejada.
