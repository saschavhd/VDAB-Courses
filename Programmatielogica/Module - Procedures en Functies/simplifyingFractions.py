from math import gcd

numerator = int(input("Enter numerator: "))
denomenator = int(input("Enter denomenator: "))

print("{}/{}".format(int(numerator/gcd(numerator, denomenator)), int(denomenator/gcd(numerator, denomenator))))
