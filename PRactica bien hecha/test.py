from Gestocliente import gestorcliente
from Gestormov import gestormov

def test():
    m=gestormov()
    c=gestorcliente()

    while True:
        print("---Menu de opciones---")
        print("1, carga")
        print("2, punto a")
        print("3, punto b")
        
        op = input("ingrese op: ")
        
        if op=="1":
            m.inicializar()
            c.inicializar()
            m.mostrar()
            c.mostrar()

        elif op == "2":
            dni=input("Ingrese dni: ")
