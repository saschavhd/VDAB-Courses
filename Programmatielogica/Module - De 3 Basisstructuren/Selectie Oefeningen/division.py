num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(round(num1/num2, 2))
else:
    print(round(num2/num1, 2))
