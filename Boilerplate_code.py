#Importar el módulo Flask en el proyecto.
from flask import Flask, render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)

@app.route("/")
def student_webpage():
    name = "Danna"
    return render_template("home.html", student_name=name)


#La función route() de la clase Flask.
#@app.route("/home")

#‘/’ URL está vinculado con la función first_flask.
#def first_flask():

    #return "Este es mi primer programa en Flask"

#Ejecutamos la app en el servidor local.
if __name__ == '__name__':
    app.run()
