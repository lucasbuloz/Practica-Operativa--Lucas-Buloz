from Gestormiembros import gesmiembros
from Gestorvisualizaciones import gesvisualizaciones

def test():
    m = gesmiembros()
    v = gesvisualizaciones()
    
    while True:
        print("1, carga")
        print("2, minutos vistos")
        
        op = input("ingrese opcion ")
        
        if op == "1":
            v.inicializar()
            v.mostrar()
            m.inicializar()
            m.mostar()
            
        elif op == "2":
            v.buscar(m)
            