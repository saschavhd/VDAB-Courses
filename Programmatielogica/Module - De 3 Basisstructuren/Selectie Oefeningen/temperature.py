degreesKelvin = float(input("Enter degrees in Kelvin: "))
if degreesKelvin < 0:
    print("Kelvin cannot fall below 0.")
else:
    print("{}°K = {}°C".format(degreesKelvin, degreesKelvin + 273.15))
