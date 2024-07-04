class movimiento:
    __nrotar:str
    __fecha:str
    __descripcion:str
    __tipodemov:str
    __importe:int
    
    def __init__(self,nrotar,fecha,descripcion,tipodemov,importe):
        self.__nrotar=nrotar
        self.__fecha=fecha
        self.__descripcion=descripcion
        self.__tipodemov=tipodemov
        self.__importe=importe
        
    def getNrotar(self):
        return self.__nrotar
    def getFecha(self):
        return self.__fecha
    def getDescripcion(self):
        return self.__descripcion
    def getTipoDeMovimiento(self):
        return self.__tipodemov
    def getImporte(self):
        return self.__importe
    def __str__(self):
        return f"NroTarj: {self.__nrotar}, Fecha: {self.__fecha}, Descripcion: {self.__descripcion}, TipoDeMovimiento: {self.__tipodemov}, Importe: {self.__importe}"
    
    def __lt__(self, other):
        return self.__nrotar < other.__nrotar