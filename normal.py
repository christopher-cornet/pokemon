from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, pv, level, atk, defense):
        super().__init__(nom, pv, level, atk, defense)

    def get(self):
        print(self.atk)

Miaouss = Normal('Miaouss', 70, 20, 'Combo-Griffe', 30)