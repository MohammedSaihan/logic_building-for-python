# From the list, find the largest ODD number
numbers = [4, 7, 2, 9, 1, 5, 6]

def largest_odd(numbers):
    odd = None

    for num in numbers:
        if num % 2 == 1:
            if odd is None:
                odd = num
            elif num > odd:
                odd = num

    return odd


lo = largest_odd(numbers)

print(lo)