# Count how many numbers in the list are greater than 5.
numbers = [3, 8, 2, 7, 10, 11, 6]
count = 0
for num in numbers:
    if num > 5:
        count += 1

print(f'number of numbers greater than 5 in the list is : {count}')