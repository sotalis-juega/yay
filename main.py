from flask import Flask
import random
app = Flask(__name__)
facts = ["Pérdida de control: Dificultad para limitar el tiempo de uso de dispositivos, incluso cuando se intenta.", 
        "Negligencia de responsabilidades: Descuido de tareas laborales, académicas o familiares. ",
        "Irritabilidad o ansiedad: Reacciones emocionales negativas al no poder acceder a la tecnología. "]
h1 =  "<h1>Hello, World!</h1>"
h2 =  "<h2>DEPENDENCIAS TECNOLOGICAS Y SUS CONSECUENCIAS</h2>"
p =  "<p>esto es real</p>"
a =  "<a href = '/factos'> esto es un facto factible factorizable</a>"
@app.route("/")
def hello_world():
    return h1 + h2 + p + a
@app.route("/factos")
def facto():
    fact = f"<li>EJEMPLO DE CONSECUENCIA: {random.choice(facts)}</li>"
    fact2 = f"<li>EJEMPLO DE CONSECUENCIA: {random.choice(facts)}</li>"
    fact3 = f"<li>EJEMPLO DE CONSECUENCIA: {random.choice(facts)}</li>"
    return h2 + fact + fact2 + fact3
app.run(debug = True)