"""
UCS420: Cognitive Computing - Assignment 2
Q5: Python Dictionaries

Name : Dev Ariwala
Roll : 1024170433
"""

my_dict = {
    "name": "Dev Ariwala",
    "roll_no": "1024170433",
    "branch": "CSE",
    "age": 19,
    "city": "Gujarat",
}
print("Original dictionary:", my_dict)

my_dict["location"] = my_dict.pop("city")
print("i. After renaming 'city' -> 'location':", my_dict)

my_dict["cgpa"] = 8.2
print("ii. After adding 'cgpa':", my_dict)

my_dict["age"] += 1
print("iii. After incrementing 'age':", my_dict)

dict_copy_pop = my_dict.copy()
removed_value = dict_copy_pop.pop("branch")
print(f"iv. pop() removed 'branch' and returned its value: {removed_value}")
print("iv. Dict after pop():", dict_copy_pop)

dict_copy_del = my_dict.copy()
del dict_copy_del["branch"]
print("iv. Dict after del:", dict_copy_del)

print("v. Iterating over dictionary:")
for key, value in my_dict.items():
    print(f"   {key} -> {value}")

if "email" in my_dict:
    print("vi. Email:", my_dict["email"])
else:
    print("vi. 'email' key not found - no email on record.")

friend_dict = {
    "name": "Rahul Sharma",
    "roll_no": "1024170499",
    "branch": "ECE",
    "age": 20,
    "city": "Delhi",
}
merged_dict = {**my_dict, **friend_dict}
print("vii. friend_dict:", friend_dict)
print("vii. Merged dictionary:", merged_dict)

string_only_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("viii. Only string-valued pairs:", string_only_dict)
