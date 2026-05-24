# Archivo inicio.py
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Datos de usuarios (simulados para el ejemplo)

USUARIOS = {
    'usuario1': 'u1',
    'usuario2': 'u2'
}


@app.route('/inicio')
def inicio():
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('usuario')
        password = request.form.get('contrasena')
        if username in USUARIOS and USUARIOS[username] == password:
            # Iniciar sesión exitosa, redirigir a otra página
            return redirect(url_for('inicio'))
        else:
            # Credenciales incorrectas, mostrar mensaje de error
            return 'Credenciales incorrectas. <a href="/login">Intenta de nuevo</a>'
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)