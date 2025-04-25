def sum_of_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Here is the sum of all the numbers you have entered: {total}")


sum_of_numbers(10,10,10)
sum_of_numbers(2,2,2,2,2,2,2,2,2,2,2,2,2,22,2, -2,-1)

print()
def display_info(name, age, city = "Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")


display_info("Alice", 30)
display_info("Alice", 30, "New York")
display_info(name= "Alice", age=30, city="New York")   #keyword arguments are passed here

print()
print()

def display_fruits(*fruits):
    for fruit in fruits:
        print(f"Here is the list of fruits you have added: {fruit}")


display_fruits("apple", "banana", "cherry", "kiwi", "orange")
print()
print()

# Passing the argument as a list[] of fruits

def display_fruits_list(fruits):
    for fruit in fruits:
        print(f"Here is the list of fruits you have added[]: {fruit}")

my_fruits_list = ["Apple", "Banana", "Cherry", "Guava", "Orange", "Kiwi"]

display_fruits_list(my_fruits_list)
