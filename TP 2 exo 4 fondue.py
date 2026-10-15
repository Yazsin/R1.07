base = int(4)
fromage = int(800)
eau = int(2)
ail = int(2)
pain = int(400)
nbConvives = int(input('veuillez entrer le nombre de convives : '))
NF= fromage * nbConvives / base
Ne = eau *nbConvives / base
Na = ail *nbConvives / base
Np = pain *nbConvives / base
print("Voici les nouvelles quantité : fromage : " , NF, "g", "eau : " , Ne , "ail : " ,Na , "pain : " ,Np )
