# Create a new list that contains only even numbers.
numbers = [3, 8, 2, 7, 10, 11, 6]

even_number = []
for num in numbers:
    if num % 2 ==0:
        even_number.append(num)

print(f'Even numbers in the list are : {even_number}')