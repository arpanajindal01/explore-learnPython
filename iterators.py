


fruits = ['apple', 'banana', 'cherry']

fruits_iter = iter(fruits)

print(next(fruits_iter))
print(next(fruits_iter))
print(next(fruits_iter))
print()


# Using generator to implement iterator

def square_func(n):
    for i in range(1, n + 1):
        yield i * i


square_gen = square_func(10)            # Here we are using a variable called square_gen, which is of type generator, which will store all the values of square_func
print(type(square_gen))

for num in square_gen:
    print(num)


# Infinite Iterators


""" Defining a infinite iterator"""
def count(start=0):
    while True:
        yield start
        start += 1

""" Using the loop to access the iterator and print it"""
count_gen = count()
for num in count_gen:
    print(num)
