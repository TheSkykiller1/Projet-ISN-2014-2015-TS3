# coding: utf8
#-------------------------------------------------------------------------------
# Name:        Fonction de tir de l'ordinateur sur la grille du joueur
# Purpose:
#
# Author:      Borio Arnaud
# Created:     27/04/2015
# Copyright:   (c) borioarnaud 2015
#-------------------------------------------------------------------------------
import tkinter
from random import *
def toucher(letindex,chifindex,damier_utilisateur,console2):#Vérifie que la position où le tir à été fait est soit vide, soit un bateau
    tableau=damier_utilisateur[chifindex][letindex]#Pour réduire la taille dans le if
    if tableau == 'A' or tableau=='C' or tableau=='D' or tableau=='P' or tableau=='S':
        damier_utilisateur[chifindex][letindex]='2' #Change le statut de la case
        console2.set("L'ordinateur a touché un de vos bateau")#Message d'information direct
        return
    elif tableau == ' ':
        damier_utilisateur[chifindex][letindex]='3'
        console2.set("L'ordinateur a loupé son tir")
        return

#tirauto
def tir_aleatoire(autoriser_lettre,autoriser_nombre,list_tir_ia,damier_utilisateur,console2):
    assemblepos=""
    test_tir_effecter = True
    while test_tir_effecter == True:
        testlettre,testnumber=False,False
        letpos=choice(autoriser_lettre) #Choix aléatoire dans la liste
        chifpos=choice(autoriser_nombre)
        chifindex=autoriser_nombre.index(chifpos) #Prend la valeur de la position dans la liste
        letindex=autoriser_lettre.index(letpos)
        assemblepos=letpos+chifpos  #Assemble la lettre et le chiffre/nombre
        test_tir_effecter = assemblepos in list_tir_ia #Vérifie que la position n'a pas été déjà utilisée
    list_tir_ia.append(assemblepos) #Ajoute la valeur à la liste des positions utilisées
    toucher(letindex,chifindex,damier_utilisateur,console2) #Effectue le tir
