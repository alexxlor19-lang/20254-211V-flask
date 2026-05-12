# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

base_de_datos =["jorge", "pepe", "juanita"] #Modelos

@app.route("/index") #Controlador
def hello():
    return render_template(template_name_or_list="index.html") #View