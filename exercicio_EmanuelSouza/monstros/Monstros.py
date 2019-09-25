class Monstros :
    semif = []
    final = []
    quartas = []
    def __init__(self, name, el_type, pow_attack, pow_def, hp, evo, level):
        self.name = name
        self.element_type = el_type
        self.pow_attack = pow_attack
        self.pow_defense = pow_def
        self.hp = hp
        self.evo = evo
        self.level = level
        self.fstatus = 2 
        self.tposition = 1
        self.acthp = 0
        self.dmg = []
        self.deffen = []
        self.count = 0 