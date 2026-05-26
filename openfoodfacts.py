import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def fetch_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "API request failed"}

    data = response.json()

    if data["status"] == 0:
        return {"error": "Product not found"}

    product = data["product"]

    return {
        "product_name": product.get("product_name"),
        "brands": product.get("brands"),
        "ingredients_text": product.get("ingredients_text")
    }