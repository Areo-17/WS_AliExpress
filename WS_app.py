from flask import Flask, request, jsonify, render_template
from WS_product import *

app = Flask(__name__)
app.template_folder = 'static'

# Endpoint raíz que devuelve un mensaje de bienvenida
@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Obtiene los datos JSON enviados en la petición
    # Aquí puedes procesar los datos según sea necesario
    return jsonify({'message': 'Datos recibidos con éxito!', 'yourData': data})

@app.route('/Scrapping', methods=['POST'])
def exe_scrappeo():
    data = request.json
    url = data['url']
    print("Entro al metodo exe_scrappeo")
    if not url:
        return jsonify({'error': 'Falta la URL del producto'})
    # Valida la URL con regex o una biblioteca (opcional)
    result = Scrapper.all_attributes(url)
    return jsonify({'message': 'Your scrapping is starting...', 'results': result})

# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})

if __name__ == '__main__':
    app.run(debug=True)  # Inicia el servidor en modo de depuración
