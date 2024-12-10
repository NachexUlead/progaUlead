from product import Product
from taxes import calculateTax, validateState

class PurchaseOrder:
    def __init__(self, products:list[Product]):
        self.products = products
    
    def getProducts(self)->list[Product]:
        return self.products
    
    def listProducts(self):
        return [product.getName() for product in self.products]
    
    def calculateFinalPrice(self, state:str)->float:
        if not validateState(state):
            raise ValueError(f"error: invalid state: {state}")

        total = sum([product.getPrice() for product in self.products])
        tax = calculateTax(state, total)
        return total + tax