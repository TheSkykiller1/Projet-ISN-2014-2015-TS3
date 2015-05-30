# coding: utf-8
#Cette première ligne permet l'utilisation des accents
#-------------------------------------------------------------------------------
# Name:        Bataille navale programme principal
# Version:     Version tkinter

# Author:      Borio Arnaud,Hervieu Sophia, Thibaud
# Copyright:   (c) borioarnaud,hervieusophia,thibaud 2015

# Code et débogage: Arnaud Borio
# Affichage graphique: Sophia Hervieu
# Création des damiers et assistance création des systèmes de tir: Thibaud
#-------------------------------------------------------------------------------
#======================Import de tous les modules================
from random import*
import random
import tir_util
import tir_ia
from time import sleep
from tkinter import*
import threading
#=========================Initialisation================
bateau_ia = {'Attaquant': 2, #Crée des listes de bateaux pour l'ordinateur (IA) et le joueur (Util ou Utilisateur)
 'Croiseur': 4,
 'Destroyer': 3,
 'Porte avion': 5,
 'Sous marin': 3}
bateau_util={'Attaquant': 2,
 'Croiseur': 4,
 'Destroyer': 3,
 'Porte avion': 5,
 'Sous marin': 3}
#Désignation des listes principales
list_tir_ia=[]#liste des tirs effectués par l'ordinateur et par l'utilisateur
list_tir_util=[]#Elles permettent d'empêcher de tirer 2 fois aux mêmes coordonnées
deb_bateau=['A','C','D','P','S'] #Les premières lettres de chaque bateau
autoriser_lettre=['A','B','C','D','E','F','G','H','I','J']#Listes de lettres et nombres utilisés dans des vérifications
autoriser_nombre=['1','2','3','4','5','6','7','8','9','10']
damier_ia=[]#Les damiers de l'ordinateur et du joueur
damier_utilisateur=[]
gagner="Pas fini!"#Variables de test
fin=False
#=====================Redémarrage de la partie==============
def redemarrage(): #Réinitialise toutes les données qui ont étés modifiées lors de l'utilisation
    global damier_ia,bateau_ia,deb_bateau,damier_utilisateur,bateau_util,deb_bateau,autoriser_lettre,autoriser_nombre,can1,can2,list_tir_ia,list_tir_util
    damier_ia=[]
    damier_utilisateur=[]
    finforce=False
    gagner=False
    list_tir_ia=[]
    list_tir_util=[]
    damier_ia=tableau_ia(damier_ia)
    damier_utilisateur=tableau_util(damier_utilisateur)
    actualiser_ia(damier_ia)
    actualiser_util(damier_utilisateur)
    jeux_thread()
#======================Damiers==================
#damier de l'ordinateur
def tableau_ia(damier_ia):
    for ligne in range(0,10):
        damier_ia.append([])
        for colonne in range (0,10):
            damier_ia[ligne].append(' ')
    return damier_ia
#damier de l'utilisateur
def tableau_util(damier_utilisateur):
    for ligne in range(0,10):
        damier_utilisateur.append([])
        for colonne in range (0,10):
            damier_utilisateur[ligne].append(' ')
    return damier_utilisateur
damier_ia=tableau_ia(damier_ia)
damier_utilisateur=tableau_util(damier_utilisateur)
#Initialisation des grilles tkinter (lettres et chiffres sur les côtés des damiers):
def initialisation_grilles(can):
    for colonne in range(0,10):#Lettres en abscisse
        x,y=colonne*40+60,20
        texte=chr(97+colonne)#Création des lettres à chaque passage dans la boucle
        texte=str.capitalize(texte)
        if texte =="J":
            texte="|     "+texte+"     |"
        else:
            texte="|     "+texte+"      "
        can.create_text(x, y, text=texte)#Affichage de la valeur sur la fenêtre
    for ligne in range(0,20):#Chiffres et nombres en ordonnée
        if ligne==0 or ligne==2 or ligne==4 or ligne==6 or ligne==8 or ligne==10 or ligne==12 or ligne==14 or ligne==16 or ligne==18 or ligne==20:
            x,y=20,ligne/2*40+40
            texte="-----"#Barre de séparation des lignes
        else:
            x,y=20,ligne/2*40+40
            texte=int(ligne/2+0.5)
        can.create_text(x, y, text=texte)
