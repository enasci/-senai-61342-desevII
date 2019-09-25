import json
from Jsonarchive import Jsonarchive

class Decode:

    count_monster = 0

    def decode(archive_name):
        
        m_name=[]
        m_element_type=[]
        m_pow_attack=[]
        m_pow_defense=[]
        m_hp=[]
        m_evo=[]
        m_level=[]

        json_decode = json.loads(Jsonarchive.read_json(archive_name))

        for x in json_decode['monstros']:
                m_name.append(x['name'])
                m_element_type.append(x['element_type'])
                m_pow_attack.append(int(x['pow_attack']))
                m_pow_defense.append(int(x['pow_defense']))
                m_hp.append(int(x['hp']))
                m_evo.append(int(x['evo']))
                m_level.append(int(x['level']))
                Decode.count_monster += 1
              
        
        data_json = [m_name, m_element_type, m_pow_attack, m_pow_defense, m_hp, m_evo, m_level]
        return data_json
