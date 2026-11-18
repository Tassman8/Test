def longueur(liste):
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur


def arrondir(x):
    return int(x + 0.5)


def trier(liste):
    n = longueur(liste)
    for i in range(n):
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


def arrondir_et_trier(liste):
    arrondis = []
    for x in liste:
        arrondis.append(arrondir(x))
    return trier(arrondis)


L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(arrondir_et_trier(L))
