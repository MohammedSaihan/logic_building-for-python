# Find the difference between the largest and smallest number in the list.

numbers = [4, 7, 2, 9, 1, 5]

largest_num = numbers[0]
smallest_num = numbers[0]

for n in numbers:
    if n > largest_num:
        largest_num =smallest_num
        largest_num = n

    if  n < smallest_num:
        smallest_num = n 


diff = largest_num - smallest_num

print(diff)