# From the list, find the average of even numbers

numbers = [3, 8, 2, 7, 10, 11, 6]
total = 0
count = 0

for num in numbers:
    if num % 2 == 0: # Check if the number is even
        total += num  # Add the even number to the total
        count +=1

avg = total / count

print(avg)