#6) Write a program to illustrate the use of tuples and sets with basic operations.

values = tuple(input("Enter tuple values: ").split())

print("\nTuple:", values)
print("First element:", values[0])
print("Length of tuple:", len(values))

numbers = set(map(int, input("\nEnter set numbers: ").split()))

print("Set:", numbers)

numbers.add(10)
print("After adding 10:", numbers)

numbers.remove(10)
print("After removing 10:", numbers)
