
class Product:
    def __init__(self, Product_name, Product_price):
        self.Product_name = Product_name
        self.Product_price = Product_price
        
    def get_name(self):
        return self.Product_name
    
    def set_name(self,name):
        self.Product_name = name

p1 = Product("Laptop", 999.99)
print(p1.get_name())  # Output: Laptop
p1.set_name("Gaming Laptop")
print(p1.get_name())  # Output: Gaming Laptop
print(p1.Product_price)  # Output: 999.99

p2=Product(Product_name="Smartphone", Product_price=499.99)
print(p2.get_name())  # Output: Smartphone
print(p2.Product_price)  # Output: 499.99

class Node:
    def __init__(self, Product_name, Product_price):
        self.Product_name = Product_name
        self.Product_price = Product_price
        self.next = None
        
# solid principle guide on  how well structure your code and 
# make it more efficient and readable.
# It stands for Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation,
# and Dependency Inversion. By following these principles,
# you can create code that is easier to maintain and extend in the future.        
            
# substitution principle states that objects of a superclass should be replaceable with 
# objects of a subclass without affecting the correctness of the program. 
# This means that if you have a class hierarchy, you should be able to use an instance of a 
# subclass wherever an instance of the superclass is expected, without causing any issues. 
# This promotes code reusability and flexibility in your design.
    
# interface segregation principle states that clients should not 
# be forced to depend on interfaces they do not use. 
# This means that you should create specific interfaces for
# different functionalities, rather than having a single interface that includes all methods.
# This allows clients to only implement the methods they need, making the code more modular and 
# easier to maintain.

# dependency inversion principle states that high-level modules should not 
# depend on low-level modules. Instead, both should depend on abstractions. 
# This means that you should rely on interfaces or 
# abstract classes rather than concrete implementations. 
# This promotes loose coupling and 
# makes it easier to change the implementation without affecting the high-level code.        