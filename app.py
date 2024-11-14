# app.py
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
