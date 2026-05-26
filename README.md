Inventory Management System
A simple, lightweight Flask-based inventory management system featuring standard CRUD operations, a CLI interface, and real-time OpenFoodFacts API integration.

Features
Complete CRUD: View, add, update, and delete inventory items.

Smart Integration: Fetch real-time product data directly from the OpenFoodFacts API.

Dual Interface: Interact via a RESTful Flask API or a user-friendly CLI.

Reliable: Fully covered by unit tests using pytest (including external API mocking).

Project Structure
Plaintext
inventory-system/
│
├── app.py                 # Flask API main application
├── cli.py                 # Command-line interface script
├── openfoodfacts.py       # OpenFoodFacts API wrapper
├── test_app.py            # Pytest test suite
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
└── data/
    └── mock_data.py       # Local mock database

Setup & Installation
1. Clone & Navigate
Bash
git clone <https://github.com/sharonbochaberi-oss/inventory-system.git>
cd inventory-system

2. Set Up Virtual Environment
Bash
# Create environment
python3 -m venv venv

# Activate
source venv/bin/activate


3. Install Dependencies
Bash
pip install flask requests pytest

Running the Application
Start the Flask API
Bash
python3 app.py
The server will run locally at: http://127.0.0.1:5000

Launch the CLI (In a separate terminal)
Bash
source venv/bin/activate
python3 cli.py

Run Tests
Bash
pytest

API Endpoints
Method	Endpoint	Description
GET	/inventory	Retrieve all inventory items
GET	/inventory/<id>	Retrieve a specific item
POST	/inventory	Add a new product
PATCH	/inventory/<id>	Update stock and/or price
DELETE	/inventory/<id>	Remove an item

Sample JSON Payloads
POST /inventory (Add Item)

JSON
{
  "barcode": "123456",
  "product_name": "Test Product",
  "brand": "Test Brand",
  "price": 9.99,
  "stock": 20,
  "ingredients": "Sugar"
}

PATCH /inventory/<id> (Update Item)

JSON
{
  "price": 12.99,
  "stock": 50
}

 CLI Usage Options
Running python3 cli.py presents the following menu:

Plaintext
1. View Inventory
2. Add Item
3. Update Item
4. Delete Item
5. Find Product From API (OpenFoodFacts)
6. Exit

 Author
Ouko Sharon Bochaberi