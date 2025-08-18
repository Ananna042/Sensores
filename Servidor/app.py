from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/sensor', methods=['POST'])
def process_sensor():
    data = request.json
    nombre = data.get ('ana')
    valor = data.get ('18')
    print(f"jelou{nombre} y {valor}")
    return 'ns'
 #hacer q los datos se guarden el una base de datos en tiempo real con current_timestamp
 #exportar el sql, la estructura