#Actualisation des damiers:
def actualiser_ia(damier_ia): #Vérifie l'état du damier et change les cases modifiées
    global can1
    r=20
    for ligne in range(0,10):
            for colonne in range (0,10):
                x,y=colonne*40+60,ligne*40+60
                if damier_ia[ligne][colonne]=='1':
                    can1.create_rectangle (x-r,y-r,x+r,y+r,fill='blue',outline='black')
                elif damier_ia[ligne][colonne]==' ':
                    can1.create_rectangle (x-r,y-r,x+r,y+r,fill='blue',outline='black')
                elif damier_ia[ligne][colonne]=='2':
                    can1.create_rectangle (x-r,y-r,x+r,y+r,fill='red',outline='black')
                elif damier_ia[ligne][colonne]=='3':
                    can1.create_rectangle (x-r,y-r,x+r,y+r,fill='yellow',outline='black')

def actualiser_util(damier_utilisateur):#Vérifie l'état du damier et change les cases modifiées
    global can2
    r=20
    for ligne in range(0,10):
            for colonne in range (0,10):
                x,y=colonne*40+60,ligne*40+60
                if damier_utilisateur[ligne][colonne] == 'A':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='grey',outline='black')
                elif damier_utilisateur[ligne][colonne]=='C':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='grey',outline='black')
                elif damier_utilisateur[ligne][colonne]=='D':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='grey',outline='black')
                elif damier_utilisateur[ligne][colonne]=='P':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='grey',outline='black')
                elif damier_utilisateur[ligne][colonne]=='S':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='grey',outline='black')
                elif damier_utilisateur[ligne][colonne]==' ':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='blue',outline='black')
                elif damier_utilisateur[ligne][colonne]=='2':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='red',outline='black')
                elif damier_utilisateur[ligne][colonne]=='3':
                    can2.create_rectangle(x-r,y-r,x+r,y+r,fill='yellow',outline='black')
#===================Génération Bateau================
#Génération des bateaux de l'ia
def generation_bateau_ia(damier_ia,bateau_ia,deb_bateau):
    for bateau_ia_interne in bateau_ia.keys():  #prend les éléments dans le dictionnaire
        correct=False
        while correct == False:                 #boucle de vérification du placement
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
            o = random.randint(0,1)             #  0=verticalement  /  1=horizontalement
            if o == 0:sens = "v"
            else:sens = "h"
                                                #Début des vérifications de position
            if sens == "v" and x+bateau_ia[bateau_ia_interne]> 10:correct= False #Vérifie que le bateau ne sorte pas du damier
            elif sens == "h" and y+bateau_ia[bateau_ia_interne] > 10:correct= False
            else:
                if sens == "v":
                    for i in range(0,bateau_ia[bateau_ia_interne],1):
                        if damier_ia[x+i][y] == " ":correct=True #Vérifie que les positions du bateau sont libres
                        else:
                            correct=False
                            break               #Casse la boucle si la position est déjà prise et demande une autre position
                elif sens == "h":
                    for i in range(0,bateau_ia[bateau_ia_interne],1):
                        if damier_ia[x][y+i] ==" ":correct=True
                        else:
                            correct= False
                            break
        damier_ia=placer_ia(damier_ia,bateau_ia[bateau_ia_interne],sens,x,y) #Place le bateau (dans une autre def pour éviter des bugs de python)
    return damier_ia    #actualise le damier
def placer_ia(damier_ia,bateau,sens,x,y):
    if sens == "v":
        for i in range(0,bateau,1): #Place le bateau dans le sens demandé et sur le nombre de cases requise et assigne '1' comme présence de bateau sur le damier (invisible au joueur)
            damier_ia[x+i][y] = '1'
    elif sens == "h":
        for i in range(0,bateau,1):
            damier_ia[x][y+i] = '1'
    return damier_ia

