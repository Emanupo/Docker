from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def index():
    return "Hola mundo"
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
#params/libros/1
def params(name='Esto es un valor por default', num='Nada'):
    return "El parametro es: {} {}".format(name, num)

if __name__ == '__main__':
    app.run(debug=True, port= 8000)