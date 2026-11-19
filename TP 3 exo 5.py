from math import factorial

x=input("Veuillez choisir entre la boucle for ou while : ")
if x =="while":
    valeur=int(input("Veuillez saisir un nombre"))
    for i in range(1,valeur+1):
        factorielle = i*i
        print(factorielle)
if x =="for":
    valeur = int(input("Veuillez saisir un nombre"))
    for i in range(1, valeur + 1):
        factorielle = i * i
        print(factorielle)
