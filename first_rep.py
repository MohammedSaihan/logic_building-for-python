# Find the first repeating number in the list.

numbers = [2, 3, 4, 2, 3, 5, 6]

def first_rep(numbers):

    seen = set()

    for num in numbers:
        if num in seen:
            print(num)
            break
        else:
            seen.add(num)

result = first_rep(numbers)

print(result)