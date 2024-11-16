from flask import Flask, request, jsonify, render_template
import products_doa
import orders_doa
import uom_doa
from sql_connection import get_sql_connection
import json  # Import json module

app = Flask(__name__)

# Ensure SQL connection is established
connection = get_sql_connection()

@app.route('/')
def index():
    return render_template('index.html')

# Define route for managing products page
@app.route('/manage-products')
def manage_products():
    return render_template('manage-products.html')

# Define route for orders page
@app.route('/orders')
def orders():
    return render_template('order.html')

# Endpoint to get all products (for API purposes)
@app.route('/getproducts', methods=['GET'])
def get_products():
    products = products_doa.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to get all UOMs (for API purposes)
@app.route('/getuom', methods=['GET'])
def get_uom():
    uoms = uom_doa.get_uoms(connection)  # Corrected from uom_dao to uom_doa
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to insert a new product
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_doa.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to get all orders
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    orders = orders_doa.get_all_orders(connection)  # Corrected from orders_dao to orders_doa
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to insert a new order
@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_doa.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to delete a product
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_doa.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask server for grocery store management system")
    app.run(debug=True)

