numbers = [2, 3, 4, 2, 3, 5, 6]

def non_rep(numbers):
    freq = {}
    non = None

    for num in numbers:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1

    for num in numbers:
        if freq[num] == 1:
            print(num)
            break

    

print(non_rep(numbers))

