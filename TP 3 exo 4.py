import random
R=random.randint(0,100)
N=int(input("Veuillez saisir un nombre : "))
C=1
while N!=R:
    C = C + 1
    if N>R:
        print("La veleur est plus petite")
        N = int(input("Veuillez saisir un nombre : "))
        print("Nombre de tentatives :", C)
    elif N<R:
        print("La veleur est plus grande")
        N = int(input("Veuillez saisir un nombre : "))
        print("Nombre de tentatives :", C)
    else:
        N = int(input("Veuillez saisir un nombre : "))
print("Vous avez réussi la valeur est ", R ,"Vous avez jouer ", C ,"fois")
