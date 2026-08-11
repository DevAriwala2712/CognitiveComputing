"""
UCS420: Cognitive Computing - Assignment 2
Q4: Python Sets

Name : Dev Ariwala
Roll : 1024170433
"""

roll_number = "1024170433"
digits = [int(d) for d in roll_number]

first_eight_digits = digits[:8]

A = {d * 7 for d in first_eight_digits}
B = {d * 9 for d in first_eight_digits}
print("A =", A)
print("B =", B)

print("vi. Union (A | B):", A | B)

print("vii. Intersection (A & B):", A & B)

a_minus_b = A.difference(B)
b_minus_a = B.difference(A)
print("viii. A - B:", a_minus_b)
print("viii. B - A:", b_minus_a)

print("ix. Symmetric difference (A ^ B):", A.symmetric_difference(B))

print("x. Is A a subset of B?", A.issubset(B))
print("x. Is B a superset of A?", B.issuperset(A))

X = int(input("xi. Enter a value X to remove from set A: "))
A.discard(X)
print("xi. A after discard():", A)
