"""
UCS420: Cognitive Computing - Assignment 2
Q1: Python Lists

Name : Dev Ariwala
Roll : 1024170433
"""

roll_number = "1024170433"

digits = [int(d) for d in roll_number]

L = [d * 10 for d in digits]

print("i. L =", L)

L.append(99)
print("ii. After append(99):", L)

L.insert(2, 55)
print("ii. After insert(2, 55):", L)

L.remove(55)
print("iii. After remove(55):", L)

popped = L.pop()
print(f"iii. After pop() (removed {popped}):", L)

L.sort()
print("iv. Ascending sort:", L)

L.sort(reverse=True)
print("iv. Descending sort:", L)

print("v. First three elements:", L[:3])
print("v. Last three elements:", L[-3:])

average = sum(L) / len(L)
above_average = [x for x in L if x > average]
print(f"vi. Average of L = {average}")
print("vi. Elements greater than average:", above_average)
