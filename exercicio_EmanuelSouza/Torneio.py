from Monstros import Monstros
from Status import Status

class Torneio :
        
    def duelo (tr1,tr2):
        print("\n ", tr1.name ,tr1.hp," contra ",tr2.name ,tr2.hp)
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
