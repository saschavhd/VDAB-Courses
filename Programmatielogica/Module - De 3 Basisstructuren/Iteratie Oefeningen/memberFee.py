from numpy import average

baseFee = 10
maxReduction = 8.5
fees = []

def getReduction(age, kids, wage):
    reduction = 0
    if age > 50:
        reduction += 2.5

    if kids >= 5:
        reduction += 5
    else:
        reduction += kids * 1

    if wage < 12500:
        reduction += 2.5

    if reduction > maxReduction:
        return maxReduction
    else:
        return reduction


while True:
    name = input("Enter name: ")
    if name.lower() == "stop":
        break
    age = int(input("Enter age: "))
    amountOfKids = int(input("Enter amount of kids: "))
    yearlyWage = float(input("Enter yearly salary: "))
    fees.append(10-getReduction(age, amountOfKids, yearlyWage))

print("A total of {} membership(s) with an average price of {}!".format(len(fees), average(fees)))
