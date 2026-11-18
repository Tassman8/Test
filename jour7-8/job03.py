def tapis(n):
    bordure = "+" + "-" * (n + 1) + "+"

    print(bordure)
    for ligne in range(n + 1):
        contenu = ""
        for colonne in range(n + 1):
            if colonne == n - ligne:
                contenu += " "
            else:
                contenu += "#"
        print("|" + contenu + "|")
    print(bordure)


tapis(10)
