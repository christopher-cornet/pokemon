# Remporter des combats et collectionner un maximum de Pokémon.

# classe Pokemon avec des attributs:
# nom attribut privé
# points de vie (par défaut 100) attribut privé
# un niveau
# une puissance d'attaque et une défense (par défaut 0).
# La défense permet de se protéger des dégâts subis.

class Pokemon:
    def __init__(self, nom, pv, level, atk, defense):
        self.__nom = nom
        self.__pv = pv
        self.level = level
        self.atk = atk
        self.defense = defense

    def get(self):
        return self.__nom, self.__pv, self.level, self.atk, self.defense

    def attaquer(self):
       print(self.__nom, 'attaque', self.atk)

    def fuir(self):
        print(self.__nom, 'prend la fuite.')

# il existe 18 types de Pokémon.

# Chaque Pokémon possède au minimum un type qui conditionne les caractéristiques du
# Pokémon, le nombre de points de vie, la puissance d'attaque, sa défense...

# ------------------------------

# Un système de combat entre deux Pokémon doit être développé.

# Lors des combats, la vie des Pokémon est vérifiée. Si la vie d'un Pokémon est à zéro,
# un message est affiché en console avec le nom du Pokémon gagnant.

# il peut arriver qu'un Pokémon loupe son attaque.

# Le Pokédex est un outil indispensable. Il sert à enregistrer les informations des Pokémon
# combattus. (nom, type, défense, puissance d'attaque et point de vie).
# Les Pokémon seront sauvegardés dans un fichier nommé pokédex.json, une
# vérification doit être effectuée afin d'éviter les doublons. Cet outil permet d'afficher
# l'ensemble des Pokémon rencontrés ainsi que leur nombre.

# En prenant en compte les informations ci-dessus, écrire la classe "Pokemon", dont
# certains de ses attributs doivent être privés (nom et point de vie).

# ------------------------------

# Créer au minimum quatre types de Pokémon : Normal, Feu, Eau et Terre.
# Les classes concernant les types héritent de la classe “Pokemon”. Chacune de ces
# catégories modifient le nombre de points de vie, la puissance d'attaque et la défense.
# Une méthode doit être implémentée permettant d'afficher en console les informations
# générales du Pokémon (nom, vies, défense, attaque).

# Ajouter une classe “Combat”. Cette classe permet la gestion complète du jeu.
# Cette classe doit avoir au minimum :
# ● Une méthode qui vérifie si l’un des deux Pokémon n’est plus en vie.
# ● Une méthode qui renvoie le nom du vainqueur.
# ● Une méthode qui choisit aléatoirement 1 ou 0. Si 1 est retourné, alors le
# Pokémon peut attaquer et infliger des dégâts à son adversaire, sinon il loupe son
# attaque.
# ● Une méthode qui récupère le type de l'adversaire et récupère sa puissance
# d’attaque et le multiplie en suivant le tableau (dans le sujet)

# Une méthode qui enlève des points de vie en fonction de la défense
# ● Une méthode qui renvoie de nom du Pokémon perdant
# ● Une méthode qui enregistre le Pokémon rencontré dans votre Pokédex

# Un menu en début de partie est proposé au joueur permettant les actions suivantes :
# ● Lancer une partie
# ● Ajouter un Pokémon (dans un fichier texte nommé “pokemon.json”)
# ● Accéder à son Pokedex.

# Lors du démarrage de la partie, le joueur doit renseigner avec quel
# Pokémon il veut jouer, selon la liste des Pokémon. L’adversaire est
# # quant à lui choisi de façon aléatoire dans le fichier “pokemon.json”.

# Faites combattre deux Pokémon.
# Chaque classe doit être dans un fichier séparé.