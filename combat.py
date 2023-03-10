from pokemon import *
from eau import *
from feu import *
from normal import *
from terre import *
import random
import json

class Combat:
    def __init__(self):
        self.pokemon1 = Feu('Dracaufeu', 40, 70, 'Lances-Flammes', 10) # 110 PV
        self.pokemon2 = Eau('Maraiste', 25, 35, 'Pistolet a O', 20) # 115 PV
        self.fighting = True

    # victoire pokemon 1
    def win_pkmn1(self):
        print(self.pokemon2.name(), 'est KO.')
        print('Victoire de', self.pokemon1.name(), '!', self.pokemon1.name(), "a gagné 100 points d'EXP.")

    # victoire pokemon 2
    def win_pkmn2(self):
        print(self.pokemon1.name(), 'est KO.')
        print('Victoire de', self.pokemon2.name(), '!', self.pokemon2.name(), "a gagné 100 points d'EXP.")

    # méthode qui vérifie si l’un des deux Pokémon n’est plus en vie.
    def verif_life(self):
        if self.pokemon2.hp() <= 0: # le pokémon2 est KO
            self.win_pkmn1()
            self.fighting = False
        elif self.pokemon1.hp() <= 0: # le pokémon1 est KO
            self.win_pkmn2()
            self.fighting = False

    # méthode qui renvoie le nom du vainqueur.
    def winner(self):
        print() # espace pour la lisibilité
        if self.pokemon1.hp() <= 0: # pokemon1 KO, vainqueur = pokemon2
            print('Vainqueur du combat:', self.pokemon2.name(), '!')
        elif self.pokemon2.hp() <= 0: # pokemon2 KO, vainqueur = pokemon1
            print('Vainqueur du combat:', self.pokemon1.name(), '!')

    # méthode qui renvoie le nom du perdant.
    def loser(self):
        print() # espace pour la lisibilité
        if self.pokemon1.hp() <= 0: # pokemon1 KO, perdant = pokemon2
            print('Perdant du combat:', self.pokemon1.name(), '...')
        elif self.pokemon2.hp() <= 0: # pokemon2 KO, perdant = pokemon1
            print('Perdant du combat:', self.pokemon2.name(), '...')

    # Possibilité de rater son attaque
    def miss_attack(self):
        miss = random.randint(0, 1) # 0 = rate son attaque et 1 = touche l'adversaire
        return miss
    
    # récupère le type de l'adversaire et récupère sa puissance d’attaque et le multiplie
    def get_type(self):
        if type(self.pokemon2) == Eau: # Adversaire Eau
            if type(self.pokemon1) == Feu: # Joueur Feu vs Eau
                self.pokemon1.atk = self.pokemon1.atk * 0.5
            elif type(self.pokemon1) == Terre: # Joueur Terre vs Eau
                self.pokemon1.atk = self.pokemon1.atk * 2
            elif type(self.pokemon1) == Normal: # Joueur Normal vs Eau
                self.pokemon1.atk = self.pokemon1.atk * 0.75
            else:
                self.pokemon1.atk = self.pokemon1.atk * 1
        elif type(self.pokemon2) == Feu: # Adversaire Feu
            if type(self.pokemon1) == Eau: # Joueur Eau vs Feu
                self.pokemon1.atk = self.pokemon1.atk * 2
            elif type(self.pokemon1) == Terre: # Joueur Terre vs Feu
                self.pokemon1.atk = self.pokemon1.atk * 0.5
            elif type(self.pokemon1) == Normal: # Joueur Normal vs Feu
                self.pokemon1.atk = self.pokemon1.atk * 0.75
            else:
                self.pokemon1.atk = self.pokemon1.atk * 1
        elif type(self.pokemon2) == Terre: # Adversaire Terre
            if type(self.pokemon1) == Eau: # Joueur Eau vs Terre
                self.pokemon1.atk = self.pokemon1.atk * 0.5
            elif type(self.pokemon1) == Feu: # Joueur Feu vs Terre
                self.pokemon1.atk = self.pokemon1.atk * 2
            elif type(self.pokemon1) == Normal: # Joueur Normal vs Terre
                self.pokemon1.atk = self.pokemon1.atk * 0.75
            else:
                self.pokemon1.atk = self.pokemon1.atk * 1
        elif type(self.pokemon2) == Normal:
            if type(self.pokemon1) == Eau: # Joueur Eau vs Normal
                self.pokemon1.atk = self.pokemon1.atk * 1
            elif type(self.pokemon1) == Feu: # Joueur Feu vs Normal
                self.pokemon1.atk = self.pokemon1.atk * 1
            elif type(self.pokemon1) == Normal: # Joueur Terre vs Normal
                self.pokemon1.atk = self.pokemon1.atk * 1
            else:
                self.pokemon1.atk = self.pokemon1.atk * 1
        else:
            print('Type invalide.')

    # Modifier les pv en fonction de la défense pokémon1 et pokémon2
    def pkmn1_hp_def(self):
        result = self.pokemon2.atk - self.pokemon1.defense
        return result
    
    def pkmn2_hp_def(self):
        result = self.pokemon1.atk - self.pokemon2.defense
        return result
    
    # Les Pokémon sont sauvegardés dans un fichier nommé pokedex.json
    def save_pkmn_pokedex(self):
        Pokedex = {
            "nom": self.pokemon1.name(),
            "pv": self.pokemon1.hp(),
            "atk": self.pokemon1.atk,
            "atk_name": self.pokemon1.atk_name,
            "defense": self.pokemon1.defense
        }
        with open('pokedex.json', 'a') as file:
            json.dump(Pokedex, file, indent=4) # écrire en JSON

    def fight(self):
        self.get_type() # multiplie les dégâts de pokemon1 selon le type de pokemon2
        while self.fighting:
            if self.pokemon2.hp() <= 0: # victoire pokemon1
                self.verif_life()
                break
            elif self.pokemon1.hp() <= 0: # victoire pokemon2
                self.verif_life()
                break
            # Joueur 1
            print('Que doit faire', self.pokemon1.name(), '?', 'attaquer', '/', 'fuir', self.pokemon1.hp(), 'PV')
            p1 = input()
            if p1 == 'attaquer':
                self.miss_attack()
                if self.miss_attack() == 1:
                    self.pokemon1.attaquer()
                    self.pokemon2.set_hp(self.pkmn2_hp_def()) # retirer les pv de pokemon2
                    # Message de victoire et KO
                    if self.pokemon2.hp() <= 0: # victoire pokemon1
                        self.verif_life()
                        break
                    elif self.pokemon1.hp() <= 0: # victoire pokemon2
                        self.verif_life()
                        break
                else:
                    print(self.pokemon1.name(), 'a raté son attaque.')
            # Joueur 2
            print('Que doit faire', self.pokemon2.name(), '?', 'attaquer', '/', 'fuir', self.pokemon2.hp(), 'PV')
            p2 = input()
            if p2 == 'attaquer':
                self.miss_attack()
                if self.miss_attack() == 1:
                    self.pokemon2.attaquer()
                    self.pokemon1.set_hp(self.pkmn1_hp_def()) # retirer les pv de pokemon1
                    # Message de victoire et KO
                    if self.pokemon2.hp() <= 0: # victoire pokemon1
                        self.verif_life()
                        break
                    elif self.pokemon1.hp() <= 0: # victoire pokemon2
                        self.verif_life()
                        break
                else:
                    print(self.pokemon2.name(), 'a raté son attaque.')
            if p1 == 'fuir':
                self.pokemon1.fuir()
                break
            if p2 == 'fuir':
                self.pokemon2.fuir()
                break
        # return le nom du vainqueur comme demandé.
        self.winner()
        self.loser()

# Menu de début de partie
print('Lancer une partie: start')
print('Ajouter un Pokémon: add')
print('Accéder au Pokédex: pokedex')

decision = input() # Prend en compte l'action à executer

instance_combat = Combat()
instance_combat.save_pkmn_pokedex()

# Lancer une partie
if decision == 'start':
    instance_combat.fight()
elif decision == 'add':
    print('Quel pokémon ajouter ?')
    which_pkmn_add = input()