def calculateKm(dieselCarPrice, benzineCarPrice, dieselPrice, benzinePrice, yearsUsed, taxDiesel, taxBenzine, usageDiesel, usageBenzine):
    km = dieselCarPrice - benzineCarPrice
    km /= yearsUsed
    km += (taxDiesel - taxBenzine)
    km *= 100
    km /= ((benzinePrice * usageBenzine) - (dieselPrice * usageDiesel))
    return km


if __name__ == '__main__':
    print(calculateKm(16000, 15000, 1.401, 1.458, 4, 240, 220, 4.5, 5.5))
