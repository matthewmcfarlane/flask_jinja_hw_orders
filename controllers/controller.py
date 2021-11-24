from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def index ():
    return render_template('index.html', title= 'Customer Orders',orders=orders)

@app.route('/orders/<id>')
def order (id):
    id_int = int(id)
    for order in orders:
        if order.order_id == id_int:
            return render_template('order.html', title=f"Order {id_int}", order=order)
