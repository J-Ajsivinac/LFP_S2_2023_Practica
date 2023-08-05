def menuIncial():
    print()
    print(" ╔════════════════════════════════════════════════════════════════════════╗")
    print(" ║            Practica 1 - Lenguajes Formales y de Programación           ║")
    print(" ╠════════════════════════════════════════════════════════════════════════╣")
    print(" ║                                                                        ║")
    print(" ║                         Sistema de Inventario                          ║")
    print(" ║                     1. Cargar Inventario Inicial                       ║")
    print(" ║                     2. Cargar Instrucciones de movimientos             ║")
    print(" ║                     3. Crear Informe de Inventario                     ║")
    print(" ║                     4. Salir                                           ║")
    print(" ║                                                                        ║")
    print(
        " ╚════════════════════════════════════════════════════════════════════════╝\n"
    )
    print("Ingrese una opción: ", end="")


def menuOpciones(opcion):
    if opcion == "1":
        print("Opcion 1")
    elif opcion == "2":
        print("Opcion 2")
    elif opcion == "3":
        print("Opcion 3")
    elif opcion == "4":
        print("Gracias por utilizar el sistema")
    else:
        print("Opción no valida")


class Producto:
    def __init__(self, nombre, cantidad, p_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.p_unitario = p_unitario
        self.ubicacion = ubicacion


if __name__ == "__main__":
    while True:
        menuIncial()
        opcion = input()
        menuOpciones(opcion)
        if opcion == "4":
            break
