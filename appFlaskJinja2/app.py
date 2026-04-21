from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Página principal para empresa de servicios
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # Captura los datos del formulario de contacto
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    servicio = request.form.get('servicio')s
    mensaje = request.form.get('mensaje')
    
    # Simulación de respuesta tras enviar el formulario
    return f"<h1>¡Gracias {nombre}!</h1><p>Hemos recibido tu mensaje sobre '{servicio}'. Te contactaremos a {email} pronto.</p><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True)