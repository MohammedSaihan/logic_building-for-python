# Count how many times the letter "a" appears in this string:

text = "banana"

count = 0

for char in text:
    if char == 'a':
        count+=1

print(f'number of times "a" appears in "{text}" is : {count}')