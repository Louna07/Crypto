#marie_subst_monoalphabetique
import random 
liste_a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#création liste contenant 26 lettres de l'alphabet
print("alphabet originale :",liste_a)
random.shuffle(liste_a)
clef = liste_a
#variable création de la clef par mélange aleatoire de la liste alphabet
print("clef:",liste_a)
message = input("entrez votre message:")  
#ici on veut renvoyer une chaine de caractére pour le chiffrage
chiffrage = str()
#on parcoure chaque lettre de notre message avec la fonction
for lettre in message: 
