from classmov import movimiento
import numpy as np
import csv

class gestormov:
    __arreglomov= np.ndarray
    __dimension=0
    __cantidad=0
    __incremento= 1

    def __init__(self):
        self.__arreglomov=np.empty([0], dtype=movimiento)

    def agregar(self, movi):
        if self.__dimension== self.__cantidad:
            self.__dimension+=self.__incremento
            self.__arreglomov.resize(self.__dimension)
        self.__arreglomov[self.__cantidad]=movi
        self.__cantidad+=1

    def inicializar(self):
        archivo=open("C:/Users/Buloz/Documents/Lucas/Facultad/LCC/POO/Unidad 2/Codigos U2/parcialtarjeta/MovimientosAbril2024.csv", "r")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            nmov= movimiento (fila[0], fila[1],fila[2],fila[3],int (fila[4]) )
            self.agregar(nmov)
        archivo.close()

    def mostrar(self):
        for movi in self.__arreglomov:
            print(movi)

    def actualizarsaldo(self, nt):
        saldo=0
        for movi in self.__arreglomov:
            if movi.getNrotar()== nt.getNrotar():
                if movi.getTipoDeMovimiento()=="P":
                    saldo-=movi.getImporte()
                elif movi.getTipoDeMovimiento()=="C":
                    saldo+=movi.getImporte()    
        return saldo
    
    def mostrarMovimientos(self, nt):
        for movimiento in self.__arreglomov:
            if movimiento.getNrotar()==nt.getNrotar():
                print(f"{movimiento.getFecha()} {movimiento.getDescripcion()} {movimiento.getTipoDeMovimiento()} {movimiento.getImporte()}")


    def buscarMov(self, nt):
        b= False
        i=0
        while not b and i< len(self.__arreglomov):
                if self.__arreglomov[i].getNrotar()==nt.getNrotar():
                    b= True
                else: i+=1
        return b            
    
    def ordenar(self):
        self.__arreglomov.sort()