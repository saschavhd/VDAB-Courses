from random import randint

arr1 = []
arr2 = []
productArr = []

for i in range(5):
    arr1.append(randint(0, 9))
    arr2.append(randint(0, 9))
    productArr.append(arr1[i] * arr2[i])

print(arr1)
print(arr2)
print(productArr)
