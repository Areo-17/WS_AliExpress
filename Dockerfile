# Utiliza una imagen base de Python oficial
FROM python

WORKDIR /API

# Se copia el directorio local al del contenedor
COPY . /API/

# Se instalan librerias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Se ejecuta la aplicacion de python
CMD ["python","WS_app.py"]