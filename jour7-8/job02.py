def draw_triangle(hauteur):
    for i in range(hauteur):
        espaces_gauche = " " * (hauteur - 1 - i)

        if i == hauteur - 1:
            interieur = "_" * (2 * i)
        else:
            interieur = " " * (2 * i)

        print(espaces_gauche + "/" + interieur + "\\")


hauteur = int(input("Hauteur du triangle : "))
draw_triangle(hauteur)
