# Find the second largest number in the list.

numbers = [4, 7, 2, 9, 1, 5]

largest = numbers[0] # Assume the first number is the largest
second_largest = None # Initialize second largest as None

for num in numbers:
    if num > largest:
        second_largest = largest # Update second largest before updating largest
        largest = num
    elif num !=largest and (second_largest is None or num > second_largest):
        second_largest = num

print(f'The second largest number in the list is : {second_largest}')