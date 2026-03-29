# Find the most frequent number in the list.

numbers = [1, 2, 2, 3, 3, 3, 4, 4]

def most_freq(numbers):
    fre1 = {}
    max = 0

    for num in numbers:
        if num in fre1:
            fre1[num] +=1
        else:
            fre1[num] = 1

        if fre1[num] > max:
            max = fre1[num]

    return max


result = most_freq(numbers)
print(result)