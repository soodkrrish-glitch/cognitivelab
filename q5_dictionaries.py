my_dict = {
    "name": "Varun",
    "roll_no": "1024170285",
    "branch": "copc",
    "age": 20,
    "city": "kota"
}

my_dict["location"] = my_dict.pop("city")
print("i. After renaming city to location:", my_dict)

my_dict["cgpa"] = 8.5
print("ii. After adding cgpa:", my_dict)

my_dict["age"] += 1
print("iii. After increasing age by 1:", my_dict)

dict_pop_copy = dict(my_dict)
popped_value = dict_pop_copy.pop("branch")
print("iv. After pop('branch'):", dict_pop_copy, "| Returned value:", popped_value)

dict_del_copy = dict(my_dict)
del dict_del_copy["branch"]
print("iv. After del branch:", dict_del_copy)
print("iv. pop() removes the key and returns its value, while del removes the key but returns nothing, so pop() is useful when you need the removed value.")

print("v. Key-value pairs:")
for key, value in my_dict.items():
    print(f"{key} → {value}")

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("vi. Key 'email' does not exist, using fallback message: Email not available.")

friend_dict = {
    "name": "Arjun",
    "roll_no": "1024170499",
    "branch": "mechanical",
    "age": 20,
    "location": "delhi"
}
merged_dict = {**my_dict, **friend_dict}
print("vii. Merged dictionary:", merged_dict)
print("vii. When both dictionaries share a key, the values from the second dictionary (friend_dict) win because later keys overwrite earlier ones in the merge.")

string_value_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("viii. Dictionary with only string values:", string_value_dict)
