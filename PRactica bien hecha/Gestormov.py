import csv
from ClasMov import Movimientos
import numpy as np

class gestormov:
    __arregloMov: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int
    
    def __init__ (self):
        self.__arreglo =np.empty([0], dtype=Movimientos)
        self.__cantidad= 0
        self.__dimension=0
        self.__incremento=1

    def agregar(self, m):
        if self.__dimension == self.__cantidad:
            self.__dimension+=self.__incremento
            self.__arregloMov.resize(self.__dimension)
        self.__arregloMov[self.__cantidad]= m
        self.__cantidad += 1

    def inicializar (self):
        archivo = open("MovimientosAbril2024.csv", "r")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            nuevomov = Movimientos((fila[0]), (fila[1]), (fila[2]), fila[3],float(fila[4]))
            self.agregar(nuevomov)
        archivo.close()

    def mostrar(self):
        for mov in len(self.__arregloMov):
            print(mov)
    