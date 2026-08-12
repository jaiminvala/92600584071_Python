#4) Write a program to demonstrate string operations including slicing formatting and built-in string functions.

text = input("Enter a string: ")

print("\nString Slicing")
print("First character:", text[0])
print("Last character:", text[-1])
print("First 3 characters:", text[:3])
print("Reverse string:", text[::-1])

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

print("\nString Formatting")
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

print("\nBuilt-in String Functions")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalized:", text.capitalize())
print("Title:", text.title())
print("Count of 'a':", text.count("a"))
print("Replace spaces with '-':", text.replace(" ", "-"))

