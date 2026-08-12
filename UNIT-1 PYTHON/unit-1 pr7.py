#7) Program to demonstrate dictionary methods and iteration

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

student = {
    "name": name,
    "age": age,
    "city": city
}

print("\nDictionary:", student)

print("Name:", student.get("name"))

student["course"] = "Python"
print("After adding course:", student)

student.pop("city")
print("After removing city:", student)


print("\nDictionary elements:")
for key, value in student.items():
    print(key, ":", value)
