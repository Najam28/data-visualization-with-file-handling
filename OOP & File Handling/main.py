from inventory_manager import InventoryManager
from product import Product

manager = InventoryManager()

products = manager.load_inventory()

manager.add_product(products, Product(1, "Laptop", 10, 999.99))
manager.add_product(products, Product(2, "Mouse", 50, 19.99))

products = manager.load_inventory()
manager.list_products(products)
