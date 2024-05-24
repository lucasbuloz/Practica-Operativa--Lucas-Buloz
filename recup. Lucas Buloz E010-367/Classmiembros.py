class miembros:
    __idm :str
    __ayn: str
    __correo: str
    
    def __init__(self, idm, ayn, correo):
        self.__idm= idm
        self.__ayn=ayn
        self.__correo=correo
        
    def __str__(self):
        return f"{self.__idm} {self.__ayn} {self.__correo}"
    
    def getidm(self):
        return self.__idm
    
    def getayn(self):
        return self.__ayn
    
    def getcorreo(self):
        return self.__correo