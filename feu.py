from pokemon import Pokemon

class Feu(Pokemon):
    def __init__(self, __nom, pv, level, atk, defense):
        super().__init__(__nom, pv, level, atk, defense)

    def get(self):
        return self.__nom, self.__pv, self.level, self.atk, self.defense

Dracaufeu = Feu('Dracaufeu', 150, 40, 'Lance-Flammes', 60)