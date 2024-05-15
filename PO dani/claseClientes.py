class Clientes:
    __nombre: str
    __apellido: str
    __dni: str
    __numtar: str
    __saldo: float
    
    def __init__(self, nombre, apellido, dni, numtar, saldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numtar = numtar
        self.__saldo = saldo
        
    def __str__(self):
      return f"{self.__apellido} {self.__nombre} {self.__dni} {self.__numtar} {self.__saldo}"
        
        
    def getnom (self):
        return self.__nombre
    
    def getap (self):
        return self.__apellido
    
    def getdni(self):
        return self.__dni
    
    def getnumtar(self):
        return self.__numtar
    
    def getsaldo(self):
        return self.__saldo
    
    def setSaldo(self, s):
        self.__saldo = s