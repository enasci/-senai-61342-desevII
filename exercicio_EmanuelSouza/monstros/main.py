from random import randint
from Monstros import Monstros
from Status import Status
from Torneio import Torneio
from Fight import Fight
from Jsonarchive import Jsonarchive
import Decode

import json
        
data_json = Decode.Decode.decode("champions.json")

part = []

for n in range(0,Decode.Decode.count_monster):
           
    monster = Monstros(data_json[0][n], data_json[1][n], data_json[2][n], data_json[3][n] , data_json[4][n] , data_json[5][n] , data_json[6][n])
    part.append(monster)

Fight.fight(part)

Fight.fight(Monstros.quartas)

Fight.fight(Monstros.semif)

Fight.fight(Monstros.final)



