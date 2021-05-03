from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):

    @property
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass

    @property
    def cor(self):
        pass

    @cor.setter
    @abstractmethod
    def cor(self, valor):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass
    
    def getInformacaoes(self):
       print("Modelo:", self.modelo, " - Cor:", self.cor, " - Preço: R$", self.preco)
    
    @abstractmethod
    def cadastrar(self, modelo, cor, preco):
        pass