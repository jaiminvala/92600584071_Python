# Iterate over a list
print("List:")
numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)

# Iterate over a string
print("\nString:")
name = "Python"

for i in name:
    print(i)

# Iterate over a dictionary
print("\nDictionary:")
student = {
    "name": "HARESH",
    "age": 21,
    "course": "MCA"
}

for key, value in student.items():
    print(key, ":", value)
