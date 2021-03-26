ARRLENGTH = 10
arr = []
while (len(arr) < ARRLENGTH):
    arr.append(int(input("Enter a whole number (positive or negative): ")))

print("Max: {}".format(max(arr)))
print("Min: {}".format(min(arr)))
