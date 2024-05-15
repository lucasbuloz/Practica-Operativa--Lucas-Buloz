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
        for clientes in self.__listC:
            print (clientes)

    def actualiza(self, dni, m):
        i=0
        b= False
        while not b and i< len(self.__listC):
            if dni == self.__listC[i].getdni():
                lista= self.__listC[i]
                b= True
            else: i += 1
        if b==True:
            s= m.ActualizaSaldo(lista.getsaldo(), lista.getnumtar())
            print(f"cliente: {lista.getap()} {lista.getnom()}, numero de tarjeta: {lista.getnumtar()}")
            print(f"saldo anterior: {lista.getsaldo()}")
            print("movimientos \n  fecha  descripcion  importe  tipo de movimiento")
            m.mostrar()
            lista.setSaldo(s)
            print(f"saldo actualizado: {lista.getsaldo()}")
        else: print("No se encontro")
