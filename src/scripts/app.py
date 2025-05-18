from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

FRASES = [
    "🌟 Cree en ti mismo y todo será posible.",
    "💪 El esfuerzo de hoy es el éxito de mañana.",
    "🚀 Nunca es tarde para empezar de nuevo.",
    "🔥 La disciplina supera al talento.",
    "🎯 La única manera de hacer un gran trabajo es amar lo que haces.",
]

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Frase Motivadora</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>
</head>
<body class="bg-light text-dark">
    <div class="container text-center mt-5">
        <h1>💡 Generador de Frases Motivadoras</h1>
        <p class="lead">Haz clic para inspirarte</p>
        <button class="btn btn-primary" onclick="generarFrase()">Generar</button>
        <div class="mt-4">
            <blockquote class="blockquote">
                <p id="frase">Aquí aparecerá tu frase...</p>
            </blockquote>
        </div>
    </div>

    <script>
        async function generarFrase() {
            const res = await fetch("/frase");
            const data = await res.json();
            document.getElementById("frase").textContent = data.frase;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/frase")
def frase():
    return jsonify({"frase": random.choice(FRASES)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
