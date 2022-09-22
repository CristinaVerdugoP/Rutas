from flask import Flask, render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('index.html')

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<string:nombre>')
def say(nombre):
    return "Hola, " + nombre

@app.route('/repeat/<int:numero>/<string:nombre>')
def repeat(nombre, numero):
    return (nombre * numero)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404