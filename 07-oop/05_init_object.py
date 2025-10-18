class ChaiOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())

# __init_ method is called automatically when a new instance of the class is created.
# It initializes the object's attributes with the provided values.
# The 'self' parameter refers to the instance being created.
# Attributes 'type' and 'size' are set for each instance based on the arguments passed during instantiation.
# The summary method uses these attributes to return a formatted string describing the chai order.
# Each instance of ChaiOrder has its own 'type' and 'size' attributes.
# This allows for creating multiple chai orders with different types and sizes.
# The __init__ method is not called explicitly; it's invoked automatically when creating a new instance of the class.
# The 'self' parameter is a reference to the current instance of the class and is used to access attributes and methods associated with that instance.
