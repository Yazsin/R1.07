age = int(input("Merci de saisir votre âge"))
import datetime
annee = datetime.date.today().year

annee = annee - age
print("Votre année de naissance est : ", annee)