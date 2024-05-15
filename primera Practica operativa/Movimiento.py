class movimiento:
    _nrotar:str
    _fecha:str
    _desc:str
    _tmov:str
    _imp:float
    
    def __init__(self, nrotar, fecha,desc,tmov,imp):
        self._nrotar= nrotar
        self._fecha= fecha
        self._desc=desc
        self._tmov=tmov
        self._imp=imp
        
    def getnro(self):
        return self._nrotar
    def getfecha(self):
        return self._fecha
    def getdesc(self):
        return self._desc
    def gettmov(self):
        return self._tmov
    def getimp(self):
        return self._imp
    
    def __lt__(self,other):
        return self._nrotar < other._nrotar
    