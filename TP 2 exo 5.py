nb = int(input("Veuillez saisir un nombre :"))
r= nb%2
if r == 0 and nb!=0:
    if nb>0:
        print("votre nombre est positif et pair")
    else :
        print("votre nombre est negatif et pair")
elif r!=0 and nb>0:
    print("votre nombre est positif et impair")
elif r!=0 and nb<0:
        print("votre nombre est negatif et impair")
else: print("votre nombre est 0")