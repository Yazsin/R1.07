while True:
    x = int(input("Veuillez saisir un nombre: "))

    if (2 <= x <= 3) or ( 0< x  <= 1) or (-10 <= x <= -2) :
        print("Votre valeur est dans l'interval")
    else:
        print("Le nombre n'appartient pas a l'interval")
