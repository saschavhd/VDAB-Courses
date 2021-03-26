from numpy import average

positives = []
negatives = []
zeros = 0

cond = True
while cond:
    temp = int(input("Enter temperature: "))
    if temp == 99:
        break
    if temp > 0:
        positives.append(temp)
    elif temp < 0:
        negatives.append(temp)
    else:
        zeros += 1

print(len(positives))
print(len(negatives))
print(average(positives))
print(average(negatives))
print(zeros)
