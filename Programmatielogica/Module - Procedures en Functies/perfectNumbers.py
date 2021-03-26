def divisorSum(n):
    dvs = 0
    for i in range(1, n):
        if n % i == 0:
            dvs += i
    return dvs


def isPerfect(n):
    if not n.isdigit():
        return False

    if divisorSum(int(n)) != int(n):
        return False

    return True


if __name__ == '__main__':
    inp = input("Enter a number: ")

    print(isPerfect(inp))
