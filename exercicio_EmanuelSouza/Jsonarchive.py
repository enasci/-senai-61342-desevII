import json

class Jsonarchive :
    
    def write_json(lista):
        with open('champions.json', 'w') as f:
            return json.dump(lista, f)

    def read_json(arquivo):
        with open(arquivo, 'r') as file:
            result = file.read()
            return str(result)