
""" Calculate the sum of numbers which are divisible by either 3 or 5 """

n = 30
total_sum = 0

for num in range(1, n):
    if num % 3 ==0 or num % 5 ==0:
        total_sum += num
print(f"Sum of numbers from 1 to 30 which are divisible by 3 or 5:  {total_sum}")

total_sum_2 = 0
i = 0
while i < n:
    if i % 3 ==0 or i % 5 ==0:
        total_sum_2 += i
    i +=1


print(f"Sum of numbers from 1 to 30 which are divisible by 3 or 5:  {total_sum_2}")

