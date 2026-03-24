# Count how many even numbers exist in this list

numbers = [3, 8, 2, 7, 10, 11, 6]
count = 0 
for num in numbers:
    if num % 2 ==0:
        count +=1

print(f'number of even numbers in the list is : {count}')