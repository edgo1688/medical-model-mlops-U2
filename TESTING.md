# 🧪 Testing y CI/CD - Sistema Médico

## 📋 Resumen de Pruebas Implementadas

Este proyecto incluye un sistema completo de **pruebas unitarias** y **CI/CD con GitHub Actions** que garantiza la calidad y funcionalidad del servicio médico.

### 🔬 Pruebas Unitarias (`test_app.py`)

#### **Pruebas de la Función `predict_disease()`:**
1. **test_predict_no_enfermo** - Verifica clasificación correcta para pacientes sanos
2. **test_predict_enfermedad_leve** - Valida diagnóstico de enfermedad leve
3. **test_predict_enfermedad_aguda** - Confirma detección de enfermedad aguda
4. **test_predict_enfermedad_cronica** - Prueba clasificación de enfermedad crónica
5. **test_predict_enfermedad_terminal** - Verifica detección de casos terminales
6. **test_predict_invalid_values** - Manejo de datos inválidos
7. **test_predict_logging_enabled** - Sistema de registro activado
8. **test_predict_logging_disabled** - Sistema de registro desactivado

#### **Pruebas de Endpoints de API:**
1. **test_api_predict_success** - API de predicción funcionando correctamente
2. **test_api_predict_invalid_data** - Manejo de datos inválidos en API
3. **test_api_stats_empty** - API de estadísticas sin datos
4. **test_api_stats_with_data** - API de estadísticas con datos
5. **test_home_page** - Página principal funcional
6. **test_stats_page_empty** - Página de estadísticas sin datos
7. **test_stats_page_with_data** - Página de estadísticas con datos

### 🚀 GitHub Actions CI/CD

#### **Workflow Configurado** (`.github/workflows/workflow.yaml`):

**Trigger:** Pull Requests hacia la rama `main`

**Pasos del Pipeline:**
1. **Comentario Inicial** - "CI/CD en acción. Ejecutando tareas..."
2. **Checkout del Código** - Obtiene el código del PR
3. **Setup Python 3.9** - Configura el entorno Python
4. **Instalación de Dependencias** - Instala Flask, pytest, pytest-flask
5. **Ejecución de Pruebas** - Ejecuta todas las 15 pruebas unitarias
6. **Comentario de Éxito** - "CI/CD terminado con éxito." (si pasan todas las pruebas)
7. **Comentario de Fallo** - Mensaje de error (si fallan las pruebas)

### 📊 Cobertura de Pruebas

- ✅ **100% de funciones críticas cubiertas**
- ✅ **Todos los endpoints de API probados**
- ✅ **Manejo de errores validado**
- ✅ **Sistema de estadísticas verificado**
- ✅ **Interfaz web funcional**

### 🛠️ Ejecutar Pruebas Localmente

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todas las pruebas
pytest test_app.py -v

# Ejecutar pruebas con coverage
pytest test_app.py -v --cov=app
```

### 🔧 Dependencias de Testing

```txt
flask==3.0.3
pytest==7.4.3
pytest-flask==1.3.0
```

### 📈 Beneficios del Sistema CI/CD

1. **Calidad Garantizada** - No se puede hacer merge sin pasar las pruebas
2. **Feedback Inmediato** - Comentarios automáticos en PRs
3. **Prevención de Bugs** - Detección temprana de problemas
4. **Confianza en Despliegues** - Código validado antes de producción
5. **Documentación Automática** - Resultados visibles en cada PR

---

🎯 **Resultado:** Sistema robusto de 15 pruebas unitarias con CI/CD completamente automatizado para garantizar la calidad del servicio médico de diagnóstico.