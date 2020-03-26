import time
import pickle

CodeBarre = []

class Produit:
    def _init_(self,CodeBarre,NomProduit):
      self.Code_Barre = CodeBarre
      self.Nom_Produit = NomProduit
        
    def get_CodeBarre (self):
      start_time = time.time()
      print("Temps d'enregistrement : %s secondes ---" % (time.time() - start_time))
      return self.Code_Barre
    
    def get_NomProduit(self):
      return self.Nom_Produit

    def set_CodeBarre(self, CodeBarre,NomProduit):

        if CodeBarre is None :
          self.Code_Barre = "Produit introuvable"
          
        else : 
          self.Code_Barre = NomProduit
          
        # Enregistrer le Produit
          pickle.load(self.Nom_Produit) 

        # Afficher le nom du produit
          def _str_(self) :
            return "Produit : {}".format(self.Nom_Produit)



  


          


