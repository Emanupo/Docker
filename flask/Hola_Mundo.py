from flask import Flask

app = Flask(__name__)#Nuevo objeto, resive como parametro name
@app.route('/')#Necesitamos un wrap o un decorador
def index(): #Funcion
    return "Hola mundo"#Regresar un string
app.run()#Ejecutar el servidor por default en elpuerto 5000