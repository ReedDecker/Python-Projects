




class Vehicle:
    def __init__(self, make, model):    # Vehicle is Parent Class #
        self.make = make
        self.model = model

    def description(self):
        return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, doors):   # Car is Child Class #
        super().__init__(make, model)
        self.doors = doors

    def description(self):
        return f"Car: {self.make} {self.model} with {self.doors} doors."

class Truck(Vehicle):
    def __init__(self, make, model, horsepower):   # Truck is Child Class #
        super().__init__(make, model)
        self.horsepower = horsepower

    def description(self):
        return f"Truck: {self.make} {self.model} with {self.horsepower} horsepower."

# Creating instances
car = Car("Chevrolet", "Chevelle", 2)
truck = Truck("Ford-150", "Lightning", 435)

# Polymorphic behavior
vehicles = [car, truck]


for vehicle in vehicles:
    print(vehicle.description())
