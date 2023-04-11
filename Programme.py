#Chiffrement par substitution mono-alphabétique. MARIE-MICHELE1
import random
import tkinter as tk
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

#décriptage MARIE-MICHELE2 
alphabet = list(ABCCDEFGHIJQLMNOPQRSTUVWXYZ)
#définir la clef de substitution 
clef = list(input("entrez votre clef:"))
print(clef)

#définir une fonction pour déchiffrer un message 
def dechiffre_message(message_chiffre) : 
    message_dechiffré = ""
    #dechiffrer chaque caractere du message 
    for caractere_chiffre in message_chiffre: 
        if caractere_chiffre in clef : 
            indice = clef.index(caractere_chiffre)
            caractere_dechiffre = alphabet[indice]
            message_dechiffre += caractere_dechiffre
        else:
            message_dechiffre += caractere_chiffre 
    return message_dechiffre 
#à corriger

#exemple d'utilisation 
message_chiffre = input("entrez le message à dechiffrer : ")
message_dechiffre = dechiffre_message(message_chiffre)
print("message chiffré:", message_chiffre)
print("message déchiffré:",message_dechiffre)

def encrypt_scytale(plaintext, key):
    key = int(key)
    ciphertext = [''] * key
    index = 0
    for letter in plaintext:
        ciphertext[index] += letter
        index = (index + 1) % key
    return ''.join(ciphertext)

# Fonction de déchiffrement de Scytale
def decrypt_scytale(ciphertext, key):
    key = int(key)
    plaintext = [''] * len(ciphertext)
    index = 0
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[index]
        index = (index + 1) % key
    return ''.join(plaintext)

#CodeCesarTessaCryptage
def cryptage(message, cle) : 
    message_resultat = ""
    #Si la lettre est en majuscule on utilise la méthode ord() ce qui donne la table des lettres ASCII
    for i in range(len(message)):
        lettre = message[i]
        if 65 <= ord(lettre) <= 90 :
            lettre_chiffree = chr(65 + (ord(lettre) - 65 + cle)%26) #%26 permet de se balader dans l'alphabet, -65 permet de donner la position de la lettre
                                                     #cle permet le décalage de la lettre, +65 permet de trouver le décalage de la lettre dans la table
    #Si la lettre est en minuscule
        elif 97 <= ord(lettre) <= 122 :
            lettre_chiffree = chr(97 + (ord(lettre) - 97 + cle)% 26)
        else :
            lettre_chiffree = lettre
        message_resultat += lettre_chiffree
    return message_resultat

message = "Salut, moi c'est Tessa"
cle = 1
message_resultat = cryptage(message, cle)
print("Message chiffré:", message_resultat)

#CodeCesarTessaDecryptage
def decrypt_cesar(messagecode, cle):
    message = ""
    for lettre in messagecode:
        if 65 <= ord(lettre) <= 90:
            # Décale la lettre en fonction de la clé de chiffrement
            message += chr(65 + (ord(lettre) - cle - 65) % 26)
        elif 97 <= ord(lettre) <= 122 :
            message += chr(97 + (ord(lettre) - cle - 97)% 26)
        
        else:
            message += lettre
    return message

messagecode = "Cpotpjs, kf n'bqqfmmf Ufttb."
cle = 1
message = decrypt_cesar(messagecode, cle)
print(message)

#CommencementInterphaceTessa
# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
def create():
    win = Toplevel()
    

fenetre = Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Cryptanalyse")
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
 # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
fenetre.resizable(height=False, width=False)  
# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Veuillez choisir votre cryptage")
texte1.pack()

# Fonction bouton 1

def create_Cesar ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter", command = cryptage)
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter", command=decrypt_cesar)
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Vigenere ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Scytal ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Submonoalpha ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()
# Ajout d'un bouton dans la fenêtre :
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create)
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create_Cesar)
bouton_Cesar.pack()
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create)
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create_Vigenere)
bouton_Vigenere.pack()
bouton_Scytal = Button (fenetre, text = "Scytal", command = create)
bouton_Scytal = Button (fenetre, text = "Scytal", command = create_Scytal)
bouton_Scytal.pack()
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create)
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create_Submonoalpha)
bouton_Submonoalpha.pack()

def create():
    newfenetre = tk.Toplevel()
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")
#def create():
    #newfenetre = Toplevel(fenetre)
    #newfenetre.pack()
    #labelExample = Label(fenetre, text = "New Window")
    #labelExample.pack()
    #buttonExample = Button(fenetre, text = "New Window button")
    #buttonExample.pack()
    #labelExample.grid(column= 0, row = 0)

# Affichage de la fenêtre créée : 
fenetre.mainloop()
