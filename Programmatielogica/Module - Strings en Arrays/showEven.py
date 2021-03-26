arr = []
for i in range(10):
    inp = int(input("Enter a number: "))
    if inp % 2 == 0:
        arr.append(inp)

print(sorted(arr))
