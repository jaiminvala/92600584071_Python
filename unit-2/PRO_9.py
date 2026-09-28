# Iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:")
for num in numbers:
    print(num)

# Iterator
print("\nIterator:")

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
