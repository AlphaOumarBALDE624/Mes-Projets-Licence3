import random
from typing import List

"""Création de la classe Personne """

class Personne:

    def __init__(self, nom: str, proba_infection: float):
        """
        Initialise une nouvelle personne

        """
        self.nom = nom #Nom de la personne
        self.sante = "saine"  # États possibles: saine, infectee, immunisee
        self.proba_infection = proba_infection

""" Fonction pour changer l'état santé en infectee """

    def infecter(self):
        self.sante = "infectee"

    """Fonction pour changer l'état santé en immunisee"""
    def immuniser(self):
        """Change l'état de santé en 'immunisee'"""
        self.sante = "immunisee"
        
    def __str__(self):
        """Retourne une représentation textuelle de la personne"""
        return f"Personne {self.nom} ({self.sante})"

"""Création de la classe Population """

class Population:
    
    def __init__(self, taille_population: int, proba_infection: float):
        """
        Initialise une nouvelle population

        """
        self.individus: List[Personnes] = []
        for i in range(taille_population):
            self.individus.append(Personnes(f"P{i}", proba_infection))
            
    def introduire_infection(self, nombre_infectes: int):
        """
        Infecter un nombre donnee d'individus au hasard

        """
        personnes_saines = [p for p in self.individus if p.sante == "saine"]
        if len(personnes_saines) < nombre_infectes:
            nombre_infectes = len(personnes_saines)
        
        for personne in random.sample(personnes_saines, nombre_infectes):
            personne.infecter()
            
    def simuler_jour(self, proba_guerison: float):
        """
        Simulation d'une journée de propagation de la maladie

        """
        # Liste des personnes infectées suite à un contact
        infectes = [p for p in self.individus if p.sante == "infectee"]
        
        # Simulation des contacts et infections
        for personne in self.individus:
            if personne.sante == "saine":
                # Chance d'être infecté par chaque personne infectée
                for infecte in infectes:
                    if random.random() < personne.proba_infection:
                        personne.infecter()
                        break
                        
        # Simulation des guérisons
        for personne in self.individus:
            if personne.sante == "infectee":
                if random.random() < proba_guerison:
                    personne.immuniser()
                    
    def __str__(self):
        """Retourne un résumé de l'état de la population"""
        sains = sum(1 for p in self.individus if p.sante == "saine")
        infectes = sum(1 for p in self.individus if p.sante == "infectee")
        immunises = sum(1 for p in self.individus if p.sante == "immunisee")
        
        return f"Population: {len(self.individus)} personnes\n" \
               f"- Saines: {sains}\n" \
               f"- Infectées: {infectes}\n" \
               f"- Immunisées: {immunises}"

def main():
    # Création de la population
    population1 = Population(1000, 0.1)
    
    # Introduction de l'infection initiale
    population1.introduire_infection(10)
    
    # Simulation sur 30 jours
    for jour in range(30):
        population1.simuler_jour(0.05)
        print(f"\nJour {jour + 1}:")
        print(population1)

if __name__ == "__main__":
    main()