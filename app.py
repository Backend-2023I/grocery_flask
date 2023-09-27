from flask import Flask, request, jsonify
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery', methods=["GET"])
def all_grocery():
    """Get all grocery"""
    data = db.all()
    table = """
    <body>
    <h1>Grocery Store</h1>


    <table border='1px'>
    <tr>
        <td>name</td>
        <td>quantity</td>
        <td>price</td>
        <td>type</td>
    </tr>"""
    for i in data:
        name = i['name']
        quantity = i['quantity']
        price = i['price']
        type_ = i['type']
        
        s = f"""
        <tr>
            <td>{name}</td>
            <td>{quantity}</td>
            <td>{price}</td>
            <td>{type_}</td>
        </tr>"""

        table += s
    return table + "</table></body>"


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    
    data = request.json
    response = db.add(data)
    return response


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    data = db.get_by_type(type)
    return jsonify(data)


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    data = db.get_by_name(name)
    return jsonify(data)


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    data = db.get_by_price(price)
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)


# CRUD

# Create
# Read
# Update
# Delete