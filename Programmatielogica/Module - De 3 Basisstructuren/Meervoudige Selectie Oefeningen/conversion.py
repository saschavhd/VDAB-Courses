from os import system, name
from time import sleep


def menu():
    print(
    '''
    1. Kilogram to pound
    2. Pound to kilogram
    3. Centimeter to inch
    4. Inch to centimeter
    5. Stop
    '''
    )

    cs = int(input("Select operation: "))
    if cs not in range(1, 6):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return menu()

    if cs == 1:
        print("{} lbs".format(round(float(input("Enter value in kilogram: "))*2.205, 2)))
    elif cs == 2:
        print("{} kg".format(round(float(input("Enter value in pounds: "))/2.205, 2)))
    elif cs == 3:
        print("{} inches".format(round(float(input("Enter value in centimeters: "))*0.394, 2)))
    elif cs == 4:
        print("{} cm".format(round(float(input("Enter value in inches: "))/0.394, 2)))
    elif cs == 5:
        print("Exiting in 3 seconds...")
        sleep(3)
        return None

    return menu()


if __name__ == '__main__':
    menu()
