from flask import Flask
from flask import request
#http://127.0.0.1:8000/params?params1=Emanuel_Bustamante
#http://127.0.0.1:8000/params
app = Flask(__name__)
@app.route('/')
def index():
    return "Hola mundo"
@app.route('/saluda')
def saluda():
    return "Buenas vaquero"
@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    return "El parametro es: {}".format(param)
if __name__ == '__main__':
    app.run(debug=True, port= 3000)