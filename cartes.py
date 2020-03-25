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
            

    


