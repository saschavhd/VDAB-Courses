ARRLENGTH = 3
arr = []
while (len(arr) < ARRLENGTH):
    score = int(input("Enter exam score: "))
    if score < 0 or score > 10:
        print("Enter a valid score out of 10!")
    else:
        arr.append(score)

if arr[0] < 6 and arr[1]+arr[2] < 12:
    print("Student failed due to math and the combination of accountancy and ICT.")
elif arr[0] < 6:
    print("Student failed due to math.")
elif arr[1]+arr[2] < 12:
    print("Student failed due to the combination of accountancy and ICT.")
else:
    print("Student passed.")
