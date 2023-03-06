from pokemon import Pokemon

class Terre(Pokemon):
    def __init__(self, nom, pv, level, atk, defense):
        super().__init__(nom, pv, level, atk, defense)

    def get(self):
        print(self.atk)

Taupiqueur = Terre('Taupiqueur', 90, 25, 'Séisme', 50)