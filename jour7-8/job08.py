def my_sort(liste):
    coups = 0
    n = 0
    for _ in liste:
        n += 1
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                coups += 1

    print("Nombre total de coups nécessaires pour trier la liste :", coups)
    return liste


resultat = my_sort([64, 34, 25, 12, 22, 11, 90])
print("Liste triée :", resultat)
