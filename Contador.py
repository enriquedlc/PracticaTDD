class Contador():

    def __init__(self, inicial= 0, incremento = 1, limite = None, valorActualContador = 0):
        self.__inicial = inicial
        self.__incremento = incremento
        self.__limite = limite
        self.__valorActualContador = valorActualContador

    def getInicial(self):
        return self.__inicial
    
    def getIncremento(self):
        return self.__incremento

    def getLimite(self):
        return self.__limite

    def getValorActualContador(self):
         return self.__valorActualContador

    def incrementarValorInicial(self):
        self.__valorActualContador = self.__valorActualContador + self.__incremento
        print(self.__valorActualContador)
        if self.__valorActualContador > self.__limite:
            print("Se supero el limite del contador")
    