#===============Génération des bateaux joueur===============#Même fonction que celle de l'ordinateur mais adaptée à l'utilisation du joueur
def generation_bateau_util(damier_utilisateur,bateau_util,deb_bateau,autoriser_lettre,autoriser_nombre):
    n=5                         #compteur du nombre de bateaux restants
    for bateau_util_interne in bateau_util.keys():
        correct=False
        n=n-1
        while correct == False: #Test que les positions sont correctes
            msgconsole="Le joueur place un " + bateau_util_interne + ", Taille: "+str(bateau_util[bateau_util_interne])+ ", Bateaux restants :"+str(n)
            console.set(msgconsole)         #Prévient le joueur qu'il va placer un certain type de bateau et sa taille, et le nombre restant de bateaux à plaçer
            testlettre,testnombre,testorient=False,False,False
            texte_input.set("")             #Texte de la boite d'entrée des valeurs remis à zéros
            while testlettre == False:      #Différents test pour prendre les coordonnées et vérifier que le joueur n'entre pas une coordonnée invalide
                console2.set("Donner une lettre de A a J : ")
                sleep(1)
                y = tk_input.get()                  #Prend la valeur de la boite d'entrée
                y=str.capitalize(y)                 #Met la valeur en majuscule
                testlettre = y in autoriser_lettre  #teste la valeur si elle est valide ou non (si non retour au début du while)
            texte_input.set("")                     #Texte de la boite d'entrée des valeurs remis à zéro
            y=autoriser_lettre.index(y)             #assignement de la lettre à une valeur chiffrée
            while testnombre == False:
                console2.set("Donner un nombre de 1 a 10 : ")
                sleep(5)#Laisse un temps pour ne pas faire trop de tours de la boucle et laisser le joueur entrer "10"
                x = tk_input.get()
                testnombre = x in autoriser_nombre
            texte_input.set("")
            x=autoriser_nombre.index(x)
            while testorient == False:
                console2.set("Donnez l'orientation du bateau [verticalement ou horizontalement (v ou h)] : ")
                sleep(1)
                sens = tk_input.get()
                if sens=='v' or sens=='h':
                    testorient=True
                else:testorient=False
            if sens == "v" and x+bateau_util[bateau_util_interne]> 10: #vérification sur le même principe que l'ordinateur
                correct= False
            elif sens == "h" and y+bateau_util[bateau_util_interne] > 10:
                correct= False
            else:
                if sens == "v":
                    for i in range(0,bateau_util[bateau_util_interne],1):
                        if damier_utilisateur[x+i][y] == " ":
                            correct=True
                        else:
                            correct=False
                            break
                elif sens == "h":
                    for i in range(0,bateau_util[bateau_util_interne],1):
                        if damier_utilisateur[x][y+i] ==" ":
                            correct=True
                        else:
                            correct= False
                            break
            speconsole.set("")#Texte de la console d'information du bouton "lancer" remis à zéro
        damier_utilisateur=placer_util(damier_utilisateur,bateau_util[bateau_util_interne],bateau_util_interne,sens,x,y)
        actualiser_util(damier_utilisateur)#Actualise tkinter
    return damier_utilisateur
def placer_util(damier_utilisateur,bateau,bateau_util_interne,sens,x,y):
    if sens == "v":
        for i in range(0,bateau,1):
            damier_utilisateur[x+i][y] = bateau_util_interne[0]
    elif sens == "h":
        for i in range(0,bateau,1):
            damier_utilisateur[x][y+i] = bateau_util_interne[0]
    return damier_utilisateur
#====================Definitions================================
def testgagner_util(damier_ia):#Les testgagner vérifient les damiers des joueurs et préviennent de la fin de partie
    global gagner
    for ligne in range(0,10):
        for colonne in range (0,10):
            if damier_ia[ligne][colonne]=='1':
                gagner=False
                break
            else:
                gagner=True
        if gagner==False:
            break
    if gagner == True:
        console2.set("Partie finie : Le joueur a gagné!")
    return gagner

def testgagner_ia(damier_utilisateur):
    global gagner
    for ligne in range(0,10):
        for colonne in range (0,10):
            tableau=damier_utilisateur[ligne][colonne]
            if tableau == 'A' or tableau=='C' or tableau=='D' or tableau=='P' or tableau=='S':
                gagner=False
                break
            else:
                gagner=True
        if gagner==False:
            break
    if gagner == True:
        console2.set("Partie finie : l'ordinateur a gagné!")
    return gagner
#====================Commencement du jeu========================
def verifbouton():#Permet d'éviter de lancer 2 parties en même temps
    global boutonlancer,fin
    if boutonlancer==False:
        boutonlancer=True
        jeux_thread()
    elif boutonlancer==True:
        if fin==True:
            speconsole.set("Veuillez redémarrer le jeu.")
        else:
            speconsole.set("Vous ne pouvez pas lancer une autre partie pendant la précédente!")
