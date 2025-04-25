class Vehicle:
    def move(self):
        return f"The Vehicle is moving as expected."


class Car(Vehicle):
    def move(self):
        return f"The car moves on the road."

class Boat(Vehicle):
    def move(self):
        return f"The boat sails on the water."


my_vehicle = Vehicle()
print(my_vehicle.move())

my_car = Car()
print(my_car.move())

my_boat = Boat()
print(my_boat.move())

