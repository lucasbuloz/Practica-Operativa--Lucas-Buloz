from Classvisualizaciones import visualizaciones
import csv

class gesvisualizaciones:
    __lista: list
    
    def __init__ (self):
        self.__lista = []
        
        
    def inicializar(self):
        archivo = open("Visualizaciones.csv", "r")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            nuevavis = visualizaciones((fila[0]), (fila[1]), (fila[2]), int(fila[3]))
            self.__lista.append(nuevavis)
        archivo.close()
        
    def mostar(self):
        for visualizacion in self.__lista:
            print(visualizacion)
            
    def buscar(self, m):
        correo = input("ingrese correo: ")
        id = m.buscarcorreo(correo)
        tm = 0
        for p in self.__lista:
            if id == p.getidm():
                tm += p.getmin()
        print(f"El tiempo que vio peliculas es:{tm}")
        