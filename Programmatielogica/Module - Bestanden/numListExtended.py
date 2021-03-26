from random import randint

with open('numList.txt', 'r') as inFile:
    x = inFile.readline()
    y = []
    for el in x:
        if el != '[' and el != ']' and el != ',' and el != '\n':
            y.append(el)

    res = []
    lastInd = 0
    for i in range(len(y)):
        if y[i] == ' ' or i == len(y) - 1:
            res.append(int(''.join(y[lastInd:i])))
            lastInd = i

    for _ in range(10):
        res.append(randint(1, 1000))
    res.sort()

with open('numListExtended.txt', 'w') as outFile:
    print(res, file=outFile)
