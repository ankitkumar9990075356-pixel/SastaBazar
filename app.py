from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Mock Data for "Saste Products"
products = [
    {"id": 1, "name": "Wireless Earbuds", "price": 299, "original_price": 999, "image": "/static/images/earbuds.png", "category": "Electronics", "description": "High-fidelity sound with Active Noise Cancellation. 24-hour battery life and water resistance."},
    {"id": 2, "name": "Smart Watch", "price": 499, "original_price": 1499, "image": "/static/images/smart_watch.png", "category": "Electronics", "description": "Track fitness, heart rate, and sleep. OLED display with customizable watch faces."},
    {"id": 3, "name": "Running Shoes", "price": 350, "original_price": 899, "image": "/static/images/running_shoes.png", "category": "Fashion", "description": "Lightweight breathable mesh with shock-absorbing soles for maximum comfort."},
    {"id": 4, "name": "Cotton T-Shirt", "price": 99, "original_price": 299, "image": "https://placehold.co/300x300/1e1e1e/ff4757?text=T-Shirt", "category": "Fashion", "description": "100% Premium Cotton. Soft, durable, and perfect for everyday wear."},
    {"id": 5, "name": "Sunglasses", "price": 149, "original_price": 599, "image": "/static/images/sunglasses.png", "category": "Accessories", "description": "Classic Aviator style with UV400 protection and scratch-resistant lenses."},
    {"id": 6, "name": "Backpack", "price": 399, "original_price": 1200, "image": "https://placehold.co/300x300/1e1e1e/ff4757?text=Bag", "category": "Accessories", "description": "Water-resistant travel backpack with laptop compartment and USB charging port."},
    {"id": 7, "name": "Gaming Mouse", "price": 199, "original_price": 500, "image": "https://placehold.co/300x300/1e1e1e/ff4757?text=Mouse", "category": "Electronics", "description": "RGB Gaming Mouse with adjustable DPI and ergonomic design for pro gamers."},
    {"id": 8, "name": "Phone Case", "price": 49, "original_price": 199, "image": "https://placehold.co/300x300/1e1e1e/ff4757?text=Phone+Case", "category": "Accessories", "description": "Shock-proof protection case with slim profile and anti-slip grip."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    # In a real app, save to database here
    print(f"Order received: {data}")
    return jsonify({"success": True, "message": "Order placed successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
