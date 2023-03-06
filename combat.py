from pokemon import *
from eau import *
from feu import *
from normal import *
from terre import *

class Combat:
    def __init__(self):
        self.pokemon1 = Feu('Dracaufeu', 150, 40, 'Lance-Flammes', 60)
        self.pokemon2 = Eau('Maraiste', 110, 25, 'Surf', 50)

    def fight(self):
        while True:
            # Joueur 1
            print('Que doit faire le joueur 1 ?', 'attaquer', '/', 'fuir')
            p1 = input()
            if p1 == 'attaquer':
                self.pokemon1.attaquer()
                # Joueur 2
                print('Que doit faire le joueur 2 ?', 'attaquer', '/', 'fuir')
                p2 = input()
            elif p1 == 'fuir':
                self.pokemon1.fuir()
                break
            if p2 == 'attaquer':
                self.pokemon2.attaquer()
            elif p2 == 'fuir':
                self.pokemon2.fuir()
                break

test = Combat()
test.fight()