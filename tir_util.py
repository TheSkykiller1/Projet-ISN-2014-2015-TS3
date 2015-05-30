# coding: utf8
#-------------------------------------------------------------------------------
# Name:        Fonction de tir du joueur sur la grille de l'ordinateur
#
# Author:      Borio Arnaud
# Created:     27/04/2015
# Copyright:   (c) borioarnaud 2015
# coding: utf8
#-------------------------------------------------------------------------------
import tkinter
from time import sleep
def toucher(letindex,chifindex,damier_ia,console2): #Effectue le tir

    if damier_ia[chifindex][letindex] == '1':#Vérifie si un bateau est présent ou non
        damier_ia[chifindex][letindex]='2'#Change la case de statut
        console2.set("Vous avez touché un bateau de l'ordinateur") #Affiche un message direct
        return
    elif damier_ia[chifindex][letindex] == ' ':
        damier_ia[chifindex][letindex]='3'
        console2.set("Vous avez tiré dans l'eau")
        return


#Vérification des coordonnées de tir
def verifinput(autoriser_lettre,autoriser_nombre,list_tir_util,damier_ia,console2,tk_input,texte_input):
    assemblepos=""
    test_tir_effecter = True
    while test_tir_effecter == True: #Vérifie si la coordonée n'a pas déjà été affectée aux même coordonnées
        testlettre,testnumber=False,False
        texte_input.set("")  #Met à zéro la barre d'entrée des valeurs
        while testlettre == False:
            console2.set("Tir: Coordonnée lettre de A à J: ") #Message direct
            sleep(1)#Pause pour laisser le joueur entrer une valeur
            letpos=tk_input.get()#Prend la valeur
            letpos=str.capitalize(letpos)#Met la valeur en majuscule
            testlettre = letpos in autoriser_lettre#Vérifie que la valeur est valide
        texte_input.set("")
        while testnumber == False:
            console2.set("Tir: Coordonnée nombre de 1 à 10: ")
            sleep(5)
            chifpos=tk_input.get()
            testnumber = chifpos in autoriser_nombre
        texte_input.set("")
        chifindex=autoriser_nombre.index(chifpos)#Prend la valeur chiffrée des coordonnées
        letindex=autoriser_lettre.index(letpos)
        assemblepos=letpos+chifpos#Assemble la lettre au chiffre/nombre pour le test
        test_tir_effecter = assemblepos in list_tir_util#Teste si la position n'a pas déjà été affectée
    list_tir_util.append(assemblepos)#Ajoute la position à la liste des tir effectués
    toucher(letindex,chifindex,damier_ia,console2)#Effectue le tir
