from car import Car
from driver import Driver

my_car = Car("Toyota", "Camry", 2020)
my_driver_detail = Driver("Dmitry", 30)
print(f"The {my_driver_detail.age} years old {my_driver_detail.name} drives "
      f"{my_car.maker}, {my_car.model},  {my_car.year} having {my_car.wheels} wheels in it.")


my_friends_car = Car("Toyota", "Rav4", 2020)
my_friend = Driver("Bob", 35)
print(f"My friend, {my_friend.name} is of age {my_friend.age} "
      f"years and drives {my_friends_car.maker}, {my_friends_car.model}, "
      f"{my_friends_car.year} having {my_friends_car.wheels} wheels in it.")

print("--------------------------------------------------------------------------------------------------")

my_car.year = 2010
Car.wheels = 6

print(f"Printing the updated year of the car:  {my_car.year}")
print(f"Printing the updated year of the car:  {my_friends_car.year}")

print(f"Printing the updated wheels of the car:  {my_car.wheels}")
print(f"Printing the updated wheels of the car:  {my_friends_car.wheels}")

