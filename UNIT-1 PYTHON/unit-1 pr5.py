#5) Write a program to create and manipulate lists using indexing slicing and list comprehensions.

numbers = list(map(int, input("Enter numbers: ").split()))

print("Original list:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])

squares = [x * x for x in numbers]

print("Squares:", squares)
