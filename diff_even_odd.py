# From the list, find the difference between the largest EVEN number and smallest ODD number
numbers = [4, 7, 2, 9, 1, 5, 6]

largest_EVEN_number = numbers [0]

smallestODDnumber = numbers[0]

for n in numbers:
    # largest even filtering
    if n % 2 == 0:
        if n > largest_EVEN_number:
            largest_EVEN_number = n

    if n % 2 != 2:
        if n < smallestODDnumber:
            smallestODDnumber=n

diff = largest_EVEN_number - smallestODDnumber
print(largest_EVEN_number)
print(smallestODDnumber)
print(diff)