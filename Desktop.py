from Computador import Computador

class Desktop(Computador):

    def __init__(self, mdlComputador, corComputador, precoComputador, potenciaFonteComputador):
        self.modelo = mdlComputador
        self.cor = corComputador
        self.preco = precoComputador
        self._potenciaDaFonte = potenciaFonteComputador
    
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

    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte

    def setPotenciaDaFonte(self, valor):
        self._potenciaDaFonte = valor

    def getInformacoes(self):
        print("-Modelo:", self.modelo,
            "\n-Cor:", self.cor,
            "\n-Preço: R$", self.preco,
            "\n-Potência da Fonte:",self._potenciaDaFonte)