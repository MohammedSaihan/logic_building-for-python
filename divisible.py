# From the list, find the sum of numbers that are divisible by 3 but NOT divisible by 2

numbers = [3, 6, 9, 12, 15, 8, 10]

total = 0 
for n in numbers:
    if n % 3 == 0 and n % 2 != 0:
        total +=n

print(total)
