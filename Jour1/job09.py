nom = "Pokemon X et Y"
prix = 30.00
stock = 20

print(nom, prix, stock)

stock += 10

achat = int(input("Quantité à acheter : "))
stock -= achat

prix *= 1.10
print(nom, prix, stock)