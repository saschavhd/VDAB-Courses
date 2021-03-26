num1 = 0
num2 = 1

print(num1)
print(num2)

while num1 + num2 < 1000:
    x = num1 + num2
    print(x)
    num1, num2 = num2, x
