class Voiture:
    def __init__(self, couleur="rouge"):
        self.couleur = couleur
        self._vitesse_max = 220
        self._vitesse = 0
        self.est_demarree = False
        print("Création d'une voiture")

    def __str__(self):
        return f"Une voiture {self.couleur} avec une vitesse max de {self._vitesse_max} km/h"


    def demarrer(self):
        if (not self.est_demarree): 
            self.est_demarree = True
            
    def avancer(self, vitesse_cible):
        if (self.est_demarree):
            for i in range(self._vitesse, min(vitesse_cible, self._vitesse_max)):
                self._vitesse += 1
                print(self._vitesse)

ma_voiture = Voiture()
print(ma_voiture)
ma_voiture.demarrer()
ma_voiture.avancer(20)
ma_voiture.avancer(100)
ma_voiture.avancer(500)
# print(ma_voiture.couleur)

ta_voiture = Voiture("bleue")
print(ta_voiture)
# print(ta_voiture.couleur)

# sa_voiture = Voiture()
# print(sa_voiture.couleur)