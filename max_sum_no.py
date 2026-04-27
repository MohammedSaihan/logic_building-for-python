data = ["10", "20", None, "30", "invalid", 40, "50.5", -5]

def max_sum_no(data):
    max_even = None
    sum_odd = 0

    for item in data:

        try:
            num = float(item)
        except (ValueError,TypeError):
            continue


        if num < 0 :
            continue


        if not num.is_integer():
            continue


        num = int(num)


        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num

            else:
                sum_odd += num

    return max_even,sum_odd


result = max_sum_no(data)

print(result)




