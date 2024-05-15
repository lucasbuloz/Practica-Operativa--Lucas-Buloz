class clientes:
    _nom:str
    _ape:str
    _dni:str
    _nrotarj:int
    _sa:float
    
    def __init__(self, nom, ape, dni, nrotarj, sa):
        self._nom=nom
        self._ape=ape
        self._dni=dni
        self._nrotarj=nrotarj
        self._sa= sa

    def getnom(self):
        return self._nom
    def getape(self):
        return self._ape
    def getdni(self):
        return self._dni
    def getnrotarj (self):
        return self._nrotarj
    def getsa(self):
        return self._sa
    
   
        
    