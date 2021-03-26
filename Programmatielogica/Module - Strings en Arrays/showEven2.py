arr = []
while True:
    inp = int(input("Enter a number: "))
    if inp == 0:
        break
    elif inp % 2 == 0:
        arr.append(inp)

print(sorted(arr))
