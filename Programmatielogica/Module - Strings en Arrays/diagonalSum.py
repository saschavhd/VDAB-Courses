from random import randint
n = int(input("Enter dimension size: "))
arr = []

for _ in range(n):
    temp = []
    for _ in range(n):
        temp.append(randint(0, 9))
    arr.append(temp)

sum = 0
for i in range(n):
    sum += arr[i][i]
    sum += arr[i][(i+1)*-1]

print(arr)
print(sum)
