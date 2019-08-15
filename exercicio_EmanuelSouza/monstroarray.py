from random import randint
count_monster = 0
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

class Status :      

    def combat (tr1,tr2):
        tr1.dmg.clear()
        tr2.dmg.clear()
        tr1.deffen.clear()
        tr2.deffen.clear()
        for n in range(0,10):
            tr1.dmg.append(tr1.pow_attack * tr1.evo * tr1.level * randint(1, 5))
            tr2.dmg.append(tr2.pow_attack * tr2.evo * tr2.level * randint(1, 5))
            tr1.deffen.append(tr1.pow_defense * tr1.evo * tr1.level * randint(1, 3))
            tr2.deffen.append(tr2.pow_defense * tr2.evo * tr2.level * randint(1, 3))

    def lvlup(tr1) :
        if tr1.element_type == 'fire' :
            tr1.level += 1
            tr1.pow_attack += 30
            tr1.hp  += 270
        if tr1.element_type == 'water' :
            tr1.level += 1
            tr1.pow_attack += 50
            tr1.hp  += 120
        if tr1.element_type == 'wind' :
            tr1.level += 1
            tr1.pow_attack += 40
            tr1.hp  += 230
        if tr1.element_type == 'earth' :
            tr1.level += 1
            tr1.pow_attack += 10
            tr1.hp  += 400        



class Torneio :
        
    def duelo (tr1,tr2):
        print("\nLEIA AQUI ", tr1.name ,tr1.hp," contra ",tr2.name ,tr2.hp)
        tr1.acthp = tr1.hp
        tr2.acthp = tr2.hp
        count = 0
        print("\nStatus inicial : ",tr1.name ,tr1.acthp," contra ",tr2.name ,tr2.acthp)
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
            if tr1 in Monstros.quartas :    
                if tr1 in Monstros.semif :
                    if tr1 not in Monstros.final :
                        print("\n",tr1.name ,' avançou para a final!')
                        Monstros.final.append(tr1)
                        Status.lvlup(tr1)        
            if tr1 in Monstros.quartas :                
                if tr1 not in Monstros.semif:  
                    print("\n",tr1.name, " avançou para a semifinal! ")           
                    Monstros.semif.append(tr1)
                    Status.lvlup(tr1)        
            if tr1 not in Monstros.quartas :
                print("\n",tr1.name, " avançou para as quartas de final! ")           
                Monstros.quartas.append(tr1)
                Status.lvlup(tr1)        
        else:
            if tr2 in Monstros.final:
                print("\n",tr2.name ,' Venceu o torneio!')
            if tr2 in Monstros.quartas :    
                if tr2 in Monstros.semif :
                    if tr2 not in Monstros.final :
                        print("\n",tr2.name ,' avançou para a final!')
                        Monstros.final.append(tr2)
                        Status.lvlup(tr2) 
            if tr2 in Monstros.quartas :                
                if tr2 not in Monstros.semif:  
                    print("\n",tr2.name, " avançou para a semifinal! ")           
                    Monstros.semif.append(tr2)
                    Status.lvlup(tr2) 
            if tr2 not in Monstros.quartas :
                print("\n",tr2.name, " avançou para as quartas de final! ")           
                Monstros.quartas.append(tr2)
                Status.lvlup(tr2) 
            
            
mon1 = Monstros( "Wildwind", "wind", 20, 5 , 3890 , 2 , 1 )
mon2 = Monstros( "Splash", "water", 18, 5 , 4890 , 2 , 1 )
mon3 = Monstros( "Igni", "fire", 15, 5 , 5890 , 2 , 1 )
mon4 = Monstros( "Rock", "earth", 10, 5 , 34890 , 2 , 1 )
mon5 = Monstros( "Bird", "wind", 20, 5 , 2890 , 2 , 1 )
mon6 = Monstros( "Garu", "water", 18, 5 , 3890 , 2 , 1 )
mon7 = Monstros( "Firin", "fire", 15, 5 , 4890 , 2 , 1 )
mon8 = Monstros( "Mountain", "earth", 10, 5 ,5890 , 2 , 1 )
mon9 = Monstros( "Rexar", "wind", 20, 5 , 7890 , 2 , 1 )
mon10 = Monstros( "Wrynn", "water", 18, 5 , 8890 , 2 , 1 )
mon11 = Monstros( "Aegwynn", "fire", 15, 5 , 7890 , 2 , 1 )
mon12 = Monstros( "Elune", "earth", 10, 5 , 6890 , 2 , 1 )
mon13 = Monstros( "Illidan", "wind", 20, 5 , 5890 , 2 , 1 )
mon14 = Monstros( "Malfurion", "water", 18, 5 , 4890 , 2 , 1 )
mon15 = Monstros( "Ragnaros", "fire", 15, 5 , 3890 , 2 , 1 )
mon16 = Monstros( "Azralon", "earth", 10, 5 , 4890 , 2 , 1 )
part = [ mon1, mon2, mon3, mon4, mon5, mon6, mon7, mon8, mon9, mon10, mon11, mon12, mon13, mon14, mon15, mon16 ]

Status.combat( part[0], part[1] )
Status.combat( part[2], part[3] )
Status.combat( part[4], part[5] )
Status.combat( part[6], part[7] )
Status.combat( part[8], part[9] )
Status.combat( part[10], part[11] )
Status.combat( part[12], part[13] )
Status.combat( part[14], part[15] )

Torneio.duelo( part[0], part[1] )
Torneio.duelo( part[2], part[3] )
Torneio.duelo( part[4], part[5] )
Torneio.duelo( part[6], part[7] )
Torneio.duelo( part[8], part[9] )
Torneio.duelo( part[10], part[11] )
Torneio.duelo( part[12], part[13] )
Torneio.duelo( part[14], part[15] )

Status.combat( Monstros.quartas[0], Monstros.quartas[1] )
Status.combat( Monstros.quartas[2], Monstros.quartas[3] )
Status.combat( Monstros.quartas[4], Monstros.quartas[5] )
Status.combat( Monstros.quartas[6], Monstros.quartas[7] )

Torneio.duelo( Monstros.quartas[0] ,Monstros.quartas[1] )
Torneio.duelo( Monstros.quartas[2] ,Monstros.quartas[3] )
Torneio.duelo( Monstros.quartas[4] ,Monstros.quartas[5] )
Torneio.duelo( Monstros.quartas[6] ,Monstros.quartas[7] )

Status.combat( Monstros.semif[0], Monstros.semif[1] )
Status.combat( Monstros.semif[2], Monstros.semif[3] )

Torneio.duelo( Monstros.semif[0] ,Monstros.semif[1] )
Torneio.duelo( Monstros.semif[2] ,Monstros.semif[3] )

Status.combat( Monstros.final[0], Monstros.final[1] )

Torneio.duelo( Monstros.final[0] ,Monstros.final[1] )


