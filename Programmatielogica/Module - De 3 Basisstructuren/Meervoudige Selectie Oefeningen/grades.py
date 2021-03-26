while True:
    numberOfCourses = int(input("Enter the number of courses for this student: "))
    grades = []
    for i in range(numberOfCourses):
        grades.append(int(input("Enter grade for the course: ")))
    name = input("Enter name of student: ")
    if name.lower() == 'stop':
        break
    percentage = round(((sum(grades)/numberOfCourses)/2)*10, 2)
    if any(grade < 10 for grade in grades) or percentage < 60:
        print("{} failed with a percentage of {}".format(name, percentage))
    elif percentage >= 90:
        print("{} passed for grootste onderscheiding with a percentage of {}".format(name, percentage))
    elif percentage >= 80:
        print("{} passed for grote onderscheiding with a percentage of {}".format(name, percentage))
    elif percentage >= 70:
        print("{} passed for onderscheiding with a percentage of {}".format(name, percentage))
    elif percentage >= 60:
        print("{} passed with a percentage of {}".format(name, percentage))
