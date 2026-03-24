# Count how many vowels exist in the sentence.
text = "data analyst"
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count+=1

print(f'number of vowels in "{text}" is : {count}')