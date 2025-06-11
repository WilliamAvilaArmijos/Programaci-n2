import sqlite3
import re
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

conn = sqlite3.connect(':memory:',  check_same_thread=False)
cursor = conn.cursor()

# Creación de una tabla de usuarios
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', '1234')") 
cursor.execute("INSERT INTO users VALUES ('admin2', '1234')") 
cursor.execute("INSERT INTO users VALUES ('admin3', '1234')") 
cursor.execute("INSERT INTO users VALUES ('admin4', '1234')") 
cursor.execute("INSERT INTO users VALUES ('admin5', '1234')") 
cursor.execute("INSERT INTO users VALUES ('admin6', '1234')")

conn.commit()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Obtener datos del formulario
        
        regex = r"[A-Za-z]"
    # Pedir el nombre de usuario hasta que sea válido
        while True:
            username = request.form.get("username")
            if re.match(regex, username):
                print("Entrada válida.")
                break  # Salir del bucle si la entrada es válida
            else:
                return render_template("login.html", error="No se admiten caracteres especiales")
        password = request.form.get("password")

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        #' OR '1'='1' --  

        cursor.execute(query)
        result = cursor.fetchall()

        # Validar credenciales
        if result:
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos.")

    return render_template("login.html")

@app.route("/welcome")
def welcome():
    return "Bienvenido al sistema seguro."

if __name__ == "__main__":
    app.run(debug=True)
