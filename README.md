<header><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"></header>
<!-- Título del Proyecto -->
<h1 align="center">Practica</h1>
<p align="center">
  <!--<img style="border-radius:10px;" align="center" src=""/>-->
    <a href="#"><img src="https://i.imgur.com/QZQLGff.png"></a>
</p>
<!-- Descripción del Proyecto -->
<p align="center">Programa en consola para la gestión de inventario, registro de movimientos, y generación de informes utilizando archivos de texto.</p>

<!-- Badges (por ejemplo, estado de construcción, licencia, etc.) -->
<div align="center">
🙍‍♂️ Joab Israel Ajsivinac Ajsivinac 🆔 202200135
</div>
<div align="center">
📕 Lenguajes Formales y de Programación
</div>
<div align="center"> 🏛 Universidad San Carlos de Guatemala</div>
<div align="center"> 📆 Segundo Semestre 2023</div>

<!-- Tabla de Contenidos -->
## 📋 Tabla de Contenidos

<!-- - [📋 Tabla de Contenidos](#-tabla-de-contenidos) -->
- [📋 Tabla de Contenidos](#-tabla-de-contenidos)
- [⚒ Requerimientos](#-requerimientos)
- [⚙ Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [⚽ Objetivos](#-objetivos)
- [🧮 Como funciona](#-como-funciona)
- [📟 Instalación](#-instalación)
- [📷 Capturas](#-capturas)


<!-- Requerimientos -->
## ⚒ Requerimientos

<ul>
  <li>Windows 8 o Superior</li>
  <li>macOS Catalina o Superior</li>
  <li>Linux: Ubuntu, Debian, CentOS, Fedora, etc.</li>
  <li>Python 3.10.8 o Superior</li>
  <li>Tkinter 8.6 o superior</li>
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

## ⚽ Objetivos
* **Objetivo General**
    * Diseñar y desarrollar un sistema de gestión de gestión de inventario que facilite la administración eficiente de productos, permitiendo el registro de inventario y movimientos con la capacidad de generar informes pertinentes. 
* **Objetivos Específicos**
    * Elaborar un sistema que proporcione una estructura para el almacenamiento de la información de los productos en inventario, involucrando la implementación de métodos eficaces.
    * Dar las herramientas para el registro de movimientos de un producto, desde la carga inicial hasta la generación del informe.
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
```
Se encarga de leer el archivo .inv dada una ruta especifica del sistema. Itera las líneas existentes del archivo .inv y valida que no sean saltos de línea, líneas vacías, si la línea es válida procede a crear el producto con los método de la clase ControlInventario.

Los parámetros enviados, son los valores de cada línea del archivo .inv que se separan dos veces con el .split(), una para tener los datos y el nombre del comando, y la segunda para obtener los datos por separado (nombre del producto, cantidad, precio unitario y ubicación)

```python
inventario.crear_producto(
    texto_datos.split(";")[0].strip(),
    int(texto_datos.split(";")[1].strip()),
    float(texto_datos.split(";")[2].strip()),
    texto_datos.split(";")[3].strip(),
    )
```

**Nota:** Se usó with open para la lectura de los archivos, para evitar el cierre manual del archivo una vez se termine el proceso, tambien para tener mejor manejo de excepciones para prevenir daños en los datos y mantener la integridad del programa. (En la Método crear_informe de la clase ControlInventario se usa with open tambien para la escritura del informe, al igual que en la función de lectura de archivos de movimiento)

```python
with open(url_archivo, "r", encoding="UTF-8") as archivo:
```
<h3>Función de lectura de archivo .mov</h3>


Se encarga de leer el archivo .mov dada una ruta específica del sistema. Itera las líneas existentes del archivo .mov y valida que no sean saltos de línea, líneas vacías, si la línea es válida procede a verificar que tipo de comando se está recibiendo para poder enviar la información necesaria a la clase ControlInventario.

Los parámetros enviados, son los valores de cada línea del archivo .inv que se separan dos veces con el .split(), una para tener los datos y el nombre del comando, y la segunda para obtener los datos por separados (nombre del producto, cantidad, precio unitario y ubicación). Con el nombre del comando se verifica si se desea agregar o vender algún producto.

Si el comando es agregar_stock se procede a llamar al método agregar_stock de la clase control de Inventario.

Si el comando es vender_producto se procede a llamar al método vender_producto de la clase control de Inventario.

```python
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

Se usa .strip() para remover los espacios en blanco al inicio y al final del valor obtenido 

<h3>Clase Control de Inventario</h3>

Está compuesta de cinco métodos, los cuales se encargan de manejar los datos de los productos.
<blockquote>

**Variable Productos**

```python
self.productos = []
```
Esta variable almacena todos los productos, como objetos que tienen todos los parametros de la clase Producto

</blockquote>

<br>

<blockquote>

**Método crear_producto**

```python
def crear_producto(self, nombre, cantidad, p_unitario, ubicacion):
```
Recibe como parámetros, el nombre, cantidad, precio unitario y ubicación de un producto y se encarga de agregar el producto al arreglo productos si la cantidad y el precio unitario es mayor a cero. Se hace uso de la propiedad append para agregar los productos del archivo a la lista de productos.

```python
self.productos.append(Producto(nombre, cantidad, p_unitario, ubicacion))
```
</blockquote>
<br>
<blockquote>

**Método agregar_stock**

```python
def agregar_stock(self, nombre, cantidad, ubicacion):
```

Recibe como parámetro el nombre, cantidad y ubicación de un producto y se encarga de agregar más unidades a los productos existentes, siempre y cuando dicha cantidad sea mayor a 0, y que el producto este en la ubicación ingresada si no cumple con las validaciones anteriores se muestra un error en consola.

El proceso de agregado es: primero buscar el producto dentro del arreglo con el método buscar_producto para luego aumentar la cantidad de stock de un producto en concreto.

```python
producto.cantidad += cantidad
```

</blockquote>
<br>
<blockquote>

**Método buscar_producto**

```python
def buscar_producto(self, nombre, ubicacion):
```
Recibe como parámetro el nombre y la ubicación de un producto y se encarga de iterar todos los elementos que están guardados en el arreglo de productos, donde se busca que un producto tenga el mismo nombre que el parámetro enviado y que dicho producto este en la ubicación dada y retorna un objeto de tipo Producto si lo encuentra, de lo contrario retorna un valor None.

```python
for producto in self.productos:
    if producto.nombre == nombre and producto.ubicacion == ubicacion:
        return producto
return None
```
</blockquote>
<br>
<blockquote>

**Método vender_producto**

```python
def vender_producto(self, nombre, cantidad, ubicacion):
```
Recibe como parámetro nombre, cantidad y ubicación de un producto y se encarga actualizar el stock de un producto luego de una venta, teniendo en cuenta que el valor no puede ser negativo o que el valor pedido sea mayor al valor stock inicial que se tiene, si no se cumple las restricciones se muestra un error en consola. Si cumple con las restricciones se reduce la cantidad del producto.

```python
producto.cantidad -= cantidad
```

</blockquote>
<br>
<blockquote>

**Método crear_informe**


```python
def crear_informe(self):
```
Este método se encarga de iterar con un bucle for todos los elementos del arreglo productos, para luego agregarlos al archivo informes.txt
</blockquote>

<h3>Función Menu Opciones</h3>

```python
def menuOpciones(opcion, inventario):
```
Recibe como parametros la opcion elegida por el usuario y una variable inventario y se encarga de llamar a las funciones correctas según la opción elegida por el usuario, verificando que la opción elegida este entre las opciones validas, si la opción no es válida muestra un error en consola.

<blockquote>

**Opción 1**

Se encarga de llamar a la función pedir_archivos que retorna una tupla con los datos obtenidos si la ruta del archivo seleccionado es correcta se procede a llamar a la función leer_inicio para poder cargar los datos de los productos en memoria, de lo contrario vuelve a pedir que seleccione un archivo, esto infinitamente hasta que ingrese el archivo correcto.
</blockquote>
<blockquote>

**Opción 2**

Se verifica primero que el tamaño de la lista de productos sea diferente de 0 ya que si es igual que 0 es que no tiene datos.

Se encarga de llamar a la función pedir_archivos que retorna una tupla con los datos obtenidos si la ruta del archivo seleccionado es correcta se procede a llamar a la función leer_movimientos para poder aplicar los cambios necesarios a los productos, de lo contrario vuelve a pedir que seleccione un archivo, esto infinitamente hasta que ingrese el archivo correcto.

</blockquote>
<blockquote>

**Opción 3**

Se verifica primero que el tamaño de la lista de productos sea diferente de 0 ya que si es igual que 0 es que no tiene datos, para luego llamar al método de crear_informe() para la creación del informe. 
</blockquote>
<blockquote>

**Opción 4**

Sale del bucle para poder terminar la ejecución del programa 
</blockquote>

Si se ingresa un valor diferente a la opción: 1,2,3 y 4 se muestra un error en consola.

<h3>Main</h3>
Instancia un objeto de tipo ControlInventario que contendrá todos los datos de los productos

```python
inventario = ControlInventario()
```
dentro de un bucle while se llama al menu inicial, y pide la opción que desee elegir al usuario para luego mandar, la opción y la variable inventario al método menuOpciones para que dicho método realice la opción pedida por el usuario.
<!-- Instalación -->
## 📟 Instalación
Descargue el código o bien clone el repositorio en una carpeta.

Si se opta por la clonación se hace con la siguiente linea de código en terminal (Antes de ejecutar el codigo asegurese de estar en la carpeta donde lo quiere descargar)

```bash
git clone https://github.com/J-Ajsivinac/LFP_S2_2023_Practica_202200135
```

## 📷 Capturas
![Captura 1](/img/menu.png)
<p align="center">Menú principal</p>

![Captura 2](/img/reportes.png)
<p align="center">Informe generado</p>