def jeux_thread():#Lance le thread de calculs permettant de laisser tkinter affiché pendant les calculs sans bug
    def jeux():
        global damier_ia,bateau_ia,deb_bateau,damier_utilisateur,bateau_util,deb_bateau,autoriser_lettre,autoriser_nombre,list_tir_util,list_tir_ia,gagner,finforce,fin
        if fin==True:
            console.set("Veuillez redémarrer le jeu.")#Si le test précédent n'a pas été effectué (python peut être instable avec les threads)
        else:
            generation_bateau_ia(damier_ia,bateau_ia,deb_bateau)#Lance la génération des bateaux IA
            damier_utilisateur=generation_bateau_util(damier_utilisateur,bateau_util,deb_bateau,autoriser_lettre,autoriser_nombre)#Lance la génération des bateaux du joueur
            gagner=False
            finforce=False
            while gagner==False and finforce==False:        #La partie s'effectue dans ce while
                speconsole.set("")                          #Texte de la console d'information du bouton "lancer" remis à zéros
                console.set("Le joueur tire")   #Message au joueur d'information du tour
                tir_util.verifinput(autoriser_lettre,autoriser_nombre,list_tir_util,damier_ia,console2,tk_input,texte_input)
                actualiser_ia(damier_ia)#Actualiser tkinter
                gagner=testgagner_util(damier_ia)#Vérifie la condition
                if gagner==True:
                    break
                sleep(3)
                speconsole.set("")
                console.set("L'ordinateur tire") #Message au joueur d'information du tour
                tir_ia.tir_aleatoire(autoriser_lettre,autoriser_nombre,list_tir_ia,damier_utilisateur,console2)
                actualiser_util(damier_utilisateur)#Actualiser tkinter
                gagner=testgagner_ia(damier_utilisateur)
                if gagner==True:
                    break
                sleep(4)
                speconsole.set("")
                testfin=False
                texte_input.set("")
                console2.set("")
                while testfin!=True:
                    console.set("Voulez-vous arrêter la partie en cours ? [Y (oui) ou N (non)]")
                    fintest=tk_input.get()
                    if fintest=='Y' or fintest=='y':
                        finforce=True
                        testfin=True
                    elif fintest=='N' or fintest=='n':
                        finforce=False
                        testfin=True
            speconsole.set("")
            texte_input.set("")
            testredem=False
            while testredem !=True:
                console.set("Voulez-vous redémarrer la partie ? (Y ou N)")
                redem=tk_input.get()#.get() s'utilise dans des while car il ne bloque pas l'action comme les input
                if redem=='Y' or redem=='y':
                    testredem=True
                    redemarrage()
                elif redem=='N' or redem=='n':
                    fin=True
                    testredem=True
                    console.set("Fin de la partie")
    threadjeux = threading.Thread(target=jeux)#Second thread permettant les calculs en fond
    threadjeux.start()

fen1 = Tk()#crée la fenêtre de jeu
fen1.title('Bataille Navale ISN 2014-2015')
console = StringVar() #affichage des messages importants
console.set("En attente de la partie")
console2 = StringVar() #affichage des messages directs
console2.set("")
speconsole = StringVar() #Affichage des messages de mauvaise utilisation du programme
speconsole.set("")
menu = LabelFrame(fen1, text="Menu") #Frame du menu avec création des boutons et afficheurs et entrée "tk_input"
bou2 = Button(menu,text='Lancer une partie',command=verifbouton)
bou2.pack(side="left",anchor=N)
bou1 = Button(menu,text='Quitter',command=fen1.destroy)
bou1.pack(side="left",anchor=N)
affichage3=Label(menu, textvariable=speconsole)
affichage3.pack(side="top")
affichage=Label(menu, textvariable=console)
affichage.pack(side="top",pady=5)
affichage2=Label(menu, textvariable=console2)
affichage2.pack(side="top",pady=1)
texte_input = StringVar()
tk_input = Entry(menu, textvariable=texte_input)
tk_input.pack(side="top",pady=10)#Créer un "input" mais de "façon tkinter" le nom à été choisi
menu.pack(side=TOP,fill=BOTH, anchor=N)

Joueurframe = LabelFrame(fen1, text="Grille du joueur")#Frame du joueur
Joueurframe.pack(side=LEFT, anchor=SW,pady=10)
can2 = Canvas(Joueurframe,bg='light blue',heigh=440,width=440) #grille joueur
can2.pack()
ordinateurframe = LabelFrame(fen1, text="Grille de l'ordinateur") #Frame de l'ordinateur
ordinateurframe.pack(side=LEFT, anchor=SE,pady=10)
can1 = Canvas(ordinateurframe,bg='#FF6666',heigh=440,width=440) #grille ennemi
can1.pack()
initialisation_grilles(can1) #Initialise les chiffres/nombres et les lettres autour des grilles
initialisation_grilles(can2)
actualiser_ia(damier_ia)    #Crée les grilles en fonctions des damiers
actualiser_util(damier_utilisateur)
boutonlancer=False #Statu du bouton lancer pour sa vérification
fen1.resizable(width=False, height=False)
fen1.mainloop ()
