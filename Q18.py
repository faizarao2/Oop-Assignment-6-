# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and 
# @price.deleter to delete it.



class Product:
    def __init__(self , price):
        self._price = price


    #getter method
    @property
    def get_price(self):
        print("getting price")
        return self._price
    
    #@property.setter
    @get_price.setter
    def set_price(self, value):
        print(f"Updated price {self._price} to {value}")
        if value is None:
            raise ValueError("price cannot be None.")
        self._price= value

    #deleter method
    @set_price.deleter
    def price(self):
        print(f"Deleted price {self._price} ")
        del self._price


product = Product(500)

print(product.price)          # calls @property
product.price = 1000     # calls @setter
del product.price            # calls @deleter