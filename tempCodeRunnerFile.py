# Find the smallest number in the list

numbers = [4, 7, 2, 9, 1, 5]

def find_smallest(numbers):
    smallest_num = numbers[0] # Assume the first number is the smallest
    for num in numbers:
        if num < smallest_num:
            smallest_num = num


    return smallest_num


smallest = find_smallest(numbers)
print(f'The smallest number in the list is: {smallest}')