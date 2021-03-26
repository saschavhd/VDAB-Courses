ARRLENGTH = 3
arr = []
while (len(arr) < ARRLENGTH):
    arr.append(int(input("Enter a number: ")))

def bubbleSort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(ARRLENGTH-1):
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
    return nums

print(bubbleSort(arr))
