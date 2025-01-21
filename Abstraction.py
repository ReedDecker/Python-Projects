from abc import ABC, abstractmethod #Import ABC method "Abstract Base Class"

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    def regular_method(self):
        print(f"This is a regular method in the {self.name} class.")

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Create an instance of the Square class
square = Square("Square", 25)

# Call both the regular and abstract methods
square.regular_method()
print(f"The area of the square is {square.area()}.")
