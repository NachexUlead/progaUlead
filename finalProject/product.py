class Product:
    def __init__(self, name:str, code:str, price:float):
        self.name = name
        self.code = code
        self.price = price
    
    def setName(self, name:str):
        self.name = name

    def getName(self)->str:
        return self.name
    
    def setCode(self, code:str):
        self.code = code

    def getCode(self)->str:
        return self.code

    def setPrice(self, price:float):
        self.price = price

    def getPrice(self)->float:
        return self.price