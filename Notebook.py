from Computador import Computador

class Notebook(Computador):

    def __init__(self, mdlComputador, corComputador, precoComputador, tempoBateriaComputador):
        self.modelo = mdlComputador
        self.cor = corComputador
        self.preco = precoComputador
        self.__tempoDeBateria = tempoBateriaComputador
    
    @property 
    def modelo(self):
        return self.modelo

    @modelo.setter
    def modelo(self, valor):
        self.modelo = valor

    @property 
    def cor(self):
        return self.cor

    @cor.setter
    def cor(self, valor):
        self.cor = valor

    @property 
    def preco(self):
        return self.preco

    @preco.setter
    def preco(self, valor):
        self.preco = valor

    def getTempoBateria(self):
        self.__tempoDeBateria

    def setTempoBateria(self, valor):
        self.__tempoDeBateria = valor

    def getInformacaoes(self):
        print("-Modelo:", self.modelo,
            "\n-Cor:", self.cor,
            "\n-Preço: R$", self.preco,
            "\n-Tempo de Bateria:",self.__tempoDeBateria)