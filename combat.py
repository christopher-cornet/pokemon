from pokemon import *
from eau import *
from feu import *
from normal import *
from terre import *

class Combat:
    def __init__(self):
        self.pokemon1 = Feu('Dracaufeu', 40, 70, 60)
        self.pokemon2 = Eau('Maraiste', 25, 35, 50)

    # victoire pokemon 1
    def win_pkmn1(self):
        print(self.pokemon2.name(), 'est KO.')
        print('Victoire de', self.pokemon1.name(), '!')

    # victoire pokemon 2
    def win_pkmn2(self):
        print(self.pokemon1.name(), 'est KO.')
        print('Victoire de', self.pokemon2.name(), '!')

    def fight(self):
        while True:
            if self.pokemon2.hp() <= 0: # victoire pokemon1
                    self.win_pkmn1()
                    break
            elif self.pokemon1.hp() <= 0: # victoire pokemon2
                self.win_pkmn2()
                break
            # Joueur 1
            print('Que doit faire', self.pokemon1.name(), '?', 'attaquer', '/', 'fuir', self.pokemon1.hp(), 'PV')
            p1 = input()
            if p1 == 'attaquer':
                self.pokemon1.attaquer()
                self.pokemon2.set_hp(self.pokemon1.atk) # retirer les pv de pokemon2
                # Message de victoire et KO
                if self.pokemon2.hp() <= 0: # victoire pokemon1
                    self.win_pkmn1()
                    break
                elif self.pokemon1.hp() <= 0: # victoire pokemon2
                    self.win_pkmn2()
                    break
                # Joueur 2
                print('Que doit faire', self.pokemon2.name(), '?', 'attaquer', '/', 'fuir', self.pokemon2.hp(), 'PV')
                p2 = input()
                # Message de victoire et KO
                if self.pokemon2.hp() <= 0: # victoire pokemon1
                    self.win_pkmn1()
                    break
                elif self.pokemon1.hp() <= 0: # victoire pokemon2
                    self.win_pkmn2()
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

instance_combat = Combat()
instance_combat.fight()