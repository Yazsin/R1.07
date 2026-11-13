X = 0
Y = 0
Z = 0
while True :
    A = int(input("Entrez un nombre : "))


    if A < 10:
        X = X + 1
        print(f"Il y a {X} nombre inférieur à 10")
    elif 10 <= A <= 15:
        Y = Y + 1
        print(f"Il y a {Y} nombre compris entre 10 et 15")
    else:
        Z = Z + 1
        print(f"Il y a {Z} nombre strictement supérieur à 15")