from pokemon import Pokemon

class Eau(Pokemon):
    def __init__(self, nom, pv, level, atk, defense):
        super().__init__(nom, pv, level, atk, defense)

    def get(self):
        print(self.atk)

Maraiste = Eau('Maraiste', 110, 25, 'Surf', 50)