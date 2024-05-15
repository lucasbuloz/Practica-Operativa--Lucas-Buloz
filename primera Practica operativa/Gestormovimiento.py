from Movimiento import movimiento
import csv
import numpy as np

class gestormovimiento:
    _listaM: np.array
    
    def __init__(self):
        self._listaM=np.array([])

    def agregar_movimiento(self, movimiento):
        self.movimientos = np.append(self.movimientos, movimiento)

    def inicializar(self):
        archivo=open("MovimientosAbril2024.csv" "r")
        reader=csv.reader(archivo, delimiter=";")
        