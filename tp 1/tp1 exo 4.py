jour = 0
heure = 0
date = 0
minute = 0
print("entrez le nombre de minute depuis le début du mois (0-44700) :")
minute=int(input())
jour = minute//1440
minute = minute%1440
heure = minute//60
minute = minute%60
print(jour, heure, minute)
