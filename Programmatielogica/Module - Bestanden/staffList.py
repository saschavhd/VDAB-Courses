with open("staff.txt", 'r') as inFile:
    for line in inFile:
        print(line.split(';')[1], line.split(';')[4])
