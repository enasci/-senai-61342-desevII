class Placar:
    def __init__(self):
        self.__instance = None
        self.placar = dict()
    def print_placar(self):

        for key, value in self.placar.items():

            print("nome: "+ (key))
            for key2, value2 in value.items():

                print("tipo "+str(key2) +" com quantidade "+str(value2))

    def adicionar_placar(self, nome, qtd, tipo):


            if nome in self.placar.keys():
                pontuacao = self.placar[nome]

                if tipo in pontuacao.keys():
                    placar[nome][tipo] += qtd
                else:
                    self.placar[nome][tipo] = qtd
            else:
                self.placar.update({nome:{tipo : qtd}})

    @staticmethod
    def instance():
        if not Placar.__instance:
            Placar.__instance = Placar()
        return Placar.__instance




pontuando = Placar.instance()
pontuando2 = Placar.instance()

pontuando.adicionar_placar("emanuel",10,"estrela")
pontuando.adicionar_placar("venha",8,"up")
pontuando2.adicionar_placar("uhul",5,"estrela")
pontuando2.adicionar_placar("legal",14,"dislike")

pontuando.print_placar()
print("aaaaaaaaa")
pontuando2.print_placar()

