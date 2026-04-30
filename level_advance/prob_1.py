logs = [
    {"user_id": 101, "duration": 35},
    {"user_id": 102, "duration": None},
    {"user_id": 101, "duration": 20},
    {"user_id": 103, "duration": "45"},
    {"user_id": 102, "duration": 15},
    {"user_id": 101, "duration": -5},
    {"user_id": 104, "duration": 50.5},
    {"user_id": 103, "duration": 10},
]

# Rules

# A valid duration:

# must be int or float
# not None
# not a string
# must be > 0

# So valid durations are:

# 101 → 35 + 20 = 55
# 102 → 15
# 103 → 10
# 104 → 50.5

# Expected answer:

# 101

def get_user_with_highest_total_duration(logs):

    user_total = {}

    for entry in logs:
        user_id = entry.get("user_id")
        duration = entry.get("duration")

        if user_id is None:
            continue
        
        if not isinstance(duration,(int,float)) or duration <= 0:
            continue

        user_total[user_id] = user_total.get(user_id,0) + duration

    if not user_id:
        return None
    
    max_user = None
    max_duration = float('-inf')

    for user_id,total in user_total.items():
        if total > max_duration:
            max_duration = total
            max_user = user_id

    
    return max_user

result = get_user_with_highest_total_duration(logs)
print(result)


