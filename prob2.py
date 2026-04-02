# Find the second largest UNIQUE valid number

numbers = [10, None, 25, "40", -5, 30, 25, 30, None]

def second_largest(numbers):
    unique_num =set()

    for num in numbers:
        if isinstance(num,(float,int)) and num > 0:
            unique_num.add(num)
        if None == num:
            continue
        

    if len(unique_num) < 2:
        return None
    
    largest = None
    second_largest = None

    for num in unique_num:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest

result = second_largest(numbers)
print(result)
            

    
                        

