from pokemon import Pokemon

class Feu(Pokemon):
    def __init__(self, nom, level, atk, defense):
        super().__init__(nom, level, atk, defense)
        self.modif_hp(10)
        self.atk += 20
        self.defense += 10