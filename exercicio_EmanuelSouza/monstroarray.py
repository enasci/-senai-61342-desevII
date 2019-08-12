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
        self.dmg = []
        self.deffen = []
    


class Torneio :
  
      
    def attq (tr1,tr2):
        tr1.dmg.clear()
        tr2.dmg.clear()
        for n in range(0,10):
            tr1.dmg.append(tr1.pow_attack * tr1.evo * tr1.level * randint(1, 5))
            tr2.dmg.append(tr2.pow_attack * tr2.evo * tr2.level * randint(1, 5))
    
    def deffen (tr1,tr2):
        tr1.deffen.clear()
        tr2.deffen.clear()
        for n in range(0,10):
            tr1.deffen.append(tr1.pow_def * tr1.evo * tr1.level * randint(1, 3))
            tr2.deffen.append(tr2.pow_def * tr2.evo * tr2.level * randint(1, 3))
                           

    def duelo (tr1,tr2):
        tr1.acthp=tr1.hp
        tr2.acthp=tr2.hp
        print(tr1.name," Hp inicial",tr1.acthp, tr2.name, "Hp inicial ",tr2.acthp)    
        for n in range(0,10):
            tr1.acthp-=tr2.dmg[n] - tr1.deffen[n]
            tr2.acthp-=tr1.dmg[n] - tr2.deffen[n]
        
        print(tr1.name," Hp ",tr1.acthp, tr2.name, "Hp ",tr2.acthp)    
        if tr1.acthp>tr2.acthp:
            print(tr1.name," Venceu!!")
            tr1.tposition = 2
        if tr2.acthp>tr1.acthp:
            print(tr2.name," Venceu!!")
            tr2.tposition = 2
                
               
                


mon1 = Monstros("Wildwind", "vento", 10, 5 , 5000 , 2 , 5)

mon2 = Monstros("Splash", "agua", 10, 5 , 5000 , 2 , 5)

mon3 = Monstros("Igni", "fogo", 10, 5 , 5000 , 2 , 5)

mon4 = Monstros("Rock", "terra", 10, 5 , 5000 , 2 , 5)



Torneio.attq(mon1,mon2)
Torneio.deffen(mon1,mon2)
Torneio.duelo(mon1,mon2)
Torneio.attq(mon3,mon4)
Torneio.deffen(mon3,mon4)
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

