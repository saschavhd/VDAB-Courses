from random import randint

arr1 = []
arr2 = []
sumArr = []
for i in range(randint(5, 10)):
    arr1.append(randint(0, 9))
    arr2.append(randint(0, 9))
    sumArr.append(arr1[i]+arr2[i])

print(arr1)
print(arr2)
print(sumArr)
