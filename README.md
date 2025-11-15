# 🩺 Servicio Médico en Docker – Predicción de Estado de Enfermedad

## 🎯 Problema Identificado

En el ámbito médico, existe la necesidad de contar con herramientas que permitan realizar **evaluaciones rápidas del estado de salud** de los pacientes basándose en parámetros clínicos fundamentales. Los médicos requieren sistemas que puedan:

- Procesar múltiples parámetros médicos de forma simultánea
- Proporcionar diagnósticos preliminares de manera rápida
- Estar disponibles 24/7 sin dependencias de infraestructura compleja
- Ser fácilmente desplegables en diferentes entornos hospitalarios

**Problema específico:** Los sistemas de diagnóstico tradicionales son costosos, requieren configuraciones complejas y no siempre están disponibles en entornos con recursos limitados.

## 🚀 Propósito del Proyecto

Este proyecto tiene como **objetivo principal** demostrar la implementación de un servicio de diagnóstico médico automatizado utilizando tecnologías modernas de contenedorización. 

### Objetivos Específicos:

1. **Crear un modelo predictivo simulado** que evalúe el estado de salud basado en tres parámetros médicos clave
2. **Implementar una API REST** para integración con sistemas hospitalarios existentes
3. **Proporcionar una interfaz web** intuitiva para uso directo por parte del personal médico
4. **Demostrar el uso de Docker** para despliegue consistente y escalable
5. **Servir como base** para futuras implementaciones con modelos de ML reales

### Beneficios Esperados:

- ✅ **Accesibilidad**: Disponible desde cualquier navegador web
- ✅ **Portabilidad**: Ejecutable en cualquier sistema con Docker
- ✅ **Escalabilidad**: Fácil replicación y distribución
- ✅ **Mantenibilidad**: Código organizado y documentado

## 📘 Descripción General

Este proyecto implementa un **servicio web en Docker** que simula el comportamiento de un modelo de Machine Learning para diagnóstico médico.

El sistema permite que un médico ingrese **tres valores médicos específicos** (glucosa, presión arterial y temperatura) y reciba uno de los siguientes posibles diagnósticos:

- `NO ENFERMO`
- `ENFERMEDAD LEVE`
- `ENFERMEDAD AGUDA`
- `ENFERMEDAD CRÓNICA`

> ⚠️ **Nota:** Este modelo **no realiza diagnósticos reales**. Su propósito es **demostrar la construcción y despliegue de un servicio en Docker**.

---

## 📂 Estructura del Repositorio

El repositorio está organizado de manera simple y eficiente para facilitar el desarrollo, mantenimiento y despliegue:

```
firstapp/
│
├── app.py                # 🐍 Aplicación principal Flask con lógica de negocio
├── Dockerfile            # 🐳 Configuración para construcción de imagen Docker
├── requirements.txt      # 📦 Dependencias de Python del proyecto
└── README.md             # 📚 Documentación completa del proyecto
```

### 📋 Descripción Detallada de Archivos:

#### `app.py` (Aplicación Principal)
- **Propósito**: Contiene toda la lógica del servicio web
- **Tecnología**: Flask (Python)
- **Funcionalidades**:
  - Función `predict_disease()`: Algoritmo de clasificación médica simulado
  - Ruta `/`: Interfaz web HTML para interacción directa
  - Ruta `/predict`: Procesamiento de formularios web
  - Ruta `/api/predict`: API REST para integraciones
- **Parámetros de entrada**: Glucosa, Presión arterial, Temperatura
- **Salida**: Clasificación del estado de salud

#### `Dockerfile` (Configuración de Contenedor)
- **Propósito**: Define el entorno de ejecución del servicio
- **Imagen base**: Python 3.9-slim (optimizada para producción)
- **Configuraciones**:
  - Instalación de dependencias
  - Copia de archivos del proyecto
  - Exposición del puerto 5001
  - Comando de inicio automático

#### `requirements.txt` (Gestión de Dependencias)
- **Propósito**: Lista todas las librerías de Python necesarias
- **Dependencias principales**:
  - `Flask`: Framework web para crear la API y interfaz
  - Versiones específicas para garantizar compatibilidad

#### `README.md` (Documentación)
- **Propósito**: Documentación completa del proyecto
- **Contenido**:
  - Guías de instalación y uso
  - Ejemplos de implementación
  - Explicación de la lógica de negocio
  - Instrucciones de despliegue

## 🏗️ Arquitectura del Sistema

### Componentes Principales:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend Web  │    │   API REST      │    │  Lógica de      │
│   (HTML Form)   │◄──►│   (Flask)       │◄──►│  Diagnóstico    │
│                 │    │                 │    │  (Python)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         ▲                       ▲                       ▲
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    Usuario      │    │  Aplicaciones   │    │   Algoritmo     │
│   (Médicos)     │    │   Externas      │    │  Predictivo     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Flujo de Datos:

1. **Entrada de Datos**: 
   - Interfaz web: Formulario HTML
   - API REST: JSON con parámetros médicos

2. **Procesamiento**:
   - Validación de datos de entrada
   - Conversión a tipos numéricos
   - Aplicación del algoritmo predictivo

3. **Clasificación**:
   - Cálculo del promedio de los tres parámetros
   - Aplicación de umbrales de clasificación
   - Generación del diagnóstico

4. **Respuesta**:
   - Interfaz web: Página HTML con resultado
   - API REST: JSON con predicción

### Tecnologías Utilizadas:

| Componente | Tecnología | Versión | Propósito |
|------------|------------|---------|-----------|
| Backend | Python | 3.9+ | Lógica de aplicación |
| Framework Web | Flask | Latest | API REST e interfaz |
| Contenedorización | Docker | Latest | Despliegue y portabilidad |
| Frontend | HTML/CSS | - | Interfaz de usuario |

## 💼 Casos de Uso del Sistema

### 👨‍⚕️ Uso Clínico Directo
**Actor**: Personal médico (médicos, enfermeras)
**Escenario**: Evaluación rápida en consulta
1. El médico accede a la interfaz web desde cualquier dispositivo
2. Ingresa los valores de glucosa, presión arterial y temperatura del paciente
3. Obtiene un diagnóstico preliminar instantáneo
4. Utiliza el resultado como apoyo para la toma de decisiones clínicas

### 🏥 Integración con Sistemas Hospitalarios
**Actor**: Sistemas de información hospitalaria (HIS)
**Escenario**: Procesamiento automatizado
1. El sistema hospitalario envía datos del paciente vía API REST
2. Recibe el diagnóstico en formato JSON estructurado
3. Integra el resultado en el expediente electrónico del paciente
4. Genera alertas automáticas según el nivel de severidad

### 🚀 Desarrollo y Pruebas
**Actor**: Desarrolladores y equipos de QA
**Escenario**: Validación de funcionalidades
1. Despliegue rápido en entornos de desarrollo
2. Pruebas de carga y rendimiento
3. Validación de respuestas de la API
4. Simulación de diferentes escenarios clínicos

### 📚 Educación y Capacitación
**Actor**: Estudiantes de medicina e instructores
**Escenario**: Herramienta educativa
1. Demostración de conceptos de diagnóstico automatizado
2. Práctica con diferentes combinaciones de parámetros
3. Comprensión de umbrales de clasificación médica
4. Introducción a tecnologías de ML en salud

---

## ⚙️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- [Docker](https://www.docker.com/get-started)  
- (Opcional) `curl` o un cliente para probar APIs

---

## 🚀 Construcción y Ejecución

### 🔹 Paso 1. Construir la imagen

Desde el directorio raíz del proyecto:

```bash
docker build -t medical-model .
```

### 🔹 Paso 2. Ejecutar el contenedor

```bash
docker run -d -p 5001:5001 medical-model
```

Esto iniciará el servicio web en el puerto **5001**.

---

## 💻 Uso del Servicio

### 🧠 Opción 1: Interfaz Web

