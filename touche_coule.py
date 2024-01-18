###############################################################################
## Programme graphique interactif en Python à l'aide du module Turtle qui
## permet de programmer une version simplifiée du jeu Touché-coulé
###############################################################################
## Auteur: Ben Amor Hazem
## Date: 04/04/2023
## Email: hazem.ben.amor@umontreal.ca
###############################################################################

from turtle import * 
import math as math
from random import *

def arc(r, angle):
    """Cette fonction permet de tracer un arc de cercle

    Args:
        r (int): Rayon de l'arc
        angle (int): Angle de l'arc
    """
    longueur_arc = 2 * math.pi * r * angle / 360
    n = int(longueur_arc / 3) + 1
    longueur_etape = longueur_arc / n
    angle_etape = float(angle) / n
    for _ in range(n):
        fd(longueur_etape)
        lt(angle_etape)


def cercle(r):
    """Cette fonction permet de dessiner un cercle

    Args:
        r (int): Longueur du rayon
    """
    arc(r, 360)

# 
def carre(cote):
    """ette fonction permet de dessiner un carré

    Args:
        cote (int): Longueur d'un coté
    """
    for _ in range(4):
        fd(cote); lt(90)

# 
def positionner(x, y):
    """Cette fonction permet de positionner la tortue relativement à son emplacement actuel

    Args:
        x (int): Nombre de pas en x
        y (int): Nombre de pas en y
    """
    pu(); fd(x); lt(90); fd(y); rt(90); pd()

def bateau(grille):
    #Cette foncntion permet de générer les positions des bateaux sur la grille
    listeind=[]
    for i in range(5):
        j=randint(0,5)
        k=randint(0,5)
        while grille[j][k]=="b":
            j=randint(0,5)
            k=randint(0,5)
        grille[j][k]="b"
        listeind.append((j,k))
    return(listeind)

def convinv(ch):
    #Cette fonction permet de tranformer des coordonnées sous forme de lettre(exp:A1)
    #en coordonnées numérique(exp:0,0) 
    i,j=0,0
    if ch[0]=="A":
        j=0
    elif ch[0]=="B":
        j=1
    elif ch[0]=="C":
        j=2
    elif ch[0]=="D":
        j=3    
    elif ch[0]=="E":
        j=4
    elif ch[0]=="F":
        j=5
    if ch[1]=="1":
        i=0
    elif ch[1]=="2":
        i=1
    elif ch[1]=="3":
        i=2
    elif ch[1]=="4":
        i=3
    elif ch[1]=="5":
        i=4
    elif ch[1]==6:
        i=5
    return i,j

def eq(l):
    #Cette fonction permet de tranformer des coordonnées numérique (exp:0,0) 
    #en coordonnées sous forme de lettre(exp:A1)
    liste=[]
    for k in range(5):
        j,i=l[k]
        corr=""
        if i==0:
            corr=corr+"A"
        elif i==1:
            corr=corr+"B"
        elif i==2:
            corr=corr+"C"
        elif i==3:
            corr=corr+"D"
        elif i==4:
            corr=corr+"E"
        elif i==5:
            corr=corr+"F"
        if j==0 :
            corr=corr+"1"
        elif j==1 :
            corr=corr+"2"
        elif j==2 :
            corr=corr+"3"
        elif j==3 :
            corr=corr+"4"
        elif j==4 :
            corr=corr+"5"
        elif j==5 :
            corr=corr+"6"
        liste.append(corr)
    return liste
                
def grille(cols, lignes, taille, espace):
    #Cette fonction permet de dessiner la grille
    for x in range(cols):
        for y in range(lignes):
            positionner(x * (taille + espace), y * (taille + espace))
            carre(taille)
            positionner(-x * (taille + espace), -y * (taille + espace))

def touchée(i,j):
    #Cette fonction permet de dessiner un cercle rouge au cas d'une tentative juste
    pu()
    positionner(((j*20)+8),(((5-i)*16)+(5-i)*4))
    pd()
    pensize(4)
    pencolor("red")
    cercle(8)
    pencolor("black")
    pensize(1)
    pu()
    home()
    pd()
def ratée(i,j):
     #Cette fonction permet de dessiner un carré barré d'un croix au cas d'une tentative ratée
    pu()
    positionner(((j*20)),(((5-i)*16)+(5-i)*4))
    pd()
    pensize(4)
    pencolor("green")
    carre(16)
    lt(45)
    fd(math.sqrt(2)*16)
    rt(135)
    fd(16)
    rt(135)
    fd(math.sqrt(2)*16)
    pencolor("black")
    pensize(1)
    pu()
    home()
    pd()
   
def deroulement(joueur,liste1,liste2):
        #Cette fonction assure le déroulement de jeu(Elle recupère les propositions
        #et fait appel aux fonctions touchée(i,j) et ratée(i,j) pour dessiner sur la grille
        prepo=(input("Entrez votre proposition (joueur"+str(joueur)+")")).upper()
        while not ((joueur==1 and (prepo in choixposs1)) or (joueur==2 and (prepo in choixposs2))):
            prepo=(input("Entrez votre proposition (joueur"+str(joueur)+")")).upper()

        if int(joueur)==1:
            pu() 
            home()
            bk(200)
            pd()
        if prepo in liste2 :
                i,j=liste1[liste2.index(prepo)]
                touchée(i,j)
                liste1.remove((i,j))
                liste2.remove(prepo)                
                print("touché")
                if joueur==1:
                    choixposs1.remove(prepo)
                else:
                    choixposs2.remove(prepo)
                    
        else:
            i,j=convinv(prepo)
            ratée(i,j)
            print("ratée")
        

def jouer():
        #Fonction principale
        global choixposs1
        global choixposs2
        choixposs1=["A1","A2","A3","A4","A5","A6","B1","B2","B3","B4",
                   "B5","B6","C1","C2","C3","C4","C5","C6","D1","D2",
                   "D3","D4","D5","D6","E1","E2","E3","E4","E5","E6",
                   "F1","F2","F3","F4","F5","F6"]
        choixposs2=["A1","A2","A3","A4","A5","A6","B1","B2","B3","B4",
                   "B5","B6","C1","C2","C3","C4","C5","C6","D1","D2",
                   "D3","D4","D5","D6","E1","E2","E3","E4","E5","E6",
                   "F1","F2","F3","F4","F5","F6"]

        speed(0)
        delay(0)
        grille(6,6,16,4)
        pu()
        bk(40)
        lt(90)
        bk(30)
        pd()
        pencolor("blue")
        pensize(10)
        fd(170)
        pu()
        home()
        bk(200)
        pd()
        pencolor("black")
        pensize(1)
        grille(6,6,16,4)
        g=[["","","","","",""],
                 ["","","","","",""],
                 ["","","","","",""],
                 ["","","","","",""],
                 ["","","","","",""],
                 ["","","","","",""]]
        liste1=bateau(g)
        liste2=bateau(g)
        listeind1=eq(liste1)
        listeind2=eq(liste2)
        while True:
            deroulement(1,liste2,listeind2)
            deroulement(2,liste1,listeind1)
            if len(liste1)==0:
                print("joueur 2 a gagné")
                break
            elif len(liste2)==0:
                print("joueur 1 a gagné")
                break
jouer()
                
                
            
        
             
             
             
             
         
         
    
    


      
    
    