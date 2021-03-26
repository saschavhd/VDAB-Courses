startCapital = float(input("Enter start capital: "))
interest = float(input("Enter interest percentage: "))
time = int(input("Enter time in years: "))

for i in range(time):
    startCapital += startCapital * (interest/100)

print(round(startCapital, 2))
