"""
UCS420: Cognitive Computing - Assignment 2
Q2: Python Tuples

Name : Dev Ariwala
Roll : 1024170433
"""

roll_number = "1024170433"
digits = [int(d) for d in roll_number]

L = [d * 10 for d in digits]
scores = tuple(L[:8])
print("scores =", scores)

highest = max(scores)
highest_index = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)
print(f"i. Highest score = {highest} at index {highest_index}")
print(f"i. Lowest score = {lowest}, appears {lowest_count} time(s)")

reversed_list = list(reversed(scores))
print("ii. Reversed (as list):", reversed_list)

user_score = int(input("iii. Enter a score to search for: "))
if user_score in scores:
    print(f"iii. {user_score} found at index {scores.index(user_score)}")
else:
    print(f"iii. {user_score} is not present in scores")

try:
    scores[0] = 100
except TypeError as e:
    print("iv. Error caught:", e)

first_score, second_score, *remaining_scores = scores
print(f"v. first_score={first_score}, second_score={second_score}, remaining_scores={remaining_scores}")
