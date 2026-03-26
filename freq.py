# Find the most frequent number in the list.

numbers = [1, 2, 2, 3, 3, 3, 4, 4]

def frequency(numbers):
    freq = {}
    maxi = None

    for n in numbers:
        if n in freq:
            freq[n] +=1
        else:
            freq[n] = 1

        if maxi is None or freq[n] > freq[maxi]:
            maxi = n
    return maxi


result = frequency(numbers)

print(result)