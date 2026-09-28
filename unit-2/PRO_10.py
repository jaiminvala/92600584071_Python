def numbers(n):
    for i in range(1, n + 1):
        yield i
n = int(input("Enter a number: "))
print("Sequence of numbers:")
for num in numbers(n):
    print(num)
