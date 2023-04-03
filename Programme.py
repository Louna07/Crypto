#Chiffrement par substitution mono-alphabétique. MARIE-MICHELE1
import random

#création de l'alphabet
liste_a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("alphabet original:",liste_a)

#cle de substitution 
clef = list(liste_a)
random.shuffle(clef)
print("nouvel alphabet:",clef)
message_en_clair = input("entrez votre message :")

#création de la fonction qui va chiffrer notre message
def chiffré_message(message_en_clair):
    #on créé une variable qui contiendra notre texte chiffré 
    message_chiffré = ""
    #on vérifie que chaque lettre ou caractere est dans l'alphabaet pré-définie.
    #on determine la position de la lettre dans la liste alphabet grace a index().on uttilise la position de la lettre dans la liste pour trouver la lettre correspondante dans l'alphabet de substitution
    #si la lettre ou le caractere n'est pas definie, celui ci est directemet renvoyer dans le message chiffré tels quel.
    #la fonction renvoie la variable message chiffre.
    for lettre in message_en_clair:
        if lettre in liste_a:
            position = liste_a.index(lettre)
            lettre_chiffré = clef[position]
            message_chiffré += lettre_chiffré
        else:
            message_chiffré += lettre
    return message_chiffré
#on appelle la fonction dans notre variable
message_chiffré = chiffré_message(message_en_clair)
print("message original:",message_en_clair)
print("message chiffré:",message_chiffré)
