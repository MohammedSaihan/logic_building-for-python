transactions = [
    {"user": "A", "amount": "100"},
    {"user": "B", "amount": 200},
    {"user": "A", "amount": None},
    {"user": "C", "amount": "invalid"},
    {"user": "B", "amount": 300},
    {"user": "A", "amount": "50.5"},
    {"user": "C", "amount": 400},
]


# Task

# Return:

# (user_with_highest_average_transaction)

# Rules

# Valid amount:

# numeric OR string convertible to float
# ignore None
# ignore invalid strings
# Expected reasoning

# You must:

# compute average per user
# not sum
# not max transaction

def get_user_with_highest_average_transaction(transactions):
    user_totals = {}
    user_counts = {}

    for transaction in transactions:
        user = transaction.get("user")
        amount = transaction.get("amount")

        if user is None:
            continue

        if isinstance(amount,(int,float)):
            valid_amount = float(amount)
        elif isinstance(amount,str):
            try:
                valid_amount = float(amount)
            except ValueError:
                continue

        else:
            continue

        user_totals[user] = user_totals.get(user,0) + valid_amount
        user_counts[user] = user_counts.get(user,0) + 1

    if not user_totals:
        return None
    max_user = None
    max_average = float('-inf')
    for user in user_totals:
        average = user_totals[user] / user_counts[user]
        if average > max_average:
            max_average = average
            max_user = user

    return max_user 

result = get_user_with_highest_average_transaction(transactions)
print(result)