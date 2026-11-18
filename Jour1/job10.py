montant = 10000
taux = 5

print("Gain :", montant * taux / 100)

montant += 5000
taux += 2
print("Gain :", montant * taux / 100)

montant *= 0.9
taux -= 1
print("Gain :", montant * taux / 100)
print("Montant final :", montant)