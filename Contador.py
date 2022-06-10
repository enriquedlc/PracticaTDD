class Contador():

    def __init__(self, inicial = 0, incremento = 1, limite = None):
        self.__inicial = inicial
        self.__incremento = incremento
        self.__limite = limite
        pass

    def getInicial(self):
        return self.__inicial
    
    def getIncremento(self):
        return self.__incremento

    def getLimite(self):
        return self.__limite
    