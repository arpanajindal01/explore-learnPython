def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num
    avg = total / len(numbers)

    return avg

my_list = [10,20,30,40,50,60,70,80,90,100]
result = calculate_average(my_list)
print(f"Here is the average of the list of numbers you have entered: {result}")

