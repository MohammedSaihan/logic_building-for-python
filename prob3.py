data = ["100", 200, None, "300", 400, "invalid", 500, -100]

def sum_valid(data):
    total = 0

    for item in data:
        num = None

        if isinstance(item, str):
            try:
                num = float(item)
            except ValueError:
                continue

        elif isinstance(item, (int, float)):
            num = item

        else:
            continue

        if num > 0:
            total +=num

    return total

result = sum_valid(data)
print(result)