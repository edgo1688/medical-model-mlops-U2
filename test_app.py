"""
Pruebas unitarias para el servicio médico de diagnóstico
"""
import pytest
import json
from app import app, predict_disease, predictions_history, predictions_count


@pytest.fixture
def client():
    """
    Fixture que configura el cliente de pruebas Flask
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def reset_data():
    """
    Fixture que limpia los datos de estadísticas antes de cada prueba
    """
    predictions_history.clear()
    predictions_count.clear()
    yield
    predictions_history.clear()
    predictions_count.clear()


class TestPredictDisease:
    """
    Pruebas para la función predict_disease
    """
    
    def test_predict_no_enfermo(self, reset_data):
        """
        Prueba que la función clasifique correctamente como NO ENFERMO
        """
        # Valores que deberían dar un promedio < 2.5
        values = [1.0, 2.0, 1.5]  # Promedio = 1.5
        result = predict_disease(values, log=False)
        assert result == "NO ENFERMO"
    
    def test_predict_enfermedad_leve(self, reset_data):
        """
        Prueba que la función clasifique correctamente como ENFERMEDAD LEVE
        """
        # Valores que deberían dar un promedio entre 2.5 y 4.5
        values = [3.0, 3.5, 4.0]  # Promedio = 3.5
        result = predict_disease(values, log=False)
        assert result == "ENFERMEDAD LEVE"
    
    def test_predict_enfermedad_aguda(self, reset_data):
        """
        Prueba que la función clasifique correctamente como ENFERMEDAD AGUDA
        """
        # Valores que deberían dar un promedio entre 4.5 y 6.5
        values = [5.0, 5.5, 6.0]  # Promedio = 5.5
        result = predict_disease(values, log=False)
        assert result == "ENFERMEDAD AGUDA"
    
    def test_predict_enfermedad_cronica(self, reset_data):
        """
        Prueba que la función clasifique correctamente como ENFERMEDAD CRÓNICA
        """
        # Valores que deberían dar un promedio entre 6.5 y 8.5
        values = [7.0, 7.5, 8.0]  # Promedio = 7.5
        result = predict_disease(values, log=False)
        assert result == "ENFERMEDAD CRÓNICA"
    
    def test_predict_enfermedad_terminal(self, reset_data):
        """
        Prueba que la función clasifique correctamente como ENFERMEDAD TERMINAL
        """
        # Valores que deberían dar un promedio >= 8.5
        values = [9.0, 9.5, 10.0]  # Promedio = 9.5
        result = predict_disease(values, log=False)
        assert result == "ENFERMEDAD TERMINAL"
    
    def test_predict_invalid_values(self, reset_data):
        """
        Prueba que la función maneje correctamente valores inválidos
        """
        # Valores que no se pueden convertir a float
        values = ["abc", "def", "ghi"]
        result = predict_disease(values, log=False)
        assert "Error en los datos" in result
    
    def test_predict_logging_enabled(self, reset_data):
        """
        Prueba que el logging funcione correctamente cuando está habilitado
        """
        values = [3.0, 3.5, 4.0]
        result = predict_disease(values, log=True)
        
        # Verificar que se registró la predicción
        assert len(predictions_history) == 1
        assert predictions_count["ENFERMEDAD LEVE"] == 1
        assert predictions_history[0]["result"] == "ENFERMEDAD LEVE"
        assert predictions_history[0]["values"] == [3.0, 3.5, 4.0]
    
    def test_predict_logging_disabled(self, reset_data):
        """
        Prueba que el logging no funcione cuando está deshabilitado
        """
        values = [3.0, 3.5, 4.0]
        result = predict_disease(values, log=False)
        
        # Verificar que NO se registró la predicción
        assert len(predictions_history) == 0
        assert predictions_count["ENFERMEDAD LEVE"] == 0


class TestAPIEndpoints:
    """
    Pruebas para los endpoints de la API
    """
    
    def test_api_predict_success(self, client, reset_data):
        """
        Prueba que el endpoint /api/predict funcione correctamente
        """
        data = {"values": [3.0, 3.5, 4.0]}
        response = client.post('/api/predict', 
                              data=json.dumps(data),
                              content_type='application/json')
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["prediction"] == "ENFERMEDAD LEVE"
    
    def test_api_predict_invalid_data(self, client, reset_data):
        """
        Prueba que el endpoint /api/predict maneje datos inválidos
        """
        data = {"values": ["abc", "def", "ghi"]}
        response = client.post('/api/predict', 
                              data=json.dumps(data),
                              content_type='application/json')
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert "Error en los datos" in json_data["prediction"]
    
    def test_api_stats_empty(self, client, reset_data):
        """
        Prueba que el endpoint /api/stats funcione cuando no hay datos
        """
        response = client.get('/api/stats')
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["total_predictions"] == 0
        assert json_data["predictions_by_category"] == {}
        assert json_data["last_predictions"] == []
        assert json_data["last_prediction_date"] is None
    
    def test_api_stats_with_data(self, client, reset_data):
        """
        Prueba que el endpoint /api/stats funcione con datos
        """
        # Primero hacer algunas predicciones
        data1 = {"values": [1.0, 2.0, 1.5]}  # NO ENFERMO
        data2 = {"values": [3.0, 3.5, 4.0]}  # ENFERMEDAD LEVE
        
        client.post('/api/predict', data=json.dumps(data1), content_type='application/json')
        client.post('/api/predict', data=json.dumps(data2), content_type='application/json')
        
        # Obtener estadísticas
        response = client.get('/api/stats')
        
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["total_predictions"] == 2
        assert json_data["predictions_by_category"]["NO ENFERMO"] == 1
        assert json_data["predictions_by_category"]["ENFERMEDAD LEVE"] == 1
        assert len(json_data["last_predictions"]) == 2
        assert json_data["last_prediction_date"] is not None
    
    def test_home_page(self, client):
        """
        Prueba que la página principal cargue correctamente
        """
        response = client.get('/')
        assert response.status_code == 200
        assert b'Servicio de Diagn' in response.data
        assert b'form' in response.data
    
    def test_stats_page_empty(self, client, reset_data):
        """
        Prueba que la página de estadísticas funcione sin datos
        """
        response = client.get('/stats')
        assert response.status_code == 200
        assert b'No hay predicciones registradas' in response.data
    
    def test_stats_page_with_data(self, client, reset_data):
        """
        Prueba que la página de estadísticas funcione con datos
        """
        # Hacer una predicción primero
        data = {"values": [3.0, 3.5, 4.0]}
        client.post('/api/predict', data=json.dumps(data), content_type='application/json')
        
        response = client.get('/stats')
        assert response.status_code == 200
        # Convertir la respuesta a string para evitar problemas de codificación
        response_text = response.data.decode('utf-8')
        assert 'Total de predicciones realizadas:</strong> 1' in response_text
        assert 'ENFERMEDAD LEVE' in response_text


if __name__ == "__main__":
    pytest.main([__file__])