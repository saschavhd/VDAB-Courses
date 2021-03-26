arr = []
while True:
    inp = int(input("Enter height of student: "))
    if inp == 0:
        break
    arr.append(inp)

print("Largest: {} - Position: {}".format(max(arr), arr.index(max(arr))))
print("Smallest: {} - Position: {}".format(min(arr), arr.index(min(arr))))
