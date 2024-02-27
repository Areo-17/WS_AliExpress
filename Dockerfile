# Utiliza una imagen base de Python oficial
FROM python:3.12

WORKDIR /API

# Se copia el directorio local al del contenedor
COPY . .

# Se instalan librerias
RUN pip install -r requirements2.txt

EXPOSE 5000

# Se ejecuta la aplicacion de python
CMD ["python","WS_app.py"]