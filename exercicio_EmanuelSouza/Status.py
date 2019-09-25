from random import randint

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