amount = float(input("Enter the end amount: "))
if amount > 5000:
    print("Price reduced to: €{:.2f}".format(amount-(amount*0.03)))
else:
    print("No price reduction: €{:.2f}".format(amount))
