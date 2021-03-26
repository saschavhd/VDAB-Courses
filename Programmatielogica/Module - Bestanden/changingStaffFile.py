YEARLYRAISE = 25

with open('staff.txt', 'r') as inFile:
    arr = []
    for line in inFile:
        print(line)
        temp = line.split(';')
        temp[-1] = str(int(temp[-1]) + YEARLYRAISE)
        arr.append(";".join(temp))


with open('staff.txt', 'w') as outFile:
    for el in arr:
        print(el, file=outFile)
