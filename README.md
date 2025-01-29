# Sistema de Carpool Universitario con IA y Machine Learning

## Descripción del Proyecto

Este sistema de **carpooling** está diseñado para mejorar la eficiencia y seguridad de los viajes compartidos dentro de la comunidad universitaria mediante la integración de **Inteligencia Artificial (IA) y Machine Learning (ML)**. La plataforma permite a los estudiantes indicar diariamente si tienen carro y desean ser conductores o si necesitan transporte, optimizando rutas, previendo disponibilidad y garantizando la seguridad.

---

## **Características Principales**

### **1. Registro de Usuarios**

- Los estudiantes crean un perfil con su ubicación y horarios habituales.
- Se requiere el **"ID de Epik"** para verificar que sean estudiantes activos de la universidad y garantizar la seguridad.

### **2. Publicación de Disponibilidad Diaria**

- Cualquier usuario puede indicar si tiene carro ese día y hacia dónde se dirige.
- El sistema hace *matching* con pasajeros que tengan rutas compatibles y dentro de la capacidad del vehículo.
- Los pasajeros pueden ingresar su horario y ruta, y el sistema les asigna un conductor disponible.
- Un mismo usuario puede actuar como conductor en ciertos días y como pasajero en otros.

### **3. Matching Inteligente**

- Algoritmo de **ML** encuentra coincidencias entre conductores y pasajeros según su ubicación, rutas y horarios.
- Considera la capacidad del vehículo y distribuye pasajeros equitativamente.

### **4. Optimización de Rutas**

- Modelo de **IA** que sugiere la mejor ruta considerando tráfico y tiempo de llegada.
- Si un usuario no encuentra coincidencias exactas, el sistema sugiere ajustes de horario o ruta.

### **5. Sistema de Pago Flexible**

- Los pasajeros pueden ofrecer una cantidad de dinero por el viaje.
- El conductor puede aceptar o rechazar la oferta.
- Se establece un método de contribución justa basado en la distancia y el número de pasajeros.
- El pago es mayormente un incentivo para que los estudiantes ofrezcan transporte seguro y económico.
- Se toma en cuenta que el conductor ya haría el viaje de todas formas, por lo que el costo se reparte entre los pasajeros y no cubre el total del trayecto.
- También se considera el costo del parqueadero universitario.

### **6. Sistema de Seguridad**

- Algoritmo de detección de anomalías analiza el historial de viajes y calificaciones para identificar comportamientos sospechosos.
- Solo estudiantes verificados pueden acceder a la plataforma para evitar fraudes.

---

## **Integración de IA y ML**

### **1. Matching Inteligente (ML - Clustering y Redes Neuronales)**

- **Técnica:** K-Means Clustering o DBSCAN para agrupar estudiantes con rutas y horarios similares.
- **Aplicación:** Si un estudiante no encuentra match exacto, la IA puede agruparlo con otro con ruta cercana y horario flexible.

### **2. Optimización de Rutas con IA (Pathfinding + Reinforcement Learning)**

- **Técnica:** Algoritmos como **A**\* o **Dijkstra** combinados con Reinforcement Learning.
- **Aplicación:** Sugiere la mejor ruta para recoger a todos los pasajeros minimizando el tiempo de viaje.

### **3. Predicción de Disponibilidad de Viajes (Regresión + Series Temporales)**

- **Técnica:** Modelos de regresión o **LSTMs** para predecir la disponibilidad de cupos en ciertas rutas y horarios.
- **Aplicación:** Si en ciertos días hay escasez de conductores, el sistema puede sugerir incentivos o alertas.

### **4. Detección de Anomalías para Seguridad (Anomaly Detection)**

- **Técnica:** **Isolation Forest** o **Autoencoders** para identificar patrones sospechosos.
- **Aplicación:** Si un conductor cambia su ruta inesperadamente o cancela viajes con frecuencia, se genera una alerta.

### **5. Sistema de Reputación con IA (NLP + Sentiment Analysis)**

- **Técnica:** Análisis de sentimiento con **NLP** en comentarios y calificaciones.
- **Aplicación:** Detecta quejas recurrentes y ajusta la reputación de los usuarios en el sistema.

### **6. Predicción de Costos**

- **Técnica:** Modelos de ML que estiman costos de gasolina y sugieren una contribución justa entre los pasajeros.
- **Aplicación:** La IA calcula una distribución equitativa del costo, asegurando que los pasajeros contribuyan proporcionalmente sin cargar todo el gasto al conductor.
- **Consideración:** Se tiene en cuenta que el conductor realizaría el viaje de todas formas y que el costo del trayecto se divide entre varios pasajeros.

---

## **Extras e Innovaciones**

✅ **Integración con APIs de mapas**: Google Maps, OpenStreetMap, Here API para mejorar la navegación. ✅ **Gamificación**: Recompensas para usuarios frecuentes o conductores responsables. ✅ **Predicción de Costos**: Un modelo ML podría estimar costos de gasolina y sugerir una contribución justa entre los pasajeros.

---

## **Requisitos del Sistema**

### **Tecnologías Utilizadas**

- **Backend:** Django / Flask
- **Base de Datos:** PostgreSQL / Firebase
- **Frontend:** React.js / Vue.js
- **Machine Learning:** Python (TensorFlow, scikit-learn, Pandas, NumPy)
- **APIs:** Google Maps API, OpenStreetMap

### **Dependencias**

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

---

## **Guía de Instalación y Ejecución**

### **1. Clonar el Repositorio**

```bash
git clone https://github.com/tuusuario/carpool-ia.git
cd carpool-ia
```

### **2. Crear un Entorno Virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate  # En Windows
```

### **3. Instalar Dependencias**

```bash
pip install -r requirements.txt
```

### **4. Configurar Variables de Entorno**

Crea un archivo `.env` en la raíz del proyecto con las credenciales necesarias.

```ini
DATABASE_URL=postgres://usuario:contraseña@localhost:5432/carpool
GOOGLE_MAPS_API_KEY=tu_api_key
```

### **5. Ejecutar el Servidor**

```bash
python manage.py runserver
```

### **6. Acceder a la Aplicación**

Abre tu navegador y ve a `http://127.0.0.1:8000/`

---

## **Contribución**

Si quieres contribuir a este proyecto, sigue estos pasos:

1. **Haz un fork** del repositorio.
2. **Crea una nueva rama** (`git checkout -b nueva-funcionalidad`).
3. **Realiza tus cambios** y haz un commit (`git commit -m 'Agregada nueva funcionalidad'`).
4. **Sube los cambios** (`git push origin nueva-funcionalidad`).
5. **Crea un Pull Request** y explícanos tu contribución.

---

## **Licencia**

Este proyecto está licenciado bajo la licencia MIT. Puedes ver el archivo `LICENSE` para más detalles.

---







