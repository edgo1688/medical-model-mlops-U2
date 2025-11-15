# Imagen base
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR .

# Copiar archivos del proyecto
COPY requirements.txt .
COPY app.py .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Flask
EXPOSE 5001

# Comando para ejecutar el servicio
CMD ["python", "app.py"]