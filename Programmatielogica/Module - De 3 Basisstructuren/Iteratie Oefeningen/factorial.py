num = -1
while num < 0:
    num = int(input("Enter a positive number: "))

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(num))
