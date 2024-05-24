class visualizaciones:
    __idm: str
    __idp: str
    __fyh: str
    __min: int
    
    def __init__(self, idm, idp, fyh, min):
        self.__idm=idm
        self.__idp=idp
        self.__fyh=fyh
        self.__min=min
        
        
    def __str__(self):
        return f"{self.__idm} {self.__idp} {self.__fyh} {self.__min} "
    
    def getidm(self):
        return self.__idm
    
    def getidp(self):
        return self.__idp
    
    def getfyh(self):
        return self.__fyh
    
    def getmin(self):
        return self.__min
    
    
