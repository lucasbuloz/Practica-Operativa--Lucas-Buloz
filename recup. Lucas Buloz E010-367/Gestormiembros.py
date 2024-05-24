from Classmiembros import miembros
import numpy as np
import csv

class gesmiembros: 
    __arreglo: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
    
    def __init__(self):
        self.__arreglo= np.empty([0], dtype= miembros)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
    
    def agregar(self, n):
            if self.__dimension == self.__cantidad:
                self.__dimension += self.__incremento
                self.__arreglo.resize(self.__dimension)
            self.__arreglo[self.__cantidad] = n
            self.__cantidad += 1
            
    def inicializar(self):
        archivo = open("Miembros.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nuevomiem = miembros((fila[0]), (fila[1]), (fila[2]))
            self.agregar(nuevomiem)
        archivo.close()
        
    def mostrar(self):
        for miembro in self.__arreglo:
            print(miembro)
                
    def buscarcorreo (self, correo):
            i=0
            b=False
            while not b and i< len(self.__arreglo):
                    if correo == self.__arreglo[i].getcorreo():
                            b= True
                            return self.__arreglo[i].getidm()
                    else:
                            i+=1
    
    