Abre tu navegador y visita:  
👉 [http://localhost:5001](http://localhost:5001)

Allí podrás ingresar los tres valores médicos:
- **Glucosa**: Nivel de glucosa en sangre
- **Presión**: Presión arterial  
- **Temperatura**: Temperatura corporal

Por ejemplo: glucosa `2.5`, presión `6.3`, temperatura `8.0` y obtener un resultado de diagnóstico simulado.

---

### 🧩 Opción 2: API REST (JSON)

También puedes enviar los datos mediante una solicitud `POST` al endpoint `/api/predict`.

#### Ejemplo usando `curl`:

```bash
curl -X POST http://localhost:5001/api/predict \
     -H "Content-Type: application/json" \
     -d '{"values": [5.2, 7.1, 6.3]}'
```

**Formato de datos:**
- El array `values` debe contener exactamente 3 valores numéricos en el siguiente orden:
  1. **Glucosa** (nivel de glucosa en sangre)
  2. **Presión** (presión arterial)
  3. **Temperatura** (temperatura corporal)

#### Respuesta esperada:

```json
{"prediction": "ENFERMEDAD AGUDA"}
```

---

## 🧱 Descripción de Archivos

### `app.py`
Contiene el código principal del servicio Flask y una función llamada `predict_disease()` que simula el modelo.  
El diagnóstico se determina promediando los tres valores médicos ingresados (glucosa, presión y temperatura) y clasificando el resultado según su magnitud.

### `Dockerfile`
Define la imagen de Docker que instala dependencias, copia los archivos y lanza la aplicación.

### `requirements.txt`
Lista las dependencias necesarias del proyecto (por ahora solo Flask).

---

## 🩺 Lógica de Clasificación Simulada

El sistema calcula el promedio de los tres valores médicos (glucosa, presión arterial y temperatura) y aplica la siguiente lógica de clasificación:

| Promedio de valores médicos | Diagnóstico retornado |
|-----------------------------|-----------------------|
| < 3                        | `NO ENFERMO`          |
| 3 ≤ x < 6                  | `ENFERMEDAD LEVE`     |
| 6 ≤ x < 8                  | `ENFERMEDAD AGUDA`    |
| ≥ 8                        | `ENFERMEDAD CRÓNICA`  |

**Nota:** Los valores representan niveles normalizados de glucosa, presión arterial y temperatura corporal para fines de demostración.

---

## 🧩 Posibles Extensiones

- Conectar el servicio con un modelo real de ML entrenado (archivo `.pkl` o `.onnx`).
- Implementar autenticación para acceso médico.
- Guardar registros de consultas en una base de datos.
- Desplegar el servicio con Docker Compose o en Kubernetes.

---

## 🧠 Conclusión y Valor del Proyecto

Este proyecto representa una **implementación práctica y educativa** de cómo las tecnologías modernas pueden aplicarse al sector salud para crear soluciones accesibles y escalables.

### 🎯 Logros Alcanzados:

1. **Demostración Tecnológica**: Integración exitosa de Python, Flask y Docker para crear un servicio médico funcional
2. **Facilidad de Despliegue**: Cualquier usuario puede ejecutar el sistema completo con un solo comando de Docker
3. **Múltiples Interfaces**: Soporte tanto para usuarios finales (interfaz web) como para integraciones (API REST)
4. **Código Limpio y Documentado**: Base sólida para futuras extensiones y mejoras

### 🔮 Potencial de Expansión:

- **Integración con ML Real**: Reemplazar el algoritmo simulado con modelos entrenados (scikit-learn, TensorFlow)
- **Base de Datos**: Incorporar PostgreSQL o MongoDB para almacenar historiales médicos
- **Autenticación**: Implementar JWT o OAuth para seguridad médica
- **Microservicios**: Evolucionar hacia una arquitectura distribuida con Docker Compose
- **Cloud Deployment**: Desplegar en AWS, Azure o Google Cloud Platform

### 📈 Impacto Esperado:

Este proyecto sirve como **punto de partida** para desarrolladores que buscan crear soluciones tecnológicas en el ámbito de la salud, demostrando que es posible crear herramientas médicas útiles con tecnologías accesibles y bien documentadas.

**La combinación de simplicidad, funcionalidad y escalabilidad** hace de este proyecto una excelente base para futuras innovaciones en HealthTech.

---

## 👥 Contribución y Contacto

**Autor Principal:**  
Edwin Gómez

**¿Quieres contribuir?**
- 🐛 Reportar bugs o problemas
- 💡 Sugerir nuevas funcionalidades
- 🔧 Enviar pull requests con mejoras
- 📖 Mejorar la documentación

**Licencia:** GNU General Public License v3.0
