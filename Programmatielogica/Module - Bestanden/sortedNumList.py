from random import randint

arr = []
for _ in range(10):
    arr.append(randint(1, 1000))

arr.sort()

with open('numList.txt', 'w') as outFile:
    print(arr, file=outFile)
