from flask import Flask, request, jsonify

app = Flask(__name__)

def predict_disease(values):
    """
    Simula la predicción de una enfermedad a partir de 3 valores.
    Los valores pueden representar, por ejemplo, niveles de glucosa, presión y temperatura.
    Un paciente puede ser clasificado en una de estas 5 categorías: NO ENFERMO, ENFERMEDAD LEVE, ENFERMEDAD AGUDA, ENFERMEDAD CRÓNICA, ENFERMEDAD TERMINAL
    """
    try:
        glucosa, presion, temperatura = map(float, values)
        score = (glucosa + presion + temperatura) / 3

        if score < 2.5:
            return "NO ENFERMO"
        elif score < 4.5:
            return "ENFERMEDAD LEVE"
        elif score < 6.5:
            return "ENFERMEDAD AGUDA"
        elif score < 8.5:
            return "ENFERMEDAD CRÓNICA"
        else:
            return "ENFERMEDAD TERMINAL"
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
    """

@app.route("/predict", methods=["POST"])
def predict():
    glucosa = request.form.get("glucosa")
    presion = request.form.get("presion")
    temperatura = request.form.get("temperatura")
    result = predict_disease([glucosa, presion, temperatura])
    return f"<h3>Resultado: {result}</h3><a href='/'>Volver</a>"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)