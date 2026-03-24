# Write a program to count how many vowels are in a string.
text = "programming"
vowels = "aeiou"
count = 0  

for char in text:
    if char in vowels:
        count +=1


print(f'number of vowels in "{text}" is : {count}')