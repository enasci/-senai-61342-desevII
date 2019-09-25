  
from abc import ABC, abstractmethod


class AbstractMassaFactory(ABC):

    @abstractmethod
    def criar_massa(self):
        pass

    def criar_ingred(self):
        pass



class Simples(AbstractMassaFactory):

    def criar_massa(self):
        return Espaguete()

    def criar_ingred(self):
        return Mol()


class Next(AbstractMassaFactory):

    def criar_massa(self):
        return Linguine()

    def criar_ingred(self):
        return Quei()  
    
class Pratin(AbstractMassaFactory):

    def criar_massa(self):
        return Linguine()

    def criar_ingred(self):
        return Sho()

class Skip(AbstractMassaFactory):

    def criar_massa(self):
        return Espaguete()

    def criar_ingred(self):
        return Bol()
      


class AbstractMassa(ABC):

    @abstractmethod
    def nome_massa(self):
        pass


class Linguine(AbstractMassa):
    def nome_massa(self):
        return "Linguine"


class Espaguete(AbstractMassa):
    def nome_massa(self):
        return "Espaguete"

class AbstractIngred(ABC):

    @abstractmethod
    def nome_ingred(self):
        pass


class Bol(AbstractIngred):
    def nome_ingred(self):
        return "Bolonhesa"


class Quei(AbstractIngred):
    def nome_ingred(self):
        return "Queijo"
		

class Sho(AbstractIngred):
    def nome_ingred(self):
        return "Shoyu"


class Mol(AbstractIngred):
    def nome_ingred(self):
        return "Molho de tomate"


def client_code(factory):
    product_a = factory.criar_massa()
    product_b = factory.criar_ingred()

    print(product_a.nome_massa())
    print(product_b.nome_ingred())


if __name__ == "__main__":
    print("Criando prato ")
    client_code(Simples())

    print("Criando segundo prato")
    client_code(Next())

    print("Criando terceiro prato")
    client_code(Pratin())    

    print("Criando quarto prato")
    client_code(Skip())    
    