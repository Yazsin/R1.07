nb = int(input("Veuillez saisir un nombre :"))
r=0
if nb== 0 :
    print("votre nombre est 0")
elif nb> 0:
    r=nb%2
    if r==0:
        print("votre nombre est positif et impair")
        else :
            print("votre nombre est negatif et  1pair")
        else