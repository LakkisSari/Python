class Product:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price * discount/100
        
p1 = Product("Lenovo", 1200)
print(p1.brand, "original price: ", p1.price)

p1.price = 1400 #modifying price

p1.apply_discount(50) #applying discount
print("Price after discount: ", p1.price)