BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbdeConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
nouvelleQuantitefromage=fromage * nbdeConvives/BASE
nouvelleQuantiteeau=eau * nbdeConvives/BASE
nouvelleQuantiteail=ail * nbdeConvives/BASE
nouvelleQuantitepain=pain * nbdeConvives/BASE

print(f"recette pour {nbdeConvives}")
print(f"Pour faire une fondue fribourgeoise pour" ,nbdeConvives, "personnes, il vous faut")

print(f"-{nouvelleQuantitefromage} gr de fromage")
print(f"-{nouvelleQuantiteeau} dl d'eau")
print(f"-{nouvelleQuantiteail} gousse(s) d'ail")
print(f"-{nouvelleQuantitepain} gr de pain")