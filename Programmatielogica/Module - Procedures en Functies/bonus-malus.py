def updateBonusMalus(old, accidents):
    if accidents == 0:
        old -= 1
    elif accidents == 1:
        old += 2
    elif accidents > 1:
        old += (2 + 3 * (accidents-1))

    if old < 1:
        old = 1
    elif old > 18:
        old = 18
    return old

if __name__ == '__main__':
    previousYear = int(input("Enter the ladder of the previous year: "))
    acds = int(input("Enter the number of accidents during the year: "))
    updated = updateBonusMalus(previousYear, acds)
    if updated == 18:
        print("Customer should switch insurance companies.")
    else:
        print("Current customer ladder is {}".format(updated))
