mathResult = int(input("Enter the result of the math exam: "))
accountancyResult = int(input("Enter the result of the accountancy exam: "))
ictResult = int(input("Enter the result of the ICT exam: "))

if mathResult < 6:
    print("Student failed due to math.")
    if accountancyResult + ictResult < 12:
        print("And also due to accountancy and ICT.")
elif accountancyResult + ictResult < 12:
    print("Student failed due to accountancy and ICT.")
else:
    print("Student passed.")
