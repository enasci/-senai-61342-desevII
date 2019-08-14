from random import randint
count_monster = 0
class Monstros :
    semif = []
    final = []
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

class Torneio :
        
    def stats (tr1,tr2):
        tr1.dmg.clear()
        tr2.dmg.clear()
        tr1.deffen.clear()
        tr2.deffen.clear()
        for n in range(0,10):
            tr1.dmg.append(tr1.pow_attack * tr1.evo * tr1.level * randint(1, 5))
            tr2.dmg.append(tr2.pow_attack * tr2.evo * tr2.level * randint(1, 5))
            tr1.deffen.append(tr1.pow_defense * tr1.evo * tr1.level * randint(1, 3))
            tr2.deffen.append(tr2.pow_defense * tr2.evo * tr2.level * randint(1, 3))                         

    def duelo (tr1,tr2):
        tr1.acthp = tr1.hp
        tr2.acthp = tr2.hp
        count = 0

        while(tr1.acthp > 0 and tr2.acthp > 0):
            if(tr1.acthp > 0):
                for n in range(0,10):
                    tr1.acthp-=tr2.dmg[n] - tr1.deffen[n]
                    tr2.acthp-=tr1.dmg[n] - tr2.deffen[n]
                   
                    
                    print("\nRound ",count ,tr1.name ,tr1.acthp," contra ",tr2.name ,tr2.acthp)
                    count+=1
                    if (tr1.acthp < 1 or tr2.acthp < 1 and tr2.acthp != tr1.acthp ) :    
                        break
              
        if (tr1.acthp > tr2.acthp):
            if tr1 in Monstros.final:
                print("\n",tr1.name ,' Venceu o torneio!')
            if tr1 in Monstros.semif :
                if tr1 not in Monstros.final :
                    print("\n",tr1.name ,' avançou para a final!')
                    Monstros.final.append(tr1)
            if tr2 not in Monstros.semif:  
                if tr2 not in Monstros.semif:  
                    print("\n",tr2.name, " avançou para a semifinal! ")           
                    Monstros.semif.append(tr2)   
        else:
            if tr2 in Monstros.final :
                print("\n",tr2.name ,' Venceu o torneio!')
            if tr2 in Monstros.semif :
                if tr2 not in Monstros.final:
                    print("\n",tr2.name ,' avançou para a final!')
                    Monstros.final.append(tr2)
            if tr2 not in Monstros.semif:   
                if tr2 not in Monstros.final:   
                    print("\n",tr2.name, " avançou para a semifinal! ")           
                    Monstros.semif.append(tr2)
            
            
mon1 = Monstros( "Wildwind", "vento", 10, 5 , 890 , 2 , 5 )
mon2 = Monstros( "Splash", "agua", 10, 5 , 890 , 2 , 5 )
mon3 = Monstros( "Igni", "fogo", 10, 5 , 890 , 2 , 5 )
mon4 = Monstros( "Rock", "terra", 10, 5 , 890 , 2 , 5 )
mon5 = Monstros( "Bird", "vento", 10, 5 , 890 , 2 , 5 )
mon6 = Monstros( "Garu", "agua", 10, 5 , 890 , 2 , 5 )
mon7 = Monstros( "Firin", "fogo", 10, 5 , 890 , 2 , 5 )
mon8 = Monstros( "Mountain", "terra", 10, 5 , 890 , 2 , 5 )
part = [ mon1, mon2, mon3, mon4, mon5, mon6, mon7, mon8 ]

Torneio.stats( part[0], part[1] )
Torneio.stats( part[2], part[3] )
Torneio.stats( part[4], part[5] )
Torneio.stats( part[6], part[7] )

Torneio.duelo( part[0], part[1] )
Torneio.duelo( part[2], part[3] )
Torneio.duelo( part[4], part[5] )
Torneio.duelo( part[6], part[7] )

Torneio.duelo( Monstros.semif[0] ,Monstros.semif[1] )
Torneio.duelo( Monstros.semif[2] ,Monstros.semif[3] )

Torneio.duelo( Monstros.final[0] ,Monstros.final[1] )


