from app import app
from flask import render_template
from models.order_list import order_list
@app.route('/')
def index():
    return "Goodmorning gurl, nemo is intown!!"
    

@app.route('/orders')
def show_orders():
    return render_template('index.html', title='Orders', order_list=order_list) 

@app.route('/order/<int:order_id>')
def show_order(order_id):
    order = order_list[order_id]
    return render_template('order.html', order=order)