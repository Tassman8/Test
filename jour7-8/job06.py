def arrondir_notes(notes):
    resultat = []
    for note in notes:
        ecart = (5 - note % 5) % 5
        if note >= 40 and ecart < 3:
            resultat.append(note + ecart)
        else:
            resultat.append(note)
    return resultat


print(arrondir_notes([73, 67, 38, 33, 83, 82, 40, 99, 100]))
