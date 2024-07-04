class cliente:
    __nom:str
    __apellido:str
    __dni:str
    __nrotar:str
    __saldoant:int
    
    def __init__(self,nombre,apellido,dni,nrotar,saldoant):
        self.__nom=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__nrotar=nrotar
        self.__saldoant=saldoant
        
    def getNombre(self):
        return self.__nom
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNrotar(self):
        return self.__nrotar
    def getSaldoAnterior(self):
        return self.__saldoant
    def setsaldo(self,saldo):
        self.__saldoant=saldo
    def __str__(self):
        return f"Nombre: {self.__nom}, Apellido: {self.__apellido}, DNI: {self.__dni}, NroTarj: {self.__nrotar}, SaldoAnterior: {self.__saldoant}"