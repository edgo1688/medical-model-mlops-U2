from flask import Flask, request, jsonify
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

# Sistema de almacenamiento en memoria para estadísticas
predictions_history = []
predictions_count = defaultdict(int)

def log_prediction(values, result):
    """
    Registra una predicción en el historial para estadísticas
    """
    prediction_record = {
        "timestamp": datetime.now().isoformat(),
        "values": values,
        "result": result
    }
    predictions_history.append(prediction_record)
    predictions_count[result] += 1

def predict_disease(values, log=True):
    """
    Simula la predicción de una enfermedad a partir de 3 valores.
    Los valores pueden representar, por ejemplo, niveles de glucosa, presión y temperatura.
    Un paciente puede ser clasificado en una de estas 5 categorías: NO ENFERMO, ENFERMEDAD LEVE, ENFERMEDAD AGUDA, ENFERMEDAD CRÓNICA, ENFERMEDAD TERMINAL
    """
    try:
        glucosa, presion, temperatura = map(float, values)
        score = (glucosa + presion + temperatura) / 3

        if score < 2.5:
            result = "NO ENFERMO"
        elif score < 4.5:
            result = "ENFERMEDAD LEVE"
        elif score < 6.5:
            result = "ENFERMEDAD AGUDA"
        elif score < 8.5:
            result = "ENFERMEDAD CRÓNICA"
        else:
            result = "ENFERMEDAD TERMINAL"
        
        # Registrar la predicción válida en el historial
        if log:
            log_prediction([glucosa, presion, temperatura], result)
        
        return result
    except Exception as e:
        return f"Error en los datos: {str(e)}"

@app.route("/")
def home():
    return """
    <h2>🩺 Servicio de Diagnóstico Médico (Simulado)</h2>
    <form action="/predict" method="post">
        <label>Glucosa:</label><input name="glucosa" type="number" step="any"><br>
        <label>Presión:</label><input name="presion" type="number" step="any"><br>
        <label>Temperatura:</label><input name="temperatura" type="number" step="any"><br>
        <input type="submit" value="Predecir">
    </form>
    <hr>
    <p><a href="/stats">📊 Ver Estadísticas de Predicciones</a></p>
    """

@app.route("/predict", methods=["POST"])
def predict():
    glucosa = request.form.get("glucosa")
    presion = request.form.get("presion")
    temperatura = request.form.get("temperatura")
    result = predict_disease([glucosa, presion, temperatura])
    return f"<h3>Resultado: {result}</h3><a href='/'>Volver</a><br><a href='/stats'>Ver Estadísticas</a>"

@app.route("/stats")
def stats():
    """
    Interfaz web para mostrar estadísticas de predicciones
    """
    if not predictions_history:
        return """
        <h2>📊 Estadísticas de Predicciones</h2>
        <p>No hay predicciones registradas aún.</p>
        <a href='/'>Volver al inicio</a>
        """
    
    # Obtener estadísticas
    total = len(predictions_history)
    last_predictions = predictions_history[-5:] if len(predictions_history) >= 5 else predictions_history.copy()
    last_prediction_date = predictions_history[-1]["timestamp"] if predictions_history else "N/A"
    
    # Construir HTML para categorías
    categories_html = ""
    for category, count in predictions_count.items():
        categories_html += f"<li><strong>{category}</strong>: {count} predicciones</li>"
    
    # Construir HTML para últimas predicciones
    recent_html = ""
    for pred in reversed(last_predictions):  # Mostrar las más recientes primero
        values_str = f"Glucosa: {pred['values'][0]}, Presión: {pred['values'][1]}, Temperatura: {pred['values'][2]}"
        recent_html += f"<li><strong>{pred['result']}</strong> - {values_str} <br><small>Fecha: {pred['timestamp']}</small></li>"
    
    return f"""
    <h2>📊 Estadísticas de Predicciones Médicas</h2>
    
    <h3>📈 Resumen General</h3>
    <p><strong>Total de predicciones realizadas:</strong> {total}</p>
    <p><strong>Fecha de última predicción:</strong> {last_prediction_date}</p>
    
    <h3>📊 Predicciones por Categoría</h3>
    <ul>{categories_html}</ul>
    
    <h3>🕒 Últimas {len(last_predictions)} Predicciones</h3>
    <ol>{recent_html}</ol>
    
    <hr>
    <p><a href='/'>🏠 Volver al inicio</a> | <a href='/api/stats'>📋 Ver datos en JSON</a></p>
    """

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    Endpoint para enviar los valores en formato JSON:
    {
        "values": [glucosa, presion, temperatura]
    }
    Ejemplo: {"values": [4.5, 6.2, 5.9]}
    """
    data = request.get_json()
    values = data.get("values", [])
    result = predict_disease(values)
    return jsonify({"prediction": result})

@app.route("/api/stats", methods=["GET"])
def api_stats():
    """
    Endpoint que retorna estadísticas de las predicciones realizadas:
    - Número total de predicciones por categoría
    - Últimas 5 predicciones realizadas
    - Fecha de la última predicción
    """
    # Obtener las últimas 5 predicciones
    last_predictions = predictions_history[-5:] if len(predictions_history) >= 5 else predictions_history.copy()
    
    # Obtener la fecha de la última predicción
    last_prediction_date = predictions_history[-1]["timestamp"] if predictions_history else None
    
    # Preparar estadísticas
    stats = {
        "total_predictions": len(predictions_history),
        "predictions_by_category": dict(predictions_count),
        "last_predictions": last_predictions,
        "last_prediction_date": last_prediction_date
    }
    
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)