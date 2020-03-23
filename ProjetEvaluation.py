import time
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
        else : 
          self.Code_Barre = NomProduit
          pickle.load(self.Nom_Produit) # Enregistrer le Produit
        
        # Afficher le nom du produit
          def _str_(self) :
            return "Produit : {}".format(self.Nom_Produit)


