from gestorcli import gestorCli
from gestormov import gestormov

def test():
    cli=gestorCli()
    mov=gestormov()
    b=True


    while b==True:
        print("1. Cargar datos y mostrar")
        print("2. Actualizar saldo")
        print("3. Moviemientos en 2024")
        print("4. Salir")

        opcion=int(input("Elija una opcion: "))

        if opcion==1:
            cli.inicializar()
            cli.mostrar()
            mov.inicializar()
            mov.ordenar()
            mov.mostrar()
            print("Datos cargados")
        elif opcion==2:
            cli.listado(mov)
        elif opcion==3:
            cli.buscarCliente(mov)
        elif opcion==4:
            b=False
        