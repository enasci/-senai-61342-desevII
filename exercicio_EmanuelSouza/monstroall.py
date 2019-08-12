from random import randint
class Monstros :

    def __init__(self, name, el_type, pow_attack, pow_def, hp, evo, level):
        self.name = name
        self.el_type = el_type
        self.pow_attack = pow_attack
        self.pow_def = pow_def
        self.hp = hp
        self.evo = evo
        self.level = level
        self.fstatus = 2 
        self.tposition = 1
        self.acthp = 0

    def attack(self):

        return self.pow_attack * self.evo * self.level * randint(1, 5)


    def deff(self):

        return self.pow_def * self.evo * self.level * randint(1, 3)


class Torneio :

    def duelo (tr1,tr2):
        
        tr1.acthp = tr1.hp
        tr2.acthp = tr2.hp
        tr1.fstatus = 1
        tr2.fstatus = 0
        count = 1
        while(tr1.acthp > 0 and tr2.acthp > 0):

            print("\nRound ",count ,tr1.name ,tr1.acthp," contra ",tr2.name ,tr2.acthp)
            count+=1
            if(tr1.fstatus == 1 and tr1.acthp > 0):
            
                print("\n ",tr1.name," ATACA ",tr2.name)
                tr2.acthp -= tr1.attack() - tr2.deff()
                tr1.fstatus = 0
                tr2.fstatus = 1

            if(tr2.fstatus == 1 and tr2.acthp > 0):
            
                print("\n ",tr2.name," ATACA ",tr1.name,)
                tr1.acthp -= tr2.attack() - tr1.deff()
                tr1.fstatus = 1
                tr2.fstatus = 0
        if (tr1.acthp > tr2.acthp):
            print("\n",tr1.name, "venceu ")
            tr1.tposition += 1
                
        else:
            print("\n",tr2.name, "venceu ")
            tr2.tposition += 1        
        


mon1 = Monstros("Wildwind", "vento", 10, 5 , 5000 , 2 , 5)

mon2 = Monstros("Splash", "agua", 10, 5 , 5000 , 2 , 5)

mon3 = Monstros("Igni", "fogo", 10, 5 , 5000 , 2 , 5)

mon4 = Monstros("Rock", "terra", 10, 5 , 5000 , 2 , 5)

Torneio.duelo(mon1,mon2)
Torneio.duelo(mon3,mon4)



if (mon1.tposition == 2):

    if (mon2.tposition == 2):
        Torneio.duelo(mon1,mon2)
    if (mon3.tposition == 2):
        Torneio.duelo(mon1,mon3)
    if (mon4.tposition == 2):
        Torneio.duelo(mon1,mon4)
                        
    
if (mon2.tposition == 2):
    
    if (mon1.tposition == 2):
        Torneio.duelo(mon1,mon2)
    if (mon3.tposition == 2):
        Torneio.duelo(mon2,mon3)
    if (mon4.tposition == 2):
        Torneio.duelo(mon2,mon4)


if (mon3.tposition == 2):
    
    if (mon2.tposition == 2):
        Torneio.duelo(mon3,mon2)
    if (mon1.tposition == 2):
        Torneio.duelo(mon1,mon3)
    if (mon4.tposition == 2):
        Torneio.duelo(mon3,mon4)


if (mon4.tposition == 2):
    
    if (mon2.tposition == 2):
        Torneio.duelo(mon4,mon2)
    if (mon3.tposition == 2):
        Torneio.duelo(mon4,mon3)
    if (mon1.tposition == 2):
        Torneio.duelo(mon1,mon4)

# 1 contra 1

