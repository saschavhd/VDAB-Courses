from random import randint
import numpy

arr = []
while (len(arr) < 7):
    temp = []
    for i in range(3):
        if i % 2 == 0:
            temp.append(randint(11, 20))
        else:
            temp.append(randint(0, 10))
    arr.append(temp)

avg = 0
for el in arr:
    avg += (sum(el)/len(el))
print(arr)
print(avg/len(arr))
