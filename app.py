# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from flask import jsonify
import mercadopago

# Configurar las credenciales de MercadoPago
sdk = mercadopago.SDK("TEST-2777059790432441-111802-608eacf1e3130d411b343321d1a36107-34660496")

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar la sesión

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/supplements')
def supplements():
    return render_template('supplements.html')

@app.route('/foods')
def foods():
    return render_template('foods.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'
app.config['MAIL_PASSWORD'] = 'tu_contraseña'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Enviar el correo
        msg = Message(subject=subject,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=["health.and.wealth.cl@gmail.com"])
        msg.charset = 'utf-8'
        msg.body = f"Nombre: {name}\nCorreo: {email}\n\n{message}".encode('utf-8').decode('utf-8')
        mail.send(msg)

        return redirect(url_for('home'))

    return render_template('contact.html')

# Productos (se pueden reemplazar con una base de datos más adelante)
PRODUCTS = {
    'vitamina_c_zinc': {'name': 'Vitamina C + Zinc', 'price': 10.0},
    'magnesio': {'name': 'Magnesio', 'price': 8.0},
    'aceite_de_coco': {'name': 'Aceite de Coco', 'price': 15.0},
    'flores_de_jamaica': {'name': 'Flores de Jamaica', 'price': 12.0},
    'libro_frank_suarez': {'name': 'La Dieta del Metabolismo Acelerado', 'price': 20.0},
    'libro_dr_johnson': {'name': 'El Poder del Sistema Inmune', 'price': 25.0},
}

# Ruta para la página principal del carrito
@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    total = sum(PRODUCTS[product]['price'] * quantity for product, quantity in cart_items.items())
    return render_template('cart.html', cart_items=cart_items, products=PRODUCTS, total=total)

# Ruta para añadir productos al carrito
@app.route('/add_to_cart/<string:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart  # Actualizar la sesión
    total_items = sum(cart.values())
    return jsonify({'status': 'success', 'total_items': total_items})

# Ruta para vaciar el carrito
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

@app.route('/create-payment', methods=['POST'])
def create_payment():
    # Datos del pago
    preference_data = {
        "items": [
            {
                "title": "Compra en Health & Wellness",
                "quantity": 1,
                "unit_price": float(session.get('total', 0))  # Total del carrito
            }
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5000/success",
            "failure": "http://127.0.0.1:5000/failure",
            "pending": "http://127.0.0.1:5000/pending"
        },
        "auto_return": "approved",
    }

    # Crear preferencia
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return jsonify({"init_point": preference["init_point"]})

if __name__ == '__main__':
    print(app.url_map)  # Esto imprimirá todas las rutas registradas
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

