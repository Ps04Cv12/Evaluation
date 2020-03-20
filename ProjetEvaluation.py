# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:06:46 2020

@author: Viviane CAI Groupe 28

Projet
But : 
Entrez le code barre du produit
Temps d'enregistrement
Lorsqu'on scanne le code barre cela nous permet de rechercher des informations (prix, nom du produit...) sur le produit
Enregistrer ce produit
Tester le programme

"""

import unittest
import pickle

class Produit:
    def _init_(self,CodeBarre,NomProduit):
        self.Code_Barre = CodeBarre
        self.Nom_Produit = NomProduit
        
    def get_CodeBarre (self):
        return self.Code_Barre
    
    def get_NomProduit(self):
        return self.Nom_Produit
    
    def set_CodeBarre(self, CodeBarre,NomProduit):
        if CodeBarre is None :
            self.Code_Barre = "Produit introuvable"
            '''
            def _str_(self):               
                return f"le code barre est indefie {self.CodeBarre}"
            '''
        else : 
            self.Code_Barre = NomProduit
            pickle.load(self.Nom_Produit) # Enregistrer le Produit
            
            # Afficher le nom du produit
            def _str_(self) :
                return "Produit : {}".format(self.Nom_Produit)
      
# Faire des tests
if __name__ == '__main__':
   unittest.main()  