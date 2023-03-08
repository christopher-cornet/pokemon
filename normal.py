from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, level, atk, defense):
        super().__init__(nom, level, atk, defense)
        self.modif_hp(10)
        self.atk += 10
        self.defense += 10