#ici on a chiffrer un message par le technique de substituion mono-alphabétique.MARIE-MICHELE1
import random
import tkinter as tk
HAUTEUR = 600
LARGEUR = 600
#definition de l'alphabet
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("alphabet original:",alphabet)
#cle de substitution 
clef = list(alphabet)
random.shuffle(clef)
print("nouvel alphabet:",clef)
message = input("entrez votre message :")

#definir une fonction qui va chiffrer le message
def chiffre_message(message):
    #initialisation d'une variable qui contient le message chiffré 
    message_chiffre = ""
    #on chiffre chaque caractere du message, on vérifie que chaque carctere est dans l'alphabaet.
    #on determine l'indice de ce caractere dans la liste alphabet grace a index()
    #la fonction renvoie la variable message chiffre.
    for caractere in message:
        if caractere in alphabet:
            indice = alphabet.index(caractere)
            caractere_chiffre = clef[indice]
            message_chiffre += caractere_chiffre
        else:
            message_chiffre += caractere
    return message_chiffre

message_chiffre = chiffre_message(message)
print("message original:",message)
print("message chiffré:",message_chiffre)

#décryptage d'un message avec clef connue. 
clef = list("MNLAVRBOZJKYDSWHEFCXTUPQGI")

racine =tk.Tk()
racine.title("")
canvas=tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)

racine.mainloop()