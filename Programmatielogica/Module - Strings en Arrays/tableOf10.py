from random import randint

arr = []
for i in range(10):
    arr.append(randint(1, 1000))

print(arr)
print(sum(arr))
