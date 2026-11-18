import random
R=random.randint(0,100)
N=int(input("Veuillez saisir un nombre : "))
C=0
while N!=R:
    if N>R:
        print("La veleur est plus petite")
        C = C+1
        N = int(input("Veuillez saisir un nombre : "))
    elif N<R:
        print("La veleur est plus grande")
        C = C+1
        N = int(input("Veuillez saisir un nombre : "))
        print(C)
    else:
        N = int(input("Veuillez saisir un nombre : "))
        print("Vous avez réussi la valeur est ", R ,"Vous avez jouer ", C ,"fois")
