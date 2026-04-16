data = [100, "200", "abc", None, 300, "400.5", -50, 0, "0"]

def process_data(data):
    total = 0
    count = 0

    for item in data:
        try:
            num = float(item)
        except (ValueError, TypeError):
            continue

        # Reject booleans explicitly (True → 1.0 problem)
        if isinstance(item, bool):
            continue

        if num > 0:
            total += num
            count += 1

    return total, count

total, count = process_data(data)
print(f"Total of valid numbers: {total}")
print(f"Count of valid numbers: {count}")