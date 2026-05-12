# save this as app.py
from flask import Flask

app = Flask(__name__)

base_de_datos =["jorge", "pepe"; "juanita"] #Modelos

@app.route("/") #Controlador
def hello():
    return render_template(template_name_or_lista="index.html") #View