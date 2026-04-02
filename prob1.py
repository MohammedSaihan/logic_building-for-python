# Write logic to find the largest valid transaction amount.

transactions = [100, 250, None, -50, 400, "300", 0, 150, None, 500]

def largest_transaction(transactions):
    longest = None

    for t in transactions:
        if not isinstance(t,(int,float)):
            continue
        if t <= 0:
            continue

        if longest is None or t > longest:
            longest = t

    return longest

result = largest_transaction(transactions)
print(result)