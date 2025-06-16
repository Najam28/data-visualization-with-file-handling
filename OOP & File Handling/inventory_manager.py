import json
from product import Product

class InventoryManager:
    def __init__(self, filename="inventory.json"):
        self.filename = filename

    def save_inventory(self, products):
        with open(self.filename, 'w') as f:
            json.dump([p.to_dict() for p in products], f, indent=2)

    def load_inventory(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Product.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def add_product(self, products, product):
        products.append(product)
        self.save_inventory(products)

    def list_products(self, products):
        for p in products:
            print(f"{p.name} | ID: {p.product_id} | Qty: {p.quantity} | Price: ${p.price:.2f}")

    