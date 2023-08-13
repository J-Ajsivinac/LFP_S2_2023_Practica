<header><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"></header>
<!-- Título del Proyecto -->
<h1 align="center">Practica</h1>

<!-- Descripción del Proyecto -->
<p align="center">Programa de gestión de inventario y registro de movimientos utilizando archivos de texto.</p>

<!-- Badges (por ejemplo, estado de construcción, licencia, etc.) -->
<div align="center">
🙍‍♂️ Joab Israel Ajsivinac Ajsivinac, 🆔 202200135
</div>
<div align="center">
📕 Lenguajes Formales y de Programación
</div>

<!-- Tabla de Contenidos -->
## 📋 Tabla de Contenidos

<!-- - [📋 Tabla de Contenidos](#-tabla-de-contenidos) -->
- [📋 Tabla de Contenidos](#-tabla-de-contenidos)
- [⚒ Requerimientos](#-requerimientos)
- [⚙ Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [🧮 Como funciona](#-como-funciona)
- [📟 Instalación](#-instalación)
- [📝 Opciones](#-opciones)
- [📖 Uso](#-uso)


<!-- Requerimientos -->
## ⚒ Requerimientos

<ul>
  <li>Windows 8 o Superior</li>
  <li>macOS Catalina o Superior</li>
  <li>Linux: Ubuntu, Debian, CentOS, Fedora, etc.</li>
  <li>Python 3.10.8 o Superior</li>
  <li>Tkinter 8.6</li>
</ul>

## ⚙ Tecnologías Utilizadas

<div align="center" style="display:flex;justify-content:center;gap:20px">
 <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,vscode,git" />
  </a>
</div>
<ul>
  <li>Python</li>
  <li>Visual Studio Code</li>
  <li>Git</li>
</ul>

<!-- Uso -->
## 🧮 Como funciona
<h3>Clase Producto</h3>

```python
def __init__(self, nombre, cantidad, p_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.p_unitario = round(p_unitario, 2)
        self.ubicacion = ubicacion

def calcular_total(self):
    return round(self.cantidad * self.p_unitario, 2)
```
Esta clase se ocupa de especificar que datos de los productos se guardarán posteriormente en un arreglo, además de calcular el valor total de un producto, redondeado a dos decimales.

<h3>Función Pedir archivos</h3>

```python
def pedir_archivos(titulo, mensaje, extension):
    archivo = filedialog.askopenfilename(title=titulo, filetypes=[(mensaje, extension)])
    return (archivo, archivo != "")
```

Se encarga de abrir una ventana para poder elegir un archivo en especifico y retorna una tupla con la dirección de dicho archivo junto si el archivo no es vacio (True o False)

<h3>Función de lectura de archivo .inv</h3>

```python
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
```
Se encarga de leer el archivo .inv dada una ruta especifica del sistema. Itera las lineas existentes del archivo .inv y valida que no sean saltos de linea, lineas vacias, si la linea es válida procede a crear el producto con los método de la clase ControlInventario.

Los parametros enviados, son los valores de cada linea del archivo .inv que se separan dos veces con el .split(), una para tener los datos y el nombre del comando, y la segunda para obtener los datos por serparados (nombre del producto, cantidad, precio unitario y ubicación)

<h3>Función de lectura de archivo .mov</h3>

```python
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
```
Se encarga de leer el archivo .mov dada una ruta especifica del sistema. Itera las lineas existentes del archivo .mov y valida que no sean saltos de linea, lineas vacias, si la linea es válida procede a verificar que tipo de commando se esta recibiendo para poder enviar la información necesaria a la clase ControlInventario.

Los parametros enviados, son los valores de cada linea del archivo .inv que se separan dos veces con el .split(), una para tener los datos y el nombre del comando, y la segunda para obtener los datos por serparados (nombre del producto, cantidad, precio unitario y ubicación). Con el nombre del comando se verifica si se desea agregar o vender algún producto.

**Nota:** Se usó with open para la lectura de los archivos, para evitar el cierre manual del archivo una vez se termine el proceso, tambíen para tener mejor manejo de excepciones para prevenir daños en los datos y mantener la integridad del programa. (En la Método crear_informe de la clase ControlInventario se usa with open tambien para la escritura del informe.)



<h3>Clase Control de Inventario</h3>

Está compuesta de cinco métodos, los cuales se encargan de manejar los datos de los productos.
<blockquote>

**Variable Productos**

```python
self.productos = []
```
Esta variable almacena todos los productos

</blockquote>

<br>

<blockquote>

**Método crear_producto**

```python
def crear_producto(self, nombre, cantidad, p_unitario, ubicacion):
    if cantidad < 0:
        alertas("La cantidad debe ser mayo a 0", "rojo")
        return
    if p_unitario < 0:
        alertas("El precio unitario debe ser mayor a 0", "rojo")
        return
    self.productos.append(Producto(nombre, cantidad, p_unitario, ubicacion))
```
Se encarga de agregar el producto al arrelgo productos si la cantidad y el precio unitario es mayor a cero.
</blockquote>
<br>
<blockquote>

**Método crear_stock**

```python
def agregar_stock(self, nombre, cantidad, ubicacion):
    if cantidad < 0:
        alertas("[Agregando] El cantidad debe ser mayor a 0", "rojo")
        return
    producto = self.buscar_producto(nombre, ubicacion)
    if producto:
        producto.cantidad += cantidad
    else:
        alertas(
            f"[Agregando] El producto: {nombre} no existe en la ubicación: {ubicacion}","rojo",
        )
```
Se encarga de agregar más unidades a los productos existentes, siempre y cuando dicha cantidad sea mayor a 0, y que el prodcuto este en la ubicación ingresada.
</blockquote>
<br>
<blockquote>

**Método buscar_producto**

```python
def buscar_producto(self, nombre, ubicacion):
    for producto in self.productos:
        if producto.nombre == nombre and producto.ubicacion == ubicacion:
            return producto
    return None
```
Se encarga de buscar un producto en especifico en el arreglo productos, y retorna un objeto de tipo Producto si lo encuentra, de lo contrario retorna un valor None
</blockquote>
<br>
<blockquote>

**Método vender_producto**


```python
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
```
Este método se encarga actualizar el stock de un producto luego de una venta, teniendo en cuenta que el valor no puede ser negativo o que el valor pedido sea mayor al valor stock incial que se tiene, si no se cumple las restricciones se muestra un error en consola.
</blockquote>
<br>
<blockquote>

**Método crear_informe**


```python
def crear_informe(self):
     with open("informe.txt", "w", encoding="UTF-8") as archivo:
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
```
Nota: Los elementos decorativos como el encabezado con los nombres se omitieron en el codigo anterior para hacer más legible el código

Este método se encarga de iterar con un bucle for todos los elementos del arreglo productos, para luego agregarlos al archivo informes.txt
</blockquote>

<h3>Función Menu Opciones</h3>

```python
def menuOpciones(opcion, inventario):
    # Cargar inventario incial
    if opcion == "1":
        url_temporal, validacion = pedir_archivos(
            "Seleccione el archivo de inicio", "Archivo de inicio", "*.inv"
        )
        if validacion:
            alertas("Archivo cargado", "verde")
            leer_inicio(inventario, url_temporal)
            alertas("Informe actualizado", "verde")
        else:
            alertas("Seleccione el archivo de inicio", "rojo")
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
```
Se encarga de llamar a las funciones correctas según la opción elegida por el usuario, verificando que la opción elegida este entre las opciones validas, si la opción no es válida muestra un error en consola.

<!-- Instalación -->
## 📟 Instalación
Descargue el código o bien clone el repositorio en una carpeta.

Si se opta por la clonación se hace con la siguiente linea de código en terminal (Antes de ejecutar el codigo asegurese de estar en la carpeta donde lo quiere descargar)

```bash
git clone https://github.com/J-Ajsivinac/LFP_S2_2023_Practica_202200135
```

## 📝 Opciones
<p>El programa cuenta con las siguientes funcionalidaes.</p>
<ul>
  <li>Cargar Inventario Inicial</li>
  <li>Cargar Instrucciones de movimientos</li>
  <li>Crear Informe de Inventario</li>
  <li>Salir</li>
</ul>

## 📖 Uso
Se le desplegara las siguiente opciones en consola

![Captura 1](/img/menu.png)

Deberá ingresar el número de la opción que desee.
* Si selecciona la opción 1, podra elegir un archivo .inv para cargar los datos inciiales en su inventario

* Si selecciona la opción 2, podra elegir un archivo .mov para cargar los movimientos que desee para su inventario

* Si selecciona la opción 3, se agregará un archivo llamado informe con los datos de los productos, como lo muestra la siguiente imagen.
![Captura 2](/img/reportes.png)

* Si selecciona la opción 3, se procedera cerrar el ciclo de preguntas de opciones.
