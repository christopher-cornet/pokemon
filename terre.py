from pokemon import Pokemon

class Terre(Pokemon):
    def __init__(self, nom, level, atk, atk_name, defense):
        super().__init__(nom, level, atk, atk_name, defense)
        self.modif_hp(30)
        self.atk += 10
        self.defense += 20