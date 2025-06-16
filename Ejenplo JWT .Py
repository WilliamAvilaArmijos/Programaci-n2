from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
CLAVE_SECRETA = "mi_clave_super_segura"

# Usuario simulado (puede reemplazarse con una base de datos real)
USUARIO_FICTICIO = {
    "usuario": "admin",
    "contraseña": "1234"
}

# Ruta para iniciar sesión y obtener el token
@app.route("/iniciar_sesion", methods=["POST"])
def iniciar_sesion():
    datos = request.get_json()
    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if usuario == USUARIO_FICTICIO["usuario"] and contraseña == USUARIO_FICTICIO["contraseña"]:
        # Crear token con expiración de 1 minutos
        payload = {
            "usuario": usuario,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
        }
        token = jwt.encode(payload, CLAVE_SECRETA, algorithm="HS256")
        return jsonify({"mensaje": "Inicio de sesión exitoso", "token": token})
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401

# Ruta protegida (requiere token válido)
@app.route("/zona_segura", methods=["GET"])
def zona_segura():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "No se proporcionó el token"}), 403

    try:
        decoded = jwt.decode(token, CLAVE_SECRETA, algorithms=["HS256"])
        fecha_expiracion = datetime.datetime.utcfromtimestamp(decoded["exp"]).strftime("%Y-%m-%d %H:%M:%S")
        return jsonify({
            "mensaje": f" Acceso permitido. Bienvenido, {decoded['usuario']}.",
            "token_expira": f" Este token vence el {fecha_expiracion} UTC"
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"error": " El token ha expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": " Token inválido"}), 401

# Ejecutar la aplicación
if __name__ == "__main__":
    if __name__ == "__main__":
     print(" Servidor Flask iniciado correctamente en http://127.0.0.1:5000")
     print("  Modo depuración activado")
     print(" Recuerda: este servidor es solo para desarrollo, no para producción.")
    app.run(debug=True)

    app.run(debug=True)
