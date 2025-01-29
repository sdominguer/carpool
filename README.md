# Sistema de Carpool Universitario con IA y Machine Learning

## Descripción del Proyecto

Este sistema de **carpooling** está diseñado para mejorar la eficiencia y seguridad de los viajes compartidos dentro de la comunidad universitaria mediante la integración de **Inteligencia Artificial (IA) y Machine Learning (ML)**. La plataforma permite a los estudiantes registrar sus horarios y preferencias de viaje, y luego utiliza algoritmos avanzados para optimizar rutas, predecir disponibilidad y garantizar la seguridad.

---

## **Características Principales**

### **1. Registro de Usuarios**

- Los estudiantes crean un perfil con su ubicación, horarios de clase y preferencias (ej. solo mujeres, no mascotas, no fumadores, etc.).

### **2. Matching Inteligente**

- Algoritmo de **ML** encuentra coincidencias entre conductores y pasajeros según su ubicación, rutas y horarios.

### **3. Predicción de Disponibilidad**

- El sistema analiza patrones de uso y sugiere viajes incluso cuando los horarios no coinciden exactamente.

### **4. Optimización de Rutas**

- Modelo de **IA** que sugiere la mejor ruta considerando tráfico y tiempo de llegada.

### **5. Sistema de Seguridad**

- Algoritmo de detección de anomalías analiza el historial de viajes y calificaciones para identificar comportamientos sospechosos.

### **6. Recomendaciones de Horarios**

- Si un usuario no encuentra coincidencias, la IA puede sugerir ajustes en su horario para mejorar la compatibilidad con otros usuarios.

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

## poner licencia


