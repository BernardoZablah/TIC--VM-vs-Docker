from flask import Flask, jsonify, render_template_string
import time
import psutil

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Monitor del Sistema</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>
</head>
<body class="bg-dark text-white">
    <div class="container mt-5 text-center">
        <h1>Monitor del Sistema</h1>
        <p class="lead">Consulta el uso actual de CPU y el tiempo desde que inició el servidor.</p>
        <button class="btn btn-success mb-3" onclick="obtenerDatos()">Actualizar</button>
        <div>
            <p><strong>Tiempo activo del servidor:</strong> <span id="uptime">-</span> segundos</p>
            <p><strong>Uso de CPU:</strong> <span id="cpu">-</span>%</p>
        </div>
    </div>

    <script>
        async function obtenerDatos() {
            const res = await fetch("/stats");
            const data = await res.json();
            document.getElementById("uptime").textContent = data.uptime;
            document.getElementById("cpu").textContent = data.cpu_percent;
        }
    </script>
</body>
</html>
"""

start_time = time.time()

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/stats")
def stats():
    uptime = round(time.time() - start_time, 2)
    cpu = psutil.cpu_percent(interval=0.2)
    return jsonify({
        "uptime": uptime,
        "cpu_percent": cpu
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
