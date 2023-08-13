from tkinter import filedialog


def menuIncial():
    print()
    print(" ╔════════════════════════════════════════════════════════════════════════╗")
    print(" ║            Practica 1 - Lenguajes Formales y de Programación           ║")
    print(" ╠════════════════════════════════════════════════════════════════════════╣")
    print(" ║                                                                        ║")
    print(
        " ║                        \033[34mSistema de Inventario\033[0m                           ║"
    )
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
    # Cargar inventario incial
    if opcion == "1":
        url_temporal = ""
        validacion = False
        url_temporal, validacion = pedir_archivos(
            "Seleccione el archivo de inicio", "Archivo de inicio", "*.inv"
        )
        if validacion:
            alertas("Archivo cargado", "verde")
            leer_inicio(inventario, url_temporal)
            inventario.crear_informe()
            alertas("Informe actualizado", "verde")
        else:
            alertas("Seleccione el archivo de inicio", "rojo")
            menuOpciones("1", inventario)
    # Cargar instrucciones de movimientos
    elif opcion == "2":
        if len(inventario.productos) == 0:
            alertas("Primero agregue el archivo .inv", "rojo")
            return
        url_temporal, validacion = pedir_archivos(
            "Seleccione el archivo de movimientos", "Archivo de movimientos", "*.mov"
        )
        if validacion:
            alertas("Archivo cargado", "verde")
            leer_movimientos(inventario, url_temporal)
            inventario.crear_informe()
            alertas("Datos Actualizados", "verde")
        else:
            alertas("Seleccione un archivo", "rojo")
            menuOpciones("2", inventario)
    # Crear Informe de Inventario
    elif opcion == "3":
        if len(inventario.productos) == 0:
            alertas("Primero agregue el archivo .inv", "rojo")
            return
        inventario.crear_informe()
        alertas("Informe actualizado", "verde")
    # Cerre de Sesión
    elif opcion == "4":
        alertas("Cierre de Sesión", "verde")
    else:
        alertas("Opción no valida", "rojo")


def alertas(texto, color):
    colores = {
        "fondo_rojo": "\033[41m",
        "texto_rojo": "\033[31m",
        "fondo_verde": "\033[42m",
        "texto_verde": "\033[32m",
    }
    tipo = "✖ Error" if color == "rojo" else "✔ Operación exitosa"
    print(f"\n{colores['fondo_'+color]} {tipo} \033[0m", end="")
    print(f"{colores['texto_'+color]} {texto} \033[0m\n")


class Producto:
    def __init__(self, nombre, cantidad, p_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.p_unitario = round(p_unitario, 2)
        self.ubicacion = ubicacion

    def calcular_total(self):
        return round(self.cantidad * self.p_unitario, 2)


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
            alertas("La cantidad debe ser mayo a 0", "rojo")
            return
        if p_unitario < 0:
            alertas("El precio unitario debe ser mayor a 0", "rojo")
            return
        self.productos.append(Producto(nombre, cantidad, p_unitario, ubicacion))

    def agregar_stock(self, nombre, cantidad, ubicacion):
        if cantidad < 0:
            alertas("[Agregando] El cantidad debe ser mayor a 0", "rojo")
            return
        producto = self.buscar_producto(nombre, ubicacion)
        if producto:
            producto.cantidad += cantidad
        else:
            alertas(
                f"[Agregando] El producto: {nombre} no existe en la ubicación: {ubicacion}",
                "rojo",
            )

    def vender_producto(self, nombre, cantidad, ubicacion):
        if cantidad < 0:
            alertas("[Vendiendo] El cantidad debe ser mayor a 0", "rojo")
            return
        producto = self.buscar_producto(nombre, ubicacion)
        if producto:
            if producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
            else:
                alertas(
                    f"[Vendiendo] No hay suficientes existencias de: {nombre} en {ubicacion}",
                    "rojo",
                )
        else:
            alertas(
                f"[Vendiendo] El producto: {nombre} no existe en la ubicación: {ubicacion}",
                "rojo",
            )

    def crear_informe(self):
        with open("informe.txt", "w", encoding="UTF-8") as archivo:
            archivo.write(
                "╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n"
            )
            archivo.write(
                "║                                                  INFORME DE INVENTARIO                                               ║\n"
            )
            # archivo.write("Producto\tCantidad\tPrecio Unitario\tUbicacion\n")
            archivo.write(
                "╠════════════════════════════════╦════════════════╦═════════════════════╦═════════════════════╦════════════════════════╣\n"
            )
            archivo.write(
                "║       NOMBRE DEL PRODUCTO      ║    CANTIDAD    ║   PRECIO UNITARIO   ║     VALOR TOTAL     ║        UBICACIÓN       ║\n"
            )
            archivo.write(
                "╠════════════════════════════════╬════════════════╬═════════════════════╬═════════════════════╬════════════════════════╣\n"
            )
            for dato in self.productos:
                archivo.write("║")
                archivo.write(" %-31s" % dato.nombre)
                archivo.write("║")
                archivo.write(" %-15s" % dato.cantidad)
                archivo.write("║")
                archivo.write(" %-20s" % f"${dato.p_unitario}")
                archivo.write("║")
                archivo.write(" %-20s" % f"${dato.calcular_total()}")
                archivo.write("║")
                archivo.write(" %-23s" % dato.ubicacion)
                archivo.write("║\n")
            archivo.write(
                "╚════════════════════════════════╩════════════════╩═════════════════════╩═════════════════════╩════════════════════════╝"
            )
            archivo.write("\n")


def pedir_archivos(titulo, mensaje, extension):
    archivo = filedialog.askopenfilename(title=titulo, filetypes=[(mensaje, extension)])
    return (archivo, archivo != "")


def leer_inicio(inventario, url_archivo):
    with open(url_archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea == "" or linea == "\n" or linea.split(" ")[0] != "crear_producto":
                continue
            texto_datos = linea.split(" ")[1]
            inventario.crear_producto(
                texto_datos.split(";")[0].strip(),
                int(texto_datos.split(";")[1].strip()),
                float(texto_datos.split(";")[2].strip()),
                texto_datos.split(";")[3].strip(),
            )


def leer_movimientos(inventario, url_archivo):
    with open(url_archivo, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea == "" or linea == "\n":
                continue
            texto_datos = linea.split(" ")[1]
            if linea.split(" ")[0] == "agregar_stock":
                inventario.agregar_stock(
                    texto_datos.split(";")[0].strip(),
                    int(texto_datos.split(";")[1].strip()),
                    texto_datos.split(";")[2].strip(),
                )
            elif linea.split(" ")[0] == "vender_producto":
                inventario.vender_producto(
                    texto_datos.split(";")[0].strip(),
                    int(texto_datos.split(";")[1].strip()),
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
