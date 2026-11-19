NombreNote = int(input("Entrez le nombre de note : "))
sommeNote=0
for i in range (1,NombreNote+1):
    X=input("Saisir une note et un coeff")
    resu =X.split(" ")
    print(resu)
    note = float(resu[0])
    coef = float(resu[1])
    print(note, coef)
    SommeNote += note*coef
if (moyenne > 10) & (note >8):
    print("Vous avez réussi avec une moyenne de : ", moyenne)
else:
    print("Echoueeee")

