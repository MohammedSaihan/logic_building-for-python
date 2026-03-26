# From the list, find the sum of all ODD numbers greater than 5

numbers = [4, 7, 2, 9, 1, 5, 6]

def sum_of_odd_numbers(numbers):
    total = 0

    for n in numbers:
        if n % 2 != 0 and n > 5:
            total+=n

    return total



result = sum_of_odd_numbers(numbers)

print(result)