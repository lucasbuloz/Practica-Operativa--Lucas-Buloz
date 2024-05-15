import csv
from ClasCliente import Clientes

class gestorcliente:
    __listC= list
    
    def __init__(self):
        self.__listC=[]
        
    def inicializar (self):
        archivo= open("PRactica bien hecha/ClientesAbril2024.csv", "r")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            nuevocliente= Clientes(fila[0], fila[1], fila[2], fila[3], float(fila[4]))
            self.__listC.append(nuevocliente)
        archivo.close()
        
    def mostrar(self):
        for Clientes in self.__listC:
            print (Clientes)
            
    
            