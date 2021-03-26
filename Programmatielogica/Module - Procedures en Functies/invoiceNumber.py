from random import randint

def checkNumber(num):
    print(num)
    print(num[:10], num[-2:])
    if int(num[:10]) % 97 == 0:
        if int(num[-2:]) == 97:
            return True
    elif int(num[0:10]) % 97 == int(num[-2:]):
        return True
    return False


def createValid():
    start = randint(1000000000, 9999999999)
    end = start % 97
    return str(start) + str(end)


def createSometimesValid():
    start = randint(1000000000, 9999999999)
    start -= start % 97
    return str(start) + '97'


def createUnvalid():
    start = randint(1000000000, 9999999999)
    end = start % 98
    return str(start) + str(end)


if __name__ == '__main__':
    for _ in range(10):
        print(checkNumber(createValid()))
        print(checkNumber(createSometimesValid()))
        print(checkNumber(createUnvalid()))
