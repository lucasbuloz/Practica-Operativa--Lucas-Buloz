from classcliente import cliente
import csv

class gestorCli:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
        
    def inicializar(self):
        archivo=open("C:/Users/Buloz/Documents/Lucas/Facultad/LCC/POO/Unidad 2/Codigos U2/parcialtarjeta/ClientesAbril2024.csv","r")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            ncli= cliente(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
            self.__lista.append(ncli)
            
    def mostrar(self):
        for cli in self.__lista:
            print(cli)

    def buscardni(self,dni):
        b=False
        i=0
        while b==False and i<len(self.__lista):
            if self.__lista[i].getDni()==dni:
                b=True
                return self.__lista[i]
            i+=1
        if  b==False:
            print("No existe cliente con ese DNI")

    def buscarTarjeta(self, numtar):
        b= False
        i=0
        while b==False and i< len(self.__lista):
            if self.__lista[i].getNrotar()==numtar:
                b= True
                return self.__lista[i]
            i+=1
        if b == False:
            return
        
    def listado(self, gm):
        dni = input("Ingrese el DNI del cliente: ")
        nt = self.buscardni(dni)
        if nt is not None: 
            print(f"nombre: {nt.getNombre()} apellido: {nt.getApellido()} numero de tarjeta: {nt.getNrotar()}")
            print(f"saldo: {nt.getSaldoAnterior()}")
            print("movimientos \n  fecha  descripcion  tipo de movimiento  importe  ")
            gm.mostrarMovimientos(nt)
            saldo = gm.actualizarsaldo(nt)
            nt.setsaldo(saldo)
            print(f"Saldo actualizado: {nt.getSaldoAnterior()}")
        else:
            print("No existe cliente con ese DNI")


    def buscarCliente(self, gm):
        t = input("ingrese numero de tarjeta: ")
        numtar = self.buscarTarjeta(t)
        nt = gm.buscarMov(numtar)
        if nt is False:
            print(f" no hay movimientos, apellido: {numtar.getApellido()} nombre: {numtar.getNombre()}")
        else:
            print("si hubieron movimientos")


   