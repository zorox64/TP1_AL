import random

nombre_inconnu = random.randint(0, 100)

compteur_essais = 0

while True:
    nombre = int(input("Entrez votre nombre : "))

    compteur_essais += 1

    if nombre < nombre_inconnu:
        print("Le nombre mystère est plus grand.")
    elif nombre > nombre_inconnu:
        print("Le nombre mystère est plus petit.")
    else:
        print(f" Vous avez trouvé le nombre {nombre_inconnu} en {compteur_essais} tours.")
        break
