# Find the largest number in this list without using max()
numbers = [4, 7, 2, 9, 1, 5]

largest = numbers[0] # Assume the first number is the largest

for num in numbers:
    if num > largest:
        largest = num

print(f'The largest number in the list is : {largest}')