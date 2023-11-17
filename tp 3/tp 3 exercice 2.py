#avec for
import time

n = int(input("Entrez un nombre entier positif : "))

while n <= 0:
    print("Veuillez entrer un nombre entier positif.")
    n = int(input("Entrez un nombre entier positif : "))

print("Compte à rebours :")

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)




#avec while
import time

n = int(input("Entrez un nombre entier positif : "))

while n <= 0:
    print("Veuillez entrer un nombre entier positif.")
    n = int(input("Entrez un nombre entier positif : "))

print("Compte à rebours :")

while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)