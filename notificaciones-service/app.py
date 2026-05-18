from flask import Flask, jsonify
from flask_cors import CORS

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

CORS(app)

metrics = PrometheusMetrics(app)

@app.route('/')
def inicio():

    return "Microservicio de notificaciones funcionando"

@app.route('/notificacion')
def notificacion():

    return jsonify({
        "mensaje": "Nueva Notificacion"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)