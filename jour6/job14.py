def longueur(texte):
    compteur = 0
    for _ in texte:
        compteur += 1
    return compteur


def my_long_word(n, phrase):
    # Découpe la phrase en mots (séparés par espace ou virgule)
    mots = []
    mot = ""
    for caractere in phrase + " ":
        if caractere == " " or caractere == ",":
            if mot != "":
                mots.append(mot)
                mot = ""
        else:
            mot += caractere

    # Garde les mots strictement plus longs que n
    resultat = ""
    for mot in mots:
        if longueur(mot) > n:
            if resultat == "":
                resultat = mot
            else:
                resultat = resultat + " " + mot
    return resultat


print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))
