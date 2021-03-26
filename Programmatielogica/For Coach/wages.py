monthDayFactor = 25
monthlyWage = int(input("Enter monthly wage: "))
daysWorked = int(input("Enter the amount of days for which you want to calculate the wage: "))

print(round((monthlyWage/monthDayFactor)*daysWorked, 2))
