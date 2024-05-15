from Clientes import clientes
from Gestormovimiento import gestormovimiento
import csv

class gestorclientes:
    _listaC:list
    
    def __init__(self):
        self._listaC=[]
        
    def inicializar(self):
        archivo=open("ClientesAbril2024.csv" "r")
        reader=csv.reader(archivo,delimiter=(";"))
        for fila in self._listaC:
            nuevocliente=clientes(fila[0], fila[1], fila[2],int(fila[3]), float(fila[5]))
            self._listaC.append(nuevocliente)
            
    def buscarcliente(self, dni):
        for cliente in self._listaC:
            if cliente.getdni() == dni:
                return cliente
        return -1        
            
            
    def menu():
        op=int (input("---Ingrese una opcion--- \n 1. Actualizar saldo \n 2. Informar movimientos \n 3.Ordenar \n"))
        while op in [1, 2, 3]:
            if op== 1:
                dni=input("Ingrese DNI: ")
                cliente= gestorclientes.buscarcliente(dni)
                if cliente!='-1': 
                    saldoactualizado =clientes.getsa(cliente)
                    for movimiento in gestormovimiento._listaM:
                        if movimiento.nrotar == cliente._nrotarj:
                            if movimiento.tmov == 'C':
                                saldoactualizado += movimiento.imp
                            elif movimiento.tmov == 'P':
                                saldoactualizado -= movimiento.imp
                    print(f"Cliente: {cliente.apellido} {cliente.nombre} - Número de tarjeta: {cliente.num_tarjeta}")
                    print(f"Saldo anterior: {cliente.sa:.2f}")
                    print("Movimientos:")
                    print("Fecha   Descripción              Importe  Tipo de movimiento")
                    for movimiento in gestormovimiento._listaM:
                            if movimiento.nrotar == cliente.nrotarj:
                                print(f"{movimiento.fecha}   {movimiento.desc:25} {movimiento.imp:.2f}    {movimiento.tmov}")
                                print(f"Saldo actualizado: {saldoactualizado:.2f}")
                    else: print("Cliente no encontrado.")
            if op == 2:
                nrotarjconsulta = input("Ingrese el número de tarjeta: ")
                csm= True
                for movimiento in gestormovimiento._listaM:
                    if movimiento.nrotar == nrotarjconsulta:
                        csm = False
                    break
                if csm:
                    print("No hubo movimientos para esta tarjeta en abril 2024.")
                else:
                    print("Hubo movimientos para esta tarjeta en abril 2024.")      
            if op == 3:
                gestormovimiento._listaM.sort()
                print("Movimientos ordenados por número de tarjeta:")
                for movimiento in gestormovimiento._listaM:
                    print(f"{movimiento.nrotar} - {movimiento.fecha} - {movimiento.desc} ({movimiento.tmov}): ${movimiento.imp:.2f}")
            op=int (input("---Ingrese una opcion--- \n 1. Actualizar saldo \n 2. Informar movimientos \n 3.Ordenar \n"))
