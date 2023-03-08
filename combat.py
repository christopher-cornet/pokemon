from pokemon import *
from eau import *
from feu import *
from normal import *
from terre import *
import random

class Combat:
    def __init__(self):
        self.pokemon1 = Feu('Dracaufeu', 40, 70, 'Lances-Flammes', 60)
        self.pokemon2 = Eau('Maraiste', 25, 35, 'Pistolet à O', 50)
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
            print('Méthode qui return le vainqueur du combat:', self.pokemon2.name(), '!')
        elif self.pokemon2.hp() <= 0: # pokemon2 KO, vainqueur = pokemon1
            print('Méthode qui return le vainqueur du combat:', self.pokemon1.name(), '!')

    # Possibilité de rater son attaque
    def miss_attack(self):
        miss = random.randint(0, 1) # 0 = rate son attaque et 1 = touche l'adversaire
        return miss

    def fight(self):
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
                self.pokemon1.attaquer()
                self.pokemon2.set_hp(self.pokemon1.atk) # retirer les pv de pokemon2
                # Message de victoire et KO
                if self.pokemon2.hp() <= 0: # victoire pokemon1
                    self.verif_life()
                    break
                elif self.pokemon1.hp() <= 0: # victoire pokemon2
                    self.verif_life()
                    break
                # Joueur 2
                print('Que doit faire', self.pokemon2.name(), '?', 'attaquer', '/', 'fuir', self.pokemon2.hp(), 'PV')
                p2 = input()
                # Message de victoire et KO
                if self.pokemon2.hp() <= 0: # victoire pokemon1
                    self.verif_life()
                    break
                elif self.pokemon1.hp() <= 0: # victoire pokemon2
                    self.verif_life()
                    break
            elif p1 == 'fuir':
                self.pokemon1.fuir()
                break
            if p2 == 'attaquer':
                self.pokemon2.attaquer()
                self.pokemon1.set_hp(self.pokemon2.atk) # retirer les pv de pokemon2
            elif p2 == 'fuir':
                self.pokemon2.fuir()
                break
        # return le nom du vainqueur comme demandé.
        self.winner()

instance_combat = Combat()
instance_combat.fight()