from flask import Flask, jsonify, request
from data.mock_data import inventory

app = Flask(__name__)

@app.route('/')
def home():
    return "Inventory API is running!"

# GET all inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

# GET single item
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)

    if item:
        return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

# POST new item
@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "barcode": data.get("barcode"),
        "product_name": data.get("product_name"),
        "brand": data.get("brand"),
        "price": data.get("price"),
        "stock": data.get("stock"),
        "ingredients": data.get("ingredients")
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

# PATCH item
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json

    item.update(data)

    return jsonify(item)

# DELETE item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)

    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)