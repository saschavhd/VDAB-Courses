amountOfKids = int(input("Enter the amount of kids the parent has: "))
monthlyWage = float(input("Enter the monthly wage of the parent: "))

if amountOfKids >= 5:
    result = 2*25 + 2*37.5 + (amountOfKids-4)*45
elif amountOfKids >= 3:
    result = 2*25 + (amountOfKids-2)*37.5
else:
    result = amountOfKids*25

if monthlyWage <= 500:
    result += result/4
elif monthlyWage > 2000:
    result -= result/4

if result < amountOfKids * 25:
    print(amountOfKids * 25)
else:
    print(result)
