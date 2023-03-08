from pokemon import Pokemon

class Eau(Pokemon):
    def __init__(self, nom, level, atk, atk_name, defense):
        super().__init__(nom, level, atk, atk_name, defense)
        self.modif_hp(15)
        self.atk += 20
        self.defense += 10