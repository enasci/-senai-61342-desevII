from Status import Status
from Torneio import Torneio
from random import randint

class Fight:
    def fight(duel_array) :
        count_monsters = len(duel_array)
        if (count_monsters%2 != 0):
            count_monsters -= 1

        random = []
    
        count_range = int(count_monsters/2)

        for ind in range(0,count_range):
            random_num = count_monsters - 1
            control_loop = 0
            while (control_loop == 0):
        
                x = randint(0, random_num)
                if x not in random:
                    random.append(x)
                    control_loop = 1
            

            control_loopi = 0
            while (control_loopi == 0):
                y = randint(0, random_num)
                if y not in random: 
                    random.append(y)
                    control_loopi = 1
          
            Status.combat( duel_array[x] ,duel_array[y] )
            Torneio.duelo( duel_array[x] ,duel_array[y] )
