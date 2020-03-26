# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:08:56 2020

@author: Tom Stockholm
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:52:17 2020
@author: Tom Stockholm
"""
import random

class Carte():
    def __init__(self,couleur,valeur):
            self.couleur = couleur
            self.valeur = valeur
    def montrer(self):
        print("{} de {}".format(self.valeur,self.couleur))
    
class Deck():
    def __init__(self):
        self.cartes = []
        self.contruire()
        
    def contruire(self):
        for s in ["Pique","Trèfle","Carreau","Coeur"]:
            for v in range(1,14):
                self.cartes.append(Carte(s,v))
                
    def montrer(self):
        for cartes in self.cartes:
            cartes.montrer()
            
    def melanger(self):
        for i in range(len(self.cartes)-1,0,-1):
            r = random.randint(0,i)
            self.cartes[i],self.cartes[r] = self.cartes[r],self.cartes[i]
             
            
            
    def tirer_carte(self):
        return self.cartes.pop()
     



class Joueur():
    def __init__(self,prenom):
        self.prenom = prenom
        self.main = []
        
    def tirer_carte(self,deck):
        self.main.append(deck.tirer_carte())
        
    def montrer_main(self):
        for cartes in self.main:
            cartes.montrer()
            


#avec cette modélisation on peut faire nimporte quel jeu de carte, exemple d'un petit jeu de bataille.
            


jeu_en_cours = True

while jeu_en_cours:
    nom1 = input("Entrez le nom du joueur 1 :")
    nom2 = input("Entrez le nom du joueur 2 :")
    
    joueur1 = Joueur(nom1)
    joueur2 = Joueur(nom2)
    
    deck = Deck()
    deck.contruire()
    deck.melanger()

    joueur1.tirer_carte(deck)
    joueur2.tirer_carte(deck)

    print(f"{joueur1.prenom} a pioché un : ")
    joueur1.montrer_main()
    print(f"{joueur2.prenom} a pioché un : ")
    joueur2.montrer_main()

    cj1 = joueur1.main[0]
    cj2 = joueur2.main[0]
    
    if  cj1.valeur > cj2.valeur:
        print(f"{joueur1.prenom} gagne")
    else:
        print(f"{joueur2.prenom} gagne")
    jeu_en_cours = False

            
