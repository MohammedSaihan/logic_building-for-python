# Find the sum of all even numbers in the list.
numbers = [3, 8, 2, 7, 10, 11, 6]
total = 0
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        total += num

print(f'Sum of even numbers {even_numbers} in the list is : {total}')