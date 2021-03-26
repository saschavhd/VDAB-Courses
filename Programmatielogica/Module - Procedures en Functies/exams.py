def enterScore():
    inp = input("Enter a valid grade: ")
    if inp in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return int(inp)
    else:
        print("Unvalid grade, try again!")
        return enterScore()


def checkGrades(grades):
    if grades[0] < 6:
        if grades[1] + grades[2] < 12:
            return "Student failed due to math, accountancy and ICT."
        else:
            return "Student failed due to math."
    elif grades[1] + grades[2] < 12:
        return "Student failed due to accountancy and ICT."
    else:
        return "Student passed"


if __name__ == '__main__':
    gds = []
    for _ in range(3):
        gds.append(enterScore())

    print(checkGrades(gds))
