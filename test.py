


from httplib2 import RETRIES


def menu():
    print("""*** CAJERO ***
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
--------
Opción (1-4)? """)
    
def leer_opcion():
    op = input()
    while not op.isdigit() or int(op) <  1 or int(op) > 4:
        print("Error. Opción inválida. Digite un número de 0 a 3.")
        input("Presione cualquier tecla para continuar")
        print("\n\n")
        menu()
        op = input()
    return int(op)

def depositar_dinero(saldo):
    try:
        monto = int(input("Ingresar saldo a cargar: "))
        if monto > 0:
            saldo += monto
            print("Monto válido, su saldo es", saldo)
        else:
            print("Error. Monto inválido")
    except ValueError:
        print("Error. No es un monto válido")
    return saldo

def retirar_dinero(saldo):
    try:
        retiro = int(input("Ingresar valor del retiro: "))
        if retiro > 0 and retiro <= saldo:
            saldo -= retiro
            print("Su retiro se realizó con éxito. Saldo restante:", saldo)
        elif retiro > saldo:
            print("Fondos insuficientes")
        else:
            print("Monto inválido")
    except ValueError:
        print("Error. Pago inválido")
    return saldo



    
def main():
    opcion = 0
    saldo = 1000

    while opcion != 4:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            print("Su saldo es", saldo)
        elif opcion == 2:
            saldo = depositar_dinero(saldo)
        elif opcion == 3:
            saldo = retirar_dinero(saldo)
        elif opcion == 4:
            print("\nGracias por usar el software. ADIOS.")


        input("Presione cualquier tecla para continuar....")
        print("\n\n")


main()

