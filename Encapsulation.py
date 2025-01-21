class MyClass:
    def __init__(self):
        self._protected_var = 476  # Protected variable
        self.__private_var = 1295   # Private variable

    def _protected_method(self):  # Protected method
        print("Protected method called 476")

    def __private_method(self):   # Private method
        print("Private method called 1295")

    def access_private(self):
        self.__private_method()


obj = MyClass() # Create an object of the class

# Access protected members
print(obj._protected_var) 
obj._protected_method()    # Calling protected method

print(obj._MyClass__private_var) 
obj.access_private()  # Accessing private method
