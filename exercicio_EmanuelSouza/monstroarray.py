from random import randint
import json
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
            tr1.pow_defense += 10
            tr1.hp  += 270
        if tr1.element_type == 'water' :
            tr1.level += 1
            tr1.pow_attack += 50
            tr1.pow_defense += 7
            tr1.hp  += 120
        if tr1.element_type == 'wind' :
            tr1.level += 1
            tr1.pow_attack += 40
            tr1.pow_defense += 10
            tr1.hp  += 230
        if tr1.element_type == 'earth' :
            tr1.level += 1
            tr1.pow_attack += 10
            tr1.pow_defense += 20
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
            
json_input = '{ "monstros": [ { "name": "Wildwind","element_type": "wind","pow_attack": "20","pow_defense": "5","hp": "890","evo":"2","level": "1"},{"name": "Splash","element_type": "water","pow_attack": "18","pow_defense": "5","hp": "890","evo": "2","level": "1"},{ "name": "Igni","element_type": "fogo","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Rock","element_type": "terra","pow_attack": "7","pow_defense": "5","hp": "2890","evo": "2","level": "1"},{"name": "Bird","element_type": "water","pow_attack": "18","pow_defense": "5","hp": "2890","evo": "2","level": "1"},{ "name": "Garu","element_type": "fogo","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Firin","element_type": "terra","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Mountain","element_type": "water","pow_attack": "18","pow_defense": "5","hp": "890","evo": "2","level": "1"},{ "name": "Rexar","element_type": "fogo","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Wrynn","element_type": "terra","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Aegwynn","element_type": "water","pow_attack": "18","pow_defense": "5","hp": "890","evo": "2","level": "1"},{ "name": "Elune","element_type": "fogo","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Illidan","element_type": "terra","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Malfurion","element_type": "water","pow_attack": "18","pow_defense": "5","hp": "890","evo": "2","level": "1"},{ "name": "Ragnaros","element_type": "fogo","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"},{"name": "Azralon","element_type": "terra","pow_attack": "7","pow_defense": "5","hp": "890","evo": "2","level": "1"}]}'


json_decode = json.loads(json_input)

m_name=[]
m_element_type=[]
m_pow_attack=[]
m_pow_defense=[]
m_hp=[]
m_evo=[]
m_level=[]


for x in json_decode['monstros']:
        m_name.append(x['name'])
        m_element_type.append(x['element_type'])
        m_pow_attack.append(int(x['pow_attack']))
        m_pow_defense.append(int(x['pow_defense']))
        m_hp.append(int(x['hp']))
        m_evo.append(int(x['evo']))
        m_level.append(int(x['level']))
 
data_json=[m_name, m_element_type, m_pow_attack, m_pow_defense, m_hp, m_evo, m_level]

 
mon1 = Monstros(data_json[0][0], data_json[1][0], data_json[2][0], data_json[3][0] , data_json[4][0] , data_json[5][0] , data_json[6][0])
mon2 = Monstros(data_json[0][1], data_json[1][1], data_json[2][1], data_json[3][1] , data_json[4][1] , data_json[5][1] , data_json[6][1])
mon3 = Monstros(data_json[0][2], data_json[1][2], data_json[2][2], data_json[3][2] , data_json[4][2] , data_json[5][2] , data_json[6][2])
mon4 = Monstros(data_json[0][3], data_json[1][3], data_json[2][3], data_json[3][3] , data_json[4][3] , data_json[5][3] , data_json[6][3])            
mon5 = Monstros(data_json[0][4], data_json[1][4], data_json[2][4], data_json[3][4] , data_json[4][4] , data_json[5][4] , data_json[6][4])
mon6 = Monstros(data_json[0][5], data_json[1][5], data_json[2][5], data_json[3][5] , data_json[4][5] , data_json[5][5] , data_json[6][5])
mon7 = Monstros(data_json[0][6], data_json[1][6], data_json[2][6], data_json[3][6] , data_json[4][6] , data_json[5][6] , data_json[6][6])
mon8 = Monstros(data_json[0][7], data_json[1][7], data_json[2][7], data_json[3][7] , data_json[4][7] , data_json[5][7] , data_json[6][7])
mon9 = Monstros(data_json[0][8], data_json[1][8], data_json[2][8], data_json[3][8] , data_json[4][8] , data_json[5][8] , data_json[6][8])
mon10 = Monstros(data_json[0][9], data_json[1][9], data_json[2][9], data_json[3][9] , data_json[4][9] , data_json[5][9] , data_json[6][9])
mon11 = Monstros(data_json[0][10], data_json[1][10], data_json[2][10], data_json[3][10] , data_json[4][10] , data_json[5][10] , data_json[6][10])
mon12 = Monstros(data_json[0][11], data_json[1][11], data_json[2][11], data_json[3][11] , data_json[4][11] , data_json[5][11] , data_json[6][11])
mon13 = Monstros(data_json[0][12], data_json[1][12], data_json[2][12], data_json[3][12] , data_json[4][12] , data_json[5][12] , data_json[6][11])
mon14 = Monstros(data_json[0][13], data_json[1][13], data_json[2][13], data_json[3][13] , data_json[4][13] , data_json[5][13] , data_json[6][13])
mon15 = Monstros(data_json[0][14], data_json[1][14], data_json[2][14], data_json[3][14] , data_json[4][14] , data_json[5][14] , data_json[6][14])
mon16 = Monstros(data_json[0][15], data_json[1][15], data_json[2][15], data_json[3][15] , data_json[4][15] , data_json[5][15] , data_json[6][15])

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


