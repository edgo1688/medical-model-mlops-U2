# 🩺 Servicio Médico en Docker – Predicción de Estado de Enfermedad

## 📘 Descripción General

Este proyecto implementa un **servicio web en Docker** que simula el comportamiento de un modelo de Machine Learning para diagnóstico médico.

El sistema permite que un médico ingrese **tres valores numéricos** (por ejemplo, resultados clínicos o síntomas cuantificados) y reciba uno de los siguientes posibles diagnósticos:

- `NO ENFERMO`
- `ENFERMEDAD LEVE`
- `ENFERMEDAD AGUDA`
- `ENFERMEDAD CRÓNICA`

> ⚠️ **Nota:** Este modelo **no realiza diagnósticos reales**. Su propósito es **demostrar la construcción y despliegue de un servicio en Docker**.

---

## 📂 Estructura del Proyecto

```
mlops-medical-service/
│
├── app.py                # Código principal del servicio Flask
├── Dockerfile            # Archivo de construcción de la imagen Docker
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Instrucciones de uso
```

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
docker run -d -p 5000:5000 medical-model
```

Esto iniciará el servicio web en el puerto **5000**.

---

## 💻 Uso del Servicio

### 🧠 Opción 1: Interfaz Web

Abre tu navegador y visita:  
👉 [http://localhost:5000](http://localhost:5000)

Allí podrás ingresar tres valores numéricos (por ejemplo, `2.5`, `6.3`, `8.0`) y obtener un resultado de diagnóstico simulado.

---

### 🧩 Opción 2: API REST (JSON)

También puedes enviar los datos mediante una solicitud `POST` al endpoint `/api/predict`.

#### Ejemplo usando `curl`:

```bash
curl -X POST http://localhost:5000/api/predict      -H "Content-Type: application/json"      -d '{"values": [5.2, 7.1, 6.3]}'
```

#### Respuesta esperada:

```json
{"prediction": "ENFERMEDAD AGUDA"}
```

---

## 🧱 Descripción de Archivos

### `app.py`
Contiene el código principal del servicio Flask y una función llamada `predict_disease()` que simula el modelo.  
El diagnóstico se determina promediando los tres valores ingresados y clasificando el resultado según su magnitud.

### `Dockerfile`
Define la imagen de Docker que instala dependencias, copia los archivos y lanza la aplicación.

### `requirements.txt`
Lista las dependencias necesarias del proyecto (por ahora solo Flask).

---

## 🩺 Lógica de Clasificación Simulada

| Promedio de valores | Diagnóstico retornado |
|----------------------|-----------------------|
| < 3                 | `NO ENFERMO`          |
| 3 ≤ x < 6           | `ENFERMEDAD LEVE`     |
| 6 ≤ x < 8           | `ENFERMEDAD AGUDA`    |
| ≥ 8                 | `ENFERMEDAD CRÓNICA`  |

---

## 🧩 Posibles Extensiones

- Conectar el servicio con un modelo real de ML entrenado (archivo `.pkl` o `.onnx`).
- Implementar autenticación para acceso médico.
- Guardar registros de consultas en una base de datos.
- Desplegar el servicio con Docker Compose o en Kubernetes.

---

## 🧠 Conclusión

Este proyecto demuestra cómo **empaquetar un servicio de predicción médica simulado** dentro de una imagen Docker, permitiendo que cualquier médico o usuario pueda **ejecutarlo localmente** sin necesidad de configurar entornos de desarrollo.

---

**Autor:**  
Edwin Gómez
