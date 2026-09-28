# List Comprehension
numbers = [1, 2, 3, 4, 5]
square = [x * x for x in numbers]

print("List Comprehension:")
print(square)


# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x * x for x in numbers}

print("\nDictionary Comprehension:")
print(square_dict)


# Set Comprehension
numbers = [1, 2, 2, 3, 3, 4, 5]
square_set = {x * x for x in numbers}

print("\nSet Comprehension:")
print(square_set)
