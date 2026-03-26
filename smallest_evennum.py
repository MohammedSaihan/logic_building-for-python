# From the list, find the smallest EVEN number
numbers = [4, 7, 2, 9, 1, 5, 6]
smallest_even = None

for num in numbers:
    if num % 2 == 0: # Check if the number is even
        if smallest_even is None or num < smallest_even:
            smallest_even = num

print(f'The smallest even number in the list is: {smallest_even}')