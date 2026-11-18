def longueur(liste):
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur


def trier(liste):
    n = longueur(liste)
    for i in range(n):
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


print(trier([5, 3, 8, 1, 9, 2]))
