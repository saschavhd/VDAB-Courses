def getValidInput():
    inp = input("Enter a positive integer: ")
    if inp.isdigit():
        return int(inp)
    else:
        print("Input not valid! Try again.")
        return getValidInput()


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':

    print(factorial(getValidInput()))
