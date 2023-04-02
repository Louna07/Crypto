#ici on a chiffrer un message par le technique de substituion mono-alphabétique.MARIE-MICHELE1
import random
#definition de l'alphabet
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("alphabet original:",alphabet)
#création de notre clè de substitution 
substitution = list(alphabet)
random.shuffle(substitution)
print("nouvel alphabet:",substitution)
message = input("entrez votre message en majuscule :")
#definir la fonction qui va chiffrer le message
def chiffre_message(message):
    #initialisation du message chiffré
    message_chiffre = ""
    #on chiffre chaque caractere du message
    for caractere in message:
        if caractere in alphabet:
            indice = alphabet.index(caractere)
            caractere_chiffre = substitution[indice]
            message_chiffre += caractere_chiffre
        else:
            message_chiffre += caractere
    return message_chiffre
message_chiffre = chiffre_message(message)
print("message original:",message)
print("message chiffré:",message_chiffre)
