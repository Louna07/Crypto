#marie_subst_monoalphabetique
import random 
liste_a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#creation liste contenant 26 lettres de l'alphabet
print("alphabet originale :",liste_a)
clef = liste_a
random.shuffle(liste_a)
#fonction creation de la clef par mélange aleatoire de la liste alphabet
print("clef:",liste_a)
msg_crypt = "BONJOUR LA CLEF EST SOUS LE TAPIS"
