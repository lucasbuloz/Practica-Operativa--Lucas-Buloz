from gestorAlquiler import gesAlquiler
from gestorCancha import gesCanchas

def test():
    c = gesCanchas()
    a = gesAlquiler()
    
    while True:
        print("1, carga")
        print("2, listado")
        print("3, total minutos")
        
        
        op = input("ingrese opcion ")
        
        if op == "1":
            c.inicializar()
            a.inicializar()
            c.mostrar()
            a.mostar()
            
        elif op == "2":
            a.ordenar()
            a.listado(c)
            
        elif op == "3":
            c.buscar(a)