L = [7, 11, 42, 39, 2]


def augmenter(liste):
    for i in range(len(liste)):
        liste[i] += 1


print(L)
augmenter(L)
print(L)
