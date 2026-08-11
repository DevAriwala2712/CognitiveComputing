"""
UCS420: Cognitive Computing - Assignment 2
Q3: Random numbers with Lists

Name : Dev Ariwala
Roll : 1024170433
"""

import random
from collections import Counter

roll_number = 1024170433

random.seed(roll_number)

numbers = [random.randint(100, 900) for _ in range(100)]
print("i. Generated numbers:", numbers)

odd_numbers = [n for n in numbers if n % 2 != 0]
print(f"ii. Odd numbers count = {len(odd_numbers)}")
print("ii. Odd numbers:", odd_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print(f"iii. Even numbers count = {len(even_numbers)}")
print("iii. Even numbers:", even_numbers)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = [n for n in numbers if is_prime(n)]
print(f"iv. Prime numbers count = {len(prime_numbers)}")
print("iv. Prime numbers:", prime_numbers)

counts = Counter(numbers)
most_common_number, frequency = counts.most_common(1)[0]
print(f"v. Most frequent number = {most_common_number}, occurs {frequency} time(s)")
