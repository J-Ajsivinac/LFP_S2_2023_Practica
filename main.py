from tkinter import filedialog


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


def menuOpciones(opcion, inventario):
    if opcion == "1":
        url_temporal, validacion = pedir_archivos(
            "Seleccione el archivo de inicio", "Archivo de inicio", "*.inv"
        )
        if validacion:
            leer_inicio(inventario, url_temporal)
        else:
            print("Selecciones un archivo")
    elif opcion == "2":
        url_temporal, validacion = pedir_archivos(
            "Seleccione el archivo de movimientos", "Archivo de movimientos", "*.mov"
        )
        if validacion:
            leer_movimientos(inventario, url_temporal)
        else:
            print("Selecciones un archivo")
    elif opcion == "3":
        inventario.crear_informe()
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


class ControlInventario:
    def __init__(self):
        self.productos = []

    def buscar_producto(self, nombre, ubicacion):
        for producto in self.productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                return producto
        return None

    def crear_producto(self, nombre, cantidad, p_unitario, ubicacion):
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor a 0")
            return
        if p_unitario < 0:
            print("Error: El precio unitario debe ser mayor a 0")
            return
        self.productos.append(Producto(nombre, cantidad, p_unitario, ubicacion))
        self.crear_informe()

    def agregar_stock(self, nombre, cantidad, ubicacion):
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor a 0")
            return
        producto = self.buscar_producto(nombre, ubicacion)
        if producto:
            producto.cantidad += cantidad
        else:
            print(
                f"Error en agregar: El producto: {nombre} no existe en la ubicación: {ubicacion}"
            )

        # self.crear_informe()

    def vender_producto(self, nombre, cantidad, ubicacion):
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor a 0")
            return
        producto = self.buscar_producto(nombre, ubicacion)
        if producto:
            if producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
            else:
                print(
                    f"Error: No hay suficientes existencias de: {nombre} en {ubicacion}"
                )
        else:
            print(
                f"Error en agregar: El producto {nombre} no existe en la ubicación {ubicacion}"
            )

        # self.crear_informe()

    def crear_informe(self):
        if len(self.productos) == 0:
            print("Primero agregue el archivo .inv")
            return

        with open("informe.txt", "w", encoding="UTF-8") as archivo:
            archivo.write(
                "╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n"
            )
            archivo.write(
                "║                                                INFORME DE INVENTARIO                                             ║\n"
            )
            # archivo.write("Producto\tCantidad\tPrecio Unitario\tUbicacion\n")
            archivo.write(
                "╠════════════════════════════════╦════════════════╦═════════════════════╦═════════════════╦════════════════════════╣\n"
            )
            archivo.write(
                "║       NOMBRE DEL PRODUCTO      ║    CANTIDAD    ║   PRECIO UNITARIO   ║   VALOR TOTAL   ║        UBICACIÓN       ║\n"
            )
            archivo.write(
                "╠════════════════════════════════╬════════════════╬═════════════════════╬═════════════════╬════════════════════════╣\n"
            )
            for dato in self.productos:
                archivo.write("║")
                archivo.write(" %-31s" % dato.nombre)
                archivo.write("║")
                archivo.write(" %-15s" % dato.cantidad)
                archivo.write("║")
                archivo.write(" %-20s" % dato.p_unitario)
                archivo.write("║")
                archivo.write(" %-16s" % (dato.cantidad * dato.p_unitario))
                archivo.write("║")
                archivo.write(" %-23s" % dato.ubicacion)
                archivo.write("║\n")
            archivo.write(
                "╚════════════════════════════════╩════════════════╩═════════════════════╩═════════════════╩════════════════════════╝"
            )
            archivo.write("\n")


def pedir_archivos(titulo, mensaje, extension):
    archivo = filedialog.askopenfilename(title=titulo, filetypes=[(mensaje, extension)])
    return (archivo, archivo != "")


def leer_inicio(inventario, url_archivo):
    with open(url_archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea.split(" ")[0] != "crear_producto":
                print("Error de comando")
                break
            texto_datos = linea.split(" ")[1]
            inventario.crear_producto(
                texto_datos.split(";")[0],
                int(texto_datos.split(";")[1]),
                float(texto_datos.split(";")[2]),
                texto_datos.split(";")[3].strip(),
            )


def leer_movimientos(inventario, url_archivo):
    if len(inventario.productos) == 0:
        print("Primero agregue el archivo .inv")
        return

    with open(url_archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea == "" or linea == "\n":
                continue
            texto_datos = linea.split(" ")[1]
            if linea.split(" ")[0] == "agregar_stock":
                inventario.agregar_stock(
                    texto_datos.split(";")[0],
                    int(texto_datos.split(";")[1]),
                    texto_datos.split(";")[2].strip(),
                )
            elif linea.split(" ")[0] == "vender_producto":
                inventario.vender_producto(
                    texto_datos.split(";")[0],
                    int(texto_datos.split(";")[1]),
                    texto_datos.split(";")[2].strip(),
                )


if __name__ == "__main__":
    inventario = ControlInventario()
    while True:
        menuIncial()
        opcion = input()
        menuOpciones(opcion, inventario)
        if opcion == "4":
            break
