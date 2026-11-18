def cesar(message, decalage):
    resultat = ""
    for caractere in message:
        if "a" <= caractere <= "z":
            position = ord(caractere) - ord("a")
            nouvelle_position = (position + decalage) % 26
            resultat += chr(nouvelle_position + ord("a"))
        elif "A" <= caractere <= "Z":
            position = ord(caractere) - ord("A")
            nouvelle_position = (position + decalage) % 26
            resultat += chr(nouvelle_position + ord("A"))
        else:
            resultat += caractere
    return resultat


print(cesar("Bonjour Zorro", 3))
print(cesar("Erqmrxu Cruur", -3))
print(cesar("xyz", 3))
print(cesar("abc", -3))
