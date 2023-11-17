print("exercice 1 a")
N = int(input("Entrez la valeur de N : "))


somme = 0


for i in range(N + 1):
    somme += i


print(f"La somme des N premiers entiers naturels de 0 à {N} est : {somme}")


print("exercice 1 b")

valeur_utilisateur = int(input("Entrez une valeur (entre 0 et 100) : "))

while valeur_utilisateur != 100:
    valeur_utilisateur = int(input("mauvaise réponse. Entrez une nouvelle valeur (entre 0 et 100) : "))

print("bonne réponse qui est 100.")

print("exercice 1 c")


valeursInf10 = 0
valeursENTRE10ET15 = 0
valeursSUPERIEUR15 = 0

for i in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    while valeur < 0 or valeur > 20:
        print("La valeur doit être comprise entre 0 et 20.")
        valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    if valeur < 10:
        valeursInf10 += 1
    elif valeur < 15:
        valeursENTRE10ET15+= 1
    else:
        valeursSUPERIEUR15 += 1

print("Le nombre de valeurs inférieures à 10 est :", valeursInf10)
print("Le nombre de valeurs entre 10 et 15 est :", valeursENTRE10ET15)
print("Le nombre de valeurs supérieures à 15 est :", valeursSUPERIEUR15)





print("exercice 1 d")

U = float(input("Entrez un nombre supérieur à 1 (U) : "))

while U <= 1:
    print("Veuillez entrer un nombre supérieur à 1.")
    U = float(input("Entrez un nombre supérieur à 1 (U) : "))

somme = 0
N = 0

while somme <= U:
    N += 1
    somme += N

N -= 1

print("Le plus grand nombre N tel que la somme de 0 à N soit inférieure ou égale à", U, "est :", N)