scores = ["85", 90, None, "100", "NaN", 75, -10, "60.5", "absent"] 

import math

def process_scores(scores):
    total = 0
    count = 0
    total_score = None

    for score in scores:
        try:
            num = float(score)
        except (ValueError, TypeError):
            continue

        if math.isnan(num):
            continue

        if num < 0:
            continue

        total += num
        count += 1

        if total_score is None or num > total_score:
            total_score = num

    average_score = total / count if count > 0 else None
    return average_score, total_score

average_score, total_score = process_scores(scores)
print(f"Average Score: {average_score}")
print(f"Total Score: {total_score}")


