# Remporter des combats et collectionner un maximum de Pokémon.

# classe Pokemon avec des attributs:
# nom attribut privé
# points de vie (par défaut 100) attribut privé
# un niveau
# une puissance d'attaque et une défense (par défaut 0).
# La défense permet de se protéger des dégâts subis.

class Pokemon:
    def __init__(self, nom, level, atk, atk_name, defense):
        self.__nom = nom
        self.__pv = 100
        self.level = level
        self.atk = atk
        self.atk_name = atk_name
        self.defense = defense

    def name(self): # Getter nom
        return self.__nom

    def hp(self): # Getter pv
        return self.__pv
    
    def modif_hp(self, newhp): # Ajouter des PV selon le type
        self.__pv += newhp
    
    def set_hp(self, newhp): # Setter points de vie
        self.__pv -= newhp

    def attaquer(self):
       print(self.__nom, 'attaque', self.atk_name) # Attaquer

    def fuir(self):
        print(self.__nom, 'prend la fuite.') # Prendre la fuite