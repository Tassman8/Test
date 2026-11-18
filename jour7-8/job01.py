def draw_rectangle(width, height):
    ligne_horizontale = "|" + "-" * (width - 2) + "|"
    ligne_vide = "|" + " " * (width - 2) + "|"

    if height == 1:
        print(ligne_horizontale)
        return

    print(ligne_horizontale)
    for _ in range(height - 2):
        print(ligne_vide)
    print(ligne_horizontale)


draw_rectangle(10, 